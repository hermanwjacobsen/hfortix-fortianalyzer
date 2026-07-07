"""Model registry for automatic Pydantic model selection based on API URL.

.. warning:: **EXPERIMENTAL — effectively inert in this release.**
    The generator does not yet produce the ``api/models/`` Pydantic package,
    so ``_register_known_models()`` finds nothing to register and
    ``get_model_for_url()`` always returns ``None``. Forward-compatible stub.
"""

from typing import Dict, Optional, Type

from pydantic import BaseModel


class ModelRegistry:
    """
    Registry for mapping API URLs to Pydantic models.

    This enables automatic parsing of API responses into properly typed
    Pydantic models based on the endpoint being called.
    """

    def __init__(self) -> None:
        """Initialize the model registry."""
        self._registry: Dict[str, Type[BaseModel]] = {}

    def register(self, url_pattern: str, model_class: Type[BaseModel]) -> None:
        """
        Register a Pydantic model for a specific URL pattern.

        Args:
            url_pattern: URL pattern (e.g., "/dvmdb/device")
            model_class: Pydantic model class to use for this URL
        """
        self._registry[url_pattern] = model_class

    def get_model(self, url: str) -> Optional[Type[BaseModel]]:
        """
        Get the Pydantic model class for a given URL.

        Args:
            url: API URL path

        Returns:
            Pydantic model class if registered, None otherwise
        """
        # Try exact match first
        if url in self._registry:
            return self._registry[url]

        # Try to match base URL (without parameters)
        # e.g., "/dvmdb/device/FGT1" -> "/dvmdb/device"
        for pattern, model in self._registry.items():
            if url.startswith(pattern):
                return model

        return None


# Global registry instance
_model_registry = ModelRegistry()


def register_model(url_pattern: str, model_class: Type[BaseModel]) -> None:
    """
    Register a Pydantic model for automatic response parsing.

    Args:
        url_pattern: URL pattern to match
        model_class: Pydantic model class
    """
    _model_registry.register(url_pattern, model_class)


def get_model_for_url(url: str) -> Optional[Type[BaseModel]]:
    """
    Get the registered Pydantic model for a URL.

    Args:
        url: API URL path

    Returns:
        Pydantic model class if available
    """
    return _model_registry.get_model(url)


# Auto-register known models
def _register_known_models() -> None:
    """Register all known Pydantic models."""
    try:
        from hfortix_fortianalyzer.api.models.dvmdb.device import (
            DvmdbDeviceModel,
        )

        register_model("/dvmdb/device", DvmdbDeviceModel)
    except ImportError:
        pass

    try:
        from hfortix_fortianalyzer.api.models.dvmdb.adom import DvmdbAdomModel

        register_model("/dvmdb/adom", DvmdbAdomModel)
    except ImportError:
        pass


# Register models on module import
_register_known_models()


__all__ = ["ModelRegistry", "register_model", "get_model_for_url"]

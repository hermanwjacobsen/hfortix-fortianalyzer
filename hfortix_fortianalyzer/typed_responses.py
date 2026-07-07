"""Typed response classes for FortiAnalyzer API endpoints.

.. warning:: **EXPERIMENTAL — typed iteration currently falls back to
    ``FortiAnalyzerObject``.** The Pydantic models these classes would wrap
    (``api/models/``) are not generated yet, so iteration yields generic
    attribute-access objects. Forward-compatible stub.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator

if TYPE_CHECKING:
    try:
        from hfortix_fortianalyzer.api.models.dvmdb.device import (
            DvmdbDeviceModel,
        )
    except (ImportError, SyntaxError, NameError):
        DvmdbDeviceModel = Any  # type: ignore

from hfortix_fortianalyzer.models import (
    FortiAnalyzerObject,
    FortiAnalyzerResponse,
)


class DvmdbDeviceResponse(FortiAnalyzerResponse):
    """Typed response for /dvmdb/device endpoint."""

    def __iter__(self) -> Iterator[Any]:  # type: ignore[override]
        """
        Iterate over devices as typed Pydantic models.

        Yields:
            DvmdbDeviceModel instances with full type safety (or FortiAnalyzerObject if model unavailable)
        """
        # Try to import the Pydantic model
        try:
            from hfortix_fortianalyzer.api.models.dvmdb.device import (
                DvmdbDeviceModel,
            )

            model_available = True
        except (ImportError, SyntaxError, NameError):
            model_available = False

        data = self.data
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    if model_available:
                        try:
                            yield DvmdbDeviceModel(**item)
                            continue
                        except Exception:
                            # Fall back to FortiAnalyzerObject if parsing fails
                            pass
                    # Return wrapped object for dynamic access
                    yield FortiAnalyzerObject(item)


__all__ = ["DvmdbDeviceResponse"]

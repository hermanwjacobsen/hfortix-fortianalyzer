"""
FortiAnalyzer Response Models

Provides structured wrappers for FortiAnalyzer JSON-RPC API responses.
"""

from __future__ import annotations

import json as json_module
from typing import TYPE_CHECKING, Any, Generic, Iterator, TypeVar

if TYPE_CHECKING:
    from pydantic import BaseModel

# TypeVar for generic typed list support
_ObjectT = TypeVar("_ObjectT", bound="FortiAnalyzerObject")
_ModelT = TypeVar("_ModelT", bound="BaseModel")


class FortiAnalyzerResponse:
    """
    Structured wrapper for FortiAnalyzer JSON-RPC API responses.

    Provides clean attribute access to API response data with automatic
    flattening of the nested JSON-RPC structure.

    FortiAnalyzer JSON-RPC responses have this structure:
    {
        "id": 1,
        "result": [{
            "status": {"code": 0, "message": "OK"},
            "url": "/pm/config/adom/root/...",
            "data": { ... actual data ... }
        }]
    }

    This class flattens the structure and provides:
    - HTTP layer properties (http_status_code, http_response_time, etc.)
    - API layer properties (api_status_code, api_status_message, api_id, api_raw)
    - Direct attribute access to data fields (alt_primary, primary, timeout, etc.)

    Features:
    - Attribute access to flattened data: response.alt_primary, response.primary
    - HTTP metadata: response.http_status_code, response.http_response_time
    - API metadata: response.api_status_code, response.api_status_message
    - Raw data access: response.raw, response.json, response.dict
    - Iteration support for list responses

    Examples:
        >>> # Get DNS configuration
        >>> result = faz.api.pm.config.system.dns.get(adom="root", devprof="default")
        >>>
        >>> # Direct attribute access to flattened data
        >>> result.alt_primary      # '0.0.0.0'
        >>> result.primary          # '0.0.0.0'
        >>> result.timeout          # 5
        >>>
        >>> # HTTP layer (transport)
        >>> result.http_status_code      # 200
        >>> result.http_response_time    # 45.2 (ms)
        >>>
        >>> # API layer (FortiAnalyzer response)
        >>> result.api_status_code       # 0 (success)
        >>> result.api_status_message    # 'OK'
        >>> result.api_id                # 1565
        >>> result.api_url               # '/pm/config/adom/root/devprof/default/system/dns'
        >>>
        >>> # Raw access
        >>> result.raw                   # Full JSON-RPC response dict
        >>> result.json                  # Pretty-printed JSON string
        >>> result.dict                  # Flattened data as dict

    Args:
        data: Dictionary from FortiAnalyzer JSON-RPC API response
        http_status_code: HTTP status code (200, 404, 500, etc.)
        response_time: Response time in seconds
        request_info: HTTP request information
    """

    def __init__(
        self,
        data: dict[str, Any],
        http_status_code: int | None = None,
        response_time: float | None = None,
        request_info: dict[str, Any] | None = None,
    ):
        """
        Initialize FortiAnalyzer response object.

        Args:
            data: Full JSON-RPC response dictionary
            http_status_code: HTTP status code from response
            response_time: Response time in seconds
            request_info: Request metadata (method, url, params, data)
        """
        self._raw_data = data

        # Extract HTTP metadata if available (added by HTTPClientJSONRPC)
        http_meta = data.get("_http_metadata", {})
        self._http_status_code = (
            http_meta.get("status_code") or http_status_code
        )
        self._response_time = http_meta.get("response_time") or (
            response_time * 1000 if response_time else None
        )

        # Extract request info from metadata or use provided
        if http_meta:
            self._request_info = {
                "method": http_meta.get("method"),
                "url": http_meta.get("url"),
            }
        else:
            self._request_info = request_info

        # Extract flattened data from JSON-RPC structure
        # Structure: {"id": 1, "result": [{"status": {...}, "data": {...}}]}
        self._flattened_data: dict[str, Any] | list[Any] = {}
        self._is_list_response = False
        self._api_url: str | None = None

        if isinstance(data, dict):
            result = data.get("result", [])
            if isinstance(result, list) and len(result) > 0:
                first_result = result[0]
                if isinstance(first_result, dict):
                    # Store the API URL for model lookup
                    self._api_url = first_result.get("url")

                    # Extract the actual data
                    result_data = first_result.get("data", {})
                    if isinstance(result_data, dict):
                        self._flattened_data = result_data
                    elif isinstance(result_data, list):
                        # Data is a list (e.g., list of devices)
                        self._flattened_data = result_data
                        self._is_list_response = True
                    else:
                        # If data is not a dict or list, store the whole first result
                        self._flattened_data = first_result

    def _get_pydantic_model_class(self) -> type[BaseModel] | None:
        """
        Get the Pydantic model class for this response based on API URL.

        Returns:
            Pydantic model class if available, None otherwise
        """
        if not self._api_url:
            return None

        try:
            from hfortix_fortianalyzer.model_registry import get_model_for_url

            return get_model_for_url(self._api_url)
        except ImportError:
            return None

    def as_models(self) -> list[BaseModel] | BaseModel | None:
        """
        Parse response data as Pydantic models.

        .. warning:: **EXPERIMENTAL — currently always returns None.**
            Pydantic model generation is not wired into the generator yet
            (no ``api/models/`` package is shipped), so no models are ever
            registered. This method is a forward-compatible stub. Use
            attribute access on the response instead
            (``for dev in response: dev.name``).

        Returns:
            - List of Pydantic models if response is a list
            - Single Pydantic model if response is a dict
            - None if no model is registered for this URL (always, currently)
        """
        model_class = self._get_pydantic_model_class()
        if not model_class:
            return None

        if isinstance(self._flattened_data, list):
            # Parse each item as a Pydantic model
            return [model_class(**item) for item in self._flattened_data]
        elif isinstance(self._flattened_data, dict):
            # Parse single item as Pydantic model
            return model_class(**self._flattened_data)

        return None

    # ========================================================================
    # HTTP Layer Properties (Transport)
    # ========================================================================

    @property
    def http_status_code(self) -> int | None:
        """HTTP status code (200, 404, 500, etc.) from HTTPS connection."""
        return self._http_status_code

    @property
    def http_response_time(self) -> float | None:
        """Response time in milliseconds for the HTTP request."""
        return self._response_time

    @property
    def http_method(self) -> str | None:
        """HTTP method used (typically POST for JSON-RPC)."""
        return self._request_info.get("method") if self._request_info else None

    @property
    def http_url(self) -> str | None:
        """Full HTTP URL that was requested."""
        return self._request_info.get("url") if self._request_info else None

    # ========================================================================
    # API Layer Properties (FortiAnalyzer JSON-RPC Response)
    # ========================================================================

    @property
    def api_status_code(self) -> int | None:
        """
        FortiAnalyzer API status code from response.

        0 = success, negative values = errors

        Common codes:
        - 0: Success
        - -1: Generic error
        - -2: Invalid parameters
        - -3: Object not found
        """
        result = self._raw_data.get("result", [])
        if isinstance(result, list) and len(result) > 0:
            status = result[0].get("status", {})
            if isinstance(status, dict):
                return status.get("code")
        return None

    @property
    def api_status_message(self) -> str | None:
        """FortiAnalyzer API status message ('OK' for success, error message otherwise)."""
        result = self._raw_data.get("result", [])
        if isinstance(result, list) and len(result) > 0:
            status = result[0].get("status", {})
            if isinstance(status, dict):
                return status.get("message")
        return None

    @property
    def api_id(self) -> int | None:
        """JSON-RPC request ID from the response."""
        return self._raw_data.get("id")

    @property
    def api_url(self) -> str | None:
        """FortiAnalyzer API URL path from the response."""
        result = self._raw_data.get("result", [])
        if isinstance(result, list) and len(result) > 0:
            return result[0].get("url")
        return None

    @property
    def api_session(self) -> str | None:
        """Session token from login response."""
        return self._raw_data.get("session")

    @property
    def api_raw(self) -> dict[str, Any]:
        """Full raw FortiAnalyzer JSON-RPC response."""
        return self._raw_data

    # ========================================================================
    # Data Access Methods
    # ========================================================================

    @property
    def raw(self) -> dict[str, Any]:
        """Full raw JSON-RPC response dictionary."""
        return self._raw_data

    @property
    def data(self) -> dict[str, Any] | list[Any]:
        """Access the raw flattened data (dict or list)."""
        if isinstance(self._flattened_data, list):
            return self._flattened_data
        return self._flattened_data

    @property
    def dict(self) -> dict[str, Any]:
        """Flattened data as dictionary (returns empty dict if data is a list)."""
        if isinstance(self._flattened_data, dict):
            return self._flattened_data.copy()
        return {}

    @property
    def json(self) -> str:
        """Pretty-printed JSON string of flattened data."""
        data = (
            self._flattened_data
            if isinstance(self._flattened_data, (dict, list))
            else {}
        )
        return json_module.dumps(data, indent=2)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a field value with optional default.

        Args:
            key: Field name
            default: Default value if field doesn't exist

        Returns:
            Field value or default
        """
        if isinstance(self._flattened_data, dict):
            return self._flattened_data.get(key, default)
        return default

    # ========================================================================
    # Dynamic Attribute Access (Flattened Data)
    # ========================================================================

    def __getattr__(self, name: str) -> Any:
        """
        Provide attribute access to flattened data fields.

        This allows response.alt_primary instead of response['data']['alt-primary']

        Args:
            name: Attribute name

        Returns:
            Field value from flattened data

        Raises:
            AttributeError: If field doesn't exist or data is a list
        """
        # If data is a list, attribute access doesn't make sense
        if not isinstance(self._flattened_data, dict):
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}' "
                f"(response data is a list, use iteration or indexing)"
            )

        # Convert Python attribute name to API field name (underscore to hyphen)
        api_field_name = name.replace("_", "-")

        # Try exact match first
        if name in self._flattened_data:
            value = self._flattened_data[name]
            return self._wrap_value(value)

        # Try with hyphen conversion
        if api_field_name in self._flattened_data:
            value = self._flattened_data[api_field_name]
            return self._wrap_value(value)

        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}' "
            f"(not found in API response data)"
        )

    def _wrap_value(self, value: Any, use_pydantic: bool = False) -> Any:
        """
        Wrap dict/list values for cleaner access.

        Args:
            value: Value to potentially wrap
            use_pydantic: If True and model available, parse as Pydantic model

        Returns:
            Wrapped value, Pydantic model, or original value
        """
        if isinstance(value, dict):
            # Try to parse as Pydantic model if requested and model is available
            if use_pydantic:
                model_class = self._get_pydantic_model_class()
                if model_class:
                    try:
                        return model_class(**value)
                    except Exception:
                        # Fall back to FortiAnalyzerObject if parsing fails
                        pass
            return FortiAnalyzerObject(value)
        elif isinstance(value, list):
            return FortiAnalyzerList(value)
        return value

    # ========================================================================
    # Container Protocol Support
    # ========================================================================

    def __getitem__(self, key: str | int) -> Any:
        """
        Dictionary-style access to flattened data or list indexing.

        Supports both Python-style (underscore) and API-style (hyphen) keys for dicts.
        Supports integer indexing for list responses.
        """
        # If data is a list, support integer indexing
        if isinstance(self._flattened_data, list):
            if isinstance(key, int):
                return self._wrap_value(self._flattened_data[key])
            raise TypeError(
                f"list indices must be integers, not {type(key).__name__}"
            )

        # If data is a dict, support string keys
        if not isinstance(key, str):
            raise TypeError(
                f"dict keys must be strings, not {type(key).__name__}"
            )

        # Try direct key first (hyphenated API name)
        if key in self._flattened_data:
            return self._wrap_value(self._flattened_data[key])

        # Try converting underscore to hyphen (Python name → API name)
        hyphenated = key.replace("_", "-")
        if hyphenated in self._flattened_data:
            return self._wrap_value(self._flattened_data[hyphenated])

        # Key not found
        raise KeyError(key)

    def __contains__(self, key: Any) -> bool:
        """
        Check if key exists in flattened data.

        Supports both Python-style (underscore) and API-style (hyphen) keys for dicts.
        For lists, checks if item is in the list.
        """
        if isinstance(self._flattened_data, list):
            return key in self._flattened_data

        if not isinstance(key, str):
            return False

        # Check direct key (hyphenated API name)
        if key in self._flattened_data:
            return True

        # Check converted key (Python name → API name)
        hyphenated = key.replace("_", "-")
        return hyphenated in self._flattened_data

    def __iter__(self) -> "Iterator[BaseModel | FortiAnalyzerObject | str]":
        """
        Iterate over response data.

        - If data is a list (e.g., device list), iterates over items as FortiAnalyzerObject instances
        - If data is a dict, iterates over keys

        Note: Items are always wrapped as FortiAnalyzerObject to provide consistent
        access to .raw, .dict, .json properties regardless of whether Pydantic models exist.
        """
        if isinstance(self._flattened_data, list):
            # Iterate over list items, always wrapping as FortiAnalyzerObject
            # This ensures consistent access to .raw, .dict, .json properties
            for item in self._flattened_data:
                # Always wrap in FortiAnalyzerObject for consistent interface
                yield self._wrap_value(item, use_pydantic=False)
        elif isinstance(self._flattened_data, dict):
            # Iterate over dict keys
            yield from self._flattened_data.keys()
        else:
            return iter([])

    def __len__(self) -> int:
        """
        Return length of data.

        - For dict responses: number of fields
        - For list responses: number of items
        """
        if isinstance(self._flattened_data, (dict, list)):
            return len(self._flattened_data)
        return 0

    def __repr__(self) -> str:
        """String representation."""
        status = f"api_status={self.api_status_code}"
        http = f"http_status={self.http_status_code}"
        return f"FortiAnalyzerResponse({status}, {http})"


class FortiAnalyzerObject:
    """
    Wrapper for nested dictionaries in FortiAnalyzer responses.

    Provides attribute access to dict fields with automatic
    conversion of hyphens to underscores.

    Examples:
        >>> obj = FortiAnalyzerObject({"server-hostname": "dns1.example.com"})
        >>> obj.server_hostname
        'dns1.example.com'
    """

    def __init__(self, data: dict[str, Any]):
        """
        Initialize object wrapper.

        Args:
            data: Dictionary to wrap
        """
        self._data = data

    def __getattr__(self, name: str) -> Any:
        """Attribute access with hyphen conversion."""
        # Convert underscore to hyphen for API field names
        api_field_name = name.replace("_", "-")

        # Try exact match first
        if name in self._data:
            value = self._data[name]
            return self._wrap_value(value)

        # Try with hyphen conversion
        if api_field_name in self._data:
            value = self._data[api_field_name]
            return self._wrap_value(value)

        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def _wrap_value(self, value: Any) -> Any:
        """Wrap nested structures."""
        if isinstance(value, dict):
            return FortiAnalyzerObject(value)
        elif isinstance(value, list):
            return FortiAnalyzerList(value)
        return value

    def __getitem__(self, key: str) -> Any:
        """Dictionary-style access."""
        return self._data[key]

    @property
    def dict(self) -> dict[str, Any]:
        """Get underlying dictionary."""
        return self._data.copy()

    @property
    def json(self) -> str:
        """Pretty-printed JSON string of data."""
        return json_module.dumps(self._data, indent=2)

    @property
    def raw(self) -> dict[str, Any]:
        """Get raw underlying dictionary."""
        return self._data

    def __repr__(self) -> str:
        """String representation."""
        return f"FortiAnalyzerObject({self._data})"


class FortiAnalyzerList(list[Any], Generic[_ObjectT]):
    """
    Wrapper for lists in FortiAnalyzer responses with typed iteration support.

    Automatically wraps dict items for attribute access and provides proper
    type hints for child table iteration.

    Examples:
        >>> lst = FortiAnalyzerList([{"name": "addr1"}, {"name": "addr2"}])
        >>> lst[0].name
        'addr1'
        >>>
        >>> # With typed child tables:
        >>> for match in group.match:  # match is properly typed
        ...     print(match.group_name)  # Full autocomplete support
    """

    def __init__(self, items: list[Any]):
        """
        Initialize list wrapper.

        Args:
            items: List to wrap
        """
        super().__init__(self._wrap_item(item) for item in items)

    def _wrap_item(self, item: Any) -> Any:
        """Wrap individual items."""
        if isinstance(item, dict):
            return FortiAnalyzerObject(item)
        elif isinstance(item, list):
            return FortiAnalyzerList(item)
        return item

    def __iter__(self) -> Iterator[_ObjectT]:  # type: ignore[override]
        """
        Iterate over wrapped items with proper type hints.

        Returns:
            Iterator yielding FortiAnalyzerObject instances (or typed subclasses)
        """
        return super().__iter__()


__all__ = [
    "FortiAnalyzerResponse",
    "FortiAnalyzerObject",
    "FortiAnalyzerList",
]

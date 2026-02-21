"""
FortiAnalyzer Response Models

Provides structured wrappers for FortiAnalyzer JSON-RPC API responses.
"""

from __future__ import annotations

import json as json_module
from typing import Any, Iterator


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
            "url": "/dvmdb/adom/root/...",
            "data": { ... actual data ... }
        }]
    }
    
    This class flattens the structure and provides:
    - HTTP layer properties (http_status_code, http_response_time, etc.)
    - API layer properties (api_status_code, api_status_message, api_id, api_raw)
    - Direct attribute access to data fields (conn_mode, device_id, name, etc.)
    
    Features:
    - Attribute access to flattened data: response.conn_mode, response.device_id
    - HTTP metadata: response.http_status_code, response.http_response_time
    - API metadata: response.api_status_code, response.api_status_message
    - Raw data access: response.raw, response.json, response.dict
    - Iteration support for list responses
    
    Examples:
        >>> # Get device configuration
        >>> result = faz.api.dvmdb.device.get(adom="root")
        >>>
        >>> # Direct attribute access to flattened data
        >>> result.conn_mode        # 'active'
        >>> result.device_id        # 123
        >>> result.name             # 'FortiGate-100D'
        >>>
        >>> # HTTP layer (transport)
        >>> result.http_status_code      # 200
        >>> result.http_response_time    # 45.2 (ms)
        >>>
        >>> # API layer (FortiAnalyzer response)
        >>> result.api_status_code       # 0 (success)
        >>> result.api_status_message    # 'OK'
        >>> result.api_id                # 1565
        >>> result.api_url               # '/dvmdb/adom/root/device'
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
        self._http_status_code = http_meta.get("status_code") or http_status_code
        self._response_time = http_meta.get("response_time") or (response_time * 1000 if response_time else None)
        
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
        self._flattened_data: dict[str, Any] = {}
        self._data_list: list[Any] | None = None  # Store list data for iteration
        
        if isinstance(data, dict):
            result = data.get("result", [])
            if isinstance(result, list) and len(result) > 0:
                first_result = result[0]
                if isinstance(first_result, dict):
                    # Extract the actual data
                    result_data = first_result.get("data", {})
                    if isinstance(result_data, dict):
                        self._flattened_data = result_data
                    elif isinstance(result_data, list):
                        # Data is a list - store for iteration support
                        self._data_list = result_data
                        # Also store in flattened for compatibility
                        self._flattened_data = first_result
                    else:
                        # If data is not a dict or list, store the whole first result
                        self._flattened_data = first_result
    
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
    def dict(self) -> dict[str, Any]:
        """Flattened data as dictionary."""
        return self._flattened_data.copy()
    
    @property
    def json(self) -> str:
        """Pretty-printed JSON string of flattened data."""
        return json_module.dumps(self._flattened_data, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a field value with optional default.
        
        Args:
            key: Field name
            default: Default value if field doesn't exist
        
        Returns:
            Field value or default
        """
        return self._flattened_data.get(key, default)
    
    # ========================================================================
    # Dynamic Attribute Access (Flattened Data)
    # ========================================================================
    
    def __getattr__(self, name: str) -> Any:
        """
        Provide attribute access to flattened data fields.
        
        This allows response.conn_mode instead of response['data']['conn-mode']
        
        Args:
            name: Attribute name
        
        Returns:
            Field value from flattened data
        
        Raises:
            AttributeError: If field doesn't exist
        """
        # Convert Python attribute name to API field name (underscore to hyphen)
        api_field_name = name.replace('_', '-')
        
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
    
    def _wrap_value(self, value: Any) -> Any:
        """
        Wrap dict/list values for cleaner access.
        
        Args:
            value: Value to potentially wrap
        
        Returns:
            Wrapped value or original value
        """
        if isinstance(value, dict):
            return FortiAnalyzerObject(value)
        elif isinstance(value, list):
            return FortiAnalyzerList(value)
        return value
    
    # ========================================================================
    # Container Protocol Support
    # ========================================================================
    
    def __getitem__(self, key: str) -> Any:
        """
        Dictionary-style access to flattened data.
        
        Supports both Python-style (underscore) and API-style (hyphen) keys.
        """
        # Try direct key first (hyphenated API name)
        if key in self._flattened_data:
            return self._wrap_value(self._flattened_data[key])
        
        # Try converting underscore to hyphen (Python name → API name)
        hyphenated = key.replace("_", "-")
        if hyphenated in self._flattened_data:
            return self._wrap_value(self._flattened_data[hyphenated])
        
        # Key not found
        raise KeyError(key)
    
    def __contains__(self, key: str) -> bool:
        """
        Check if key exists in flattened data.
        
        Supports both Python-style (underscore) and API-style (hyphen) keys.
        """
        # Check direct key (hyphenated API name)
        if key in self._flattened_data:
            return True
        
        # Check converted key (Python name → API name)
        hyphenated = key.replace("_", "-")
        return hyphenated in self._flattened_data
    
    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over response data.
        
        If the response contains a list (e.g., multiple devices), iterates over
        the list items as typed objects. Otherwise, iterates over dict keys.
        
        Examples:
            >>> # List response (multiple devices)
            >>> devices = faz.api.dvmdb.device.get(adom="root")
            >>> for device in devices:
            ...     print(device.conn_mode)  # Access device attributes
            
            >>> # Dict response (single object)
            >>> device = faz.api.dvmdb.device.get(adom="root", name="FGT-001")
            >>> for key in device:
            ...     print(key)  # Iterate over field names
        """
        # If data is a list, iterate over wrapped list items
        if self._data_list is not None:
            # Try to import and use typed model if available
            model_class = self._get_typed_model()
            if model_class:
                for item in self._data_list:
                    try:
                        yield model_class(**item)
                    except Exception:
                        # Fall back to dict wrapper if model validation fails
                        yield FortiAnalyzerObject(item) if isinstance(item, dict) else item
            else:
                # No typed model available, use dict wrapper
                for item in self._data_list:
                    if isinstance(item, dict):
                        yield FortiAnalyzerObject(item)
                    else:
                        yield item
        # Otherwise, iterate over dict keys
        elif isinstance(self._flattened_data, dict):
            yield from iter(self._flattened_data.keys())
        else:
            yield from iter([])
    
    def _get_typed_model(self) -> type | None:
        """
        Get the appropriate Pydantic model class for this response.
        
        Returns None if no typed model is available.
        """
        # Determine model from API URL
        api_url = self.api_url
        if not api_url:
            return None
        
        # Map URL patterns to model classes
        # Example: /dvmdb/adom/{adom}/device -> DeviceModel
        if '/dvmdb/' in api_url and '/device' in api_url:
            try:
                from hfortix_fortianalyzer.api.models.dvmdb.device import DeviceModel
                return DeviceModel
            except ImportError:
                pass
        
        # Add more mappings as models are generated
        
        return None
    
    def __len__(self) -> int:
        """Return number of fields in flattened data."""
        if isinstance(self._flattened_data, dict):
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
        >>> obj = FortiAnalyzerObject({"device-id": 123})
        >>> obj.device_id
        123
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
        api_field_name = name.replace('_', '-')
        
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
    
    def __repr__(self) -> str:
        """String representation."""
        return f"FortiAnalyzerObject({self._data})"


class FortiAnalyzerList(list):
    """
    Wrapper for lists in FortiAnalyzer responses.
    
    Automatically wraps dict items for attribute access.
    
    Examples:
        >>> lst = FortiAnalyzerList([{"name": "device1"}, {"name": "device2"}])
        >>> lst[0].name
        'device1'
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


__all__ = [
    "FortiAnalyzerResponse",
    "FortiAnalyzerObject",
    "FortiAnalyzerList",
]

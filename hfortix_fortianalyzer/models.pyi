"""Type stubs for FortiAnalyzer response models."""

from typing import Any, Iterator, Union

class FortiAnalyzerResponse:
    """Structured wrapper for FortiAnalyzer JSON-RPC API responses."""
    
    def __init__(
        self,
        data: dict[str, Any],
        http_status_code: int | None = None,
        response_time: float | None = None,
        request_info: dict[str, Any] | None = None,
    ) -> None: ...
    
    # ========================================================================
    # HTTP Layer Properties (Transport)
    # ========================================================================
    
    @property
    def http_status_code(self) -> int | None:
        """HTTP status code (200, 404, 500, etc.) from HTTPS connection."""
        ...
    
    @property
    def http_response_time(self) -> float | None:
        """Response time in milliseconds for the HTTP request."""
        ...
    
    @property
    def http_method(self) -> str | None:
        """HTTP method used (typically POST for JSON-RPC)."""
        ...
    
    @property
    def http_url(self) -> str | None:
        """Full HTTP URL that was requested."""
        ...
    
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
        ...
    
    @property
    def api_status_message(self) -> str | None:
        """FortiAnalyzer API status message ('OK' for success, error message otherwise)."""
        ...
    
    @property
    def api_id(self) -> int | None:
        """JSON-RPC request ID from the response."""
        ...
    
    @property
    def api_url(self) -> str | None:
        """FortiAnalyzer API URL path from the response."""
        ...
    
    @property
    def api_session(self) -> str | None:
        """Session token from login response."""
        ...
    
    @property
    def api_raw(self) -> dict[str, Any]:
        """Full raw FortiAnalyzer JSON-RPC response."""
        ...
    
    # ========================================================================
    # Data Access Methods
    # ========================================================================
    
    @property
    def raw(self) -> dict[str, Any]:
        """Full raw JSON-RPC response dictionary."""
        ...
    
    @property
    def dict(self) -> dict[str, Any]:
        """Flattened data as dictionary."""
        ...
    
    @property
    def json(self) -> str:
        """Pretty-printed JSON string of flattened data."""
        ...
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a field value with optional default."""
        ...
    
    # ========================================================================
    # Dynamic Attribute Access (Flattened Data)
    # ========================================================================
    # Note: __getattr__ is not defined in the stub file because specific
    # response classes define all attributes explicitly.
    # The base class implements __getattr__ at runtime for dynamic access.
    
    # ========================================================================
    # Container Protocol Support
    # ========================================================================
    
    def __getitem__(self, key: str) -> Any:
        """
        Dictionary-style access to flattened data.
        
        Supports both Python-style (underscore) and API-style (hyphen) keys.
        """
        ...
    
    def __contains__(self, key: str) -> bool:
        """
        Check if key exists in flattened data.
        
        Supports both Python-style (underscore) and API-style (hyphen) keys.
        """
        ...
    
    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over response data.
        
        If the response contains a list (e.g., multiple devices), iterates over
        the list items as typed Pydantic model instances (when available) or
        FortiAnalyzerObject wrappers. Otherwise, iterates over dict keys (str).
        
        For typed responses, each item will be a Pydantic model with full
        autocomplete and type checking for all fields.
        
        Examples:
            >>> # List response (multiple devices) - returns DvmdbDevice instances
            >>> devices = faz.api.dvmdb.device.get(adom="root")
            >>> for device in devices:
            ...     print(device.conn_mode)  # Fully typed attribute access
            
            >>> # Dict response (single object)
            >>> device = faz.api.dvmdb.device.get(adom="root", name="FGT-001")
            >>> for key in device:
            ...     print(key)  # Iterate over field names
        """
        ...
    
    def __len__(self) -> int:
        """Return number of fields in flattened data."""
        ...
    
    def __repr__(self) -> str:
        """String representation."""
        ...


class FortiAnalyzerObject:
    """
    Wrapper for nested dictionaries in FortiAnalyzer responses.
    
    Provides attribute-style access to nested objects with automatic
    wrapping of nested dictionaries and lists.
    """
    
    def __init__(self, data: dict[str, Any]) -> None: ...
    
    def __getattr__(self, name: str) -> Any:
        """
        Provide attribute access to nested data fields.
        
        Args:
            name: Attribute name (underscores converted to hyphens)
        
        Returns:
            Field value (wrapped if dict/list)
        
        Raises:
            AttributeError: If field doesn't exist
        """
        ...
    
    def __getitem__(self, key: str) -> Any:
        """Dictionary-style access."""
        ...
    
    def __repr__(self) -> str:
        """String representation."""
        ...


class FortiAnalyzerList(list[Any]):
    """
    Wrapper for lists in FortiAnalyzer responses.
    
    Automatically wraps nested dictionaries as FortiAnalyzerObject instances.
    """
    
    def __init__(self, items: list[Any]) -> None: ...


__all__ = [
    "FortiAnalyzerResponse",
    "FortiAnalyzerObject",
    "FortiAnalyzerList",
]

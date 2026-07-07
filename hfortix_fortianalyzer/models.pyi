"""Type stubs for FortiAnalyzer response models."""

from __future__ import annotations
from typing import Any, Iterator, Union, TypeVar, Generic, overload, SupportsIndex, TYPE_CHECKING

if TYPE_CHECKING:
    from pydantic import BaseModel

# TypeVar for generic typed list support
_ObjectT = TypeVar("_ObjectT", bound="FortiAnalyzerObject")
_ModelT = TypeVar("_ModelT", bound="BaseModel")

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
    def data(self) -> dict[str, Any] | list[Any]:
        """Access the raw flattened data (dict or list)."""
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
    
    def as_models(self) -> list[BaseModel] | BaseModel | None:
        """
        Parse response data as Pydantic models.
        
        Returns:
            - List of Pydantic models if response is a list
            - Single Pydantic model if response is a dict
            - None if no model is registered for this URL
        """
        ...
    
    # ========================================================================
    # Dynamic Attribute Access (Flattened Data)
    # ========================================================================
    # Note: __getattr__ is not defined in the stub file because specific
    # response classes (like SystemDnsResponse) define all attributes explicitly.
    # The base class implements __getattr__ at runtime for dynamic access.
    
    # ========================================================================
    # Container Protocol Support
    # ========================================================================
    
    @overload
    def __getitem__(self, key: str) -> Any: ...
    @overload
    def __getitem__(self, key: int) -> FortiAnalyzerObject: ...
    
    def __contains__(self, key: Any) -> bool:
        """
        Check if key exists in flattened data.
        
        Supports both Python-style (underscore) and API-style (hyphen) keys for dicts.
        For lists, checks if item is in the list.
        """
        ...
    
    def __iter__(self) -> Iterator[FortiAnalyzerObject]:
        """
        Iterate over response data.
        
        - If data is a list (e.g., device list), iterates over wrapped items
        - If data is a dict, iterates over keys (as strings)
        
        Note: Type hint shows FortiAnalyzerObject for list iteration use cases.
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
    
    @property
    def dict(self) -> dict[str, Any]:
        """Get underlying dictionary."""
        ...
    
    @property
    def json(self) -> str:
        """Pretty-printed JSON string of data."""
        ...
    
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw underlying dictionary."""
        ...
    
    def __repr__(self) -> str:
        """String representation."""
        ...


class FortiAnalyzerList(list[_ObjectT], Generic[_ObjectT]):
    """
    Wrapper for lists in FortiAnalyzer responses with typed iteration support.
    
    Automatically wraps nested dictionaries as FortiAnalyzerObject instances
    and provides proper type hints for child table iterations.
    
    The Generic pattern allows for properly typed iterations:
    ```python
    for match in group.match:  # match is properly typed as FortiAnalyzerObject
        print(match.group_name)  # Full autocomplete support
    ```
    """
    
    def __init__(self, items: list[Any]) -> None: ...
    
    # ========================================================================
    # Iterator and indexing support for proper type inference
    # ========================================================================
    
    def __iter__(self) -> Iterator[_ObjectT]:
        """Iterate over FortiAnalyzerObject items with full type safety."""
        ...
    
    @overload
    def __getitem__(self, index: SupportsIndex, /) -> _ObjectT: ...
    @overload
    def __getitem__(self, index: slice, /) -> list[_ObjectT]: ...


__all__ = [
    "FortiAnalyzerResponse",
    "FortiAnalyzerObject",
    "FortiAnalyzerList",
]

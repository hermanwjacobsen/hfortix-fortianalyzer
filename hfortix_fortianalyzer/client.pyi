"""FortiAnalyzer client - Type Stubs."""

from typing import Any, Optional
from hfortix_fortianalyzer.api import API
from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC

__all__ = ["FortiAnalyzer"]

class FortiAnalyzer:
    """FortiAnalyzer API client with type-safe endpoint access."""

    url: str
    client: HTTPClientJSONRPC
    api: API

    def __init__(
        self,
        url: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        api_key: Optional[str] = None,
        verify: bool = True,
        adom: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        adaptive_retry: bool = False,
        retry_strategy: str = "exponential",
        retry_jitter: bool = False,
        read_only: bool = False,
        audit_handler: Optional[Any] = None,
        audit_callback: Optional[Any] = None,
        user_context: Optional[dict[str, Any]] = None,
        rate_limit_calls_per_min: Optional[int] = None,
        rate_limit_calls_per_5min: Optional[int] = None,
        rate_limit_calls_per_hour: Optional[int] = None,
        rate_limit_errors_per_min: Optional[int] = None,
        rate_limit_errors_per_5min: Optional[int] = None,
        rate_limit_errors_per_hour: Optional[int] = None,
        rate_limit: bool = False,
        rate_limit_strategy: str = "queue",
        rate_limit_max_requests: int = 100,
        rate_limit_window_seconds: float = 60.0,
        rate_limit_queue_size: int = 100,
        rate_limit_queue_timeout: float = 30.0,
        rate_limit_queue_overflow: str = "block",
        circuit_breaker: bool = False,
        circuit_breaker_half_open_calls: int = 3,
        session_idle_timeout: float = 900.0,
    ) -> None:
        """Initialize FortiAnalyzer client."""
        ...

    def login(self) -> None:
        """Login to FortiAnalyzer (session-based auth only)."""
        ...

    def logout(self) -> None:
        """Logout from FortiAnalyzer (session-based auth only)."""
        ...

    def __enter__(self) -> FortiAnalyzer:
        """Context manager entry."""
        ...

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        ...

    def __repr__(self) -> str:
        """String representation."""
        ...

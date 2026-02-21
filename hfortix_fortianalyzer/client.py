"""FortiAnalyzer main client class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC

if TYPE_CHECKING:
    from hfortix_fortianalyzer.api import API

__all__ = ["FortiAnalyzer"]


class FortiAnalyzer:
    """
    FortiAnalyzer API client with type-safe endpoint access.
    
    This class provides a convenient interface to FortiAnalyzer APIs with
    generated endpoint classes that offer full type hints and IDE support.
    
    FortiAnalyzer uses the same JSON-RPC protocol as FortiManager, so we
    reuse the HTTPClientJSONRPC client from hfortix_core.
    
    Example:
        >>> from hfortix_fortianalyzer import FortiAnalyzer
        >>> faz = FortiAnalyzer(
        ...     url="https://fortianalyzer.example.com",
        ...     username="admin",
        ...     password="password"
        ... )
        >>> faz.login()
        >>> 
        >>> # Type-safe API navigation
        >>> result = faz.api.dvmdb.device.get(adom="root")
        >>> print(result.primary)  # Full type hints!
        >>> 
        >>> faz.logout()
    
    Attributes:
        client: The underlying HTTPClientJSONRPC instance
        api: Type-safe access to all API endpoints (API class instance)
    """
    
    api: "API"
    
    def __init__(
        self,
        url: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        api_key: Optional[str] = None,
        verify: bool = True,
        adom: Optional[str] = None,
        # Enterprise features (same as FortiOS)
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
    ):
        """
        Initialize FortiAnalyzer client.
        
        Args:
            url: FortiAnalyzer URL (e.g., "https://fortianalyzer.example.com")
            username: Username for session-based authentication
            password: Password for session-based authentication
            api_key: API key for token-based authentication (alternative to username/password)
            verify: Whether to verify SSL certificates
            adom: Default ADOM to use for operations
            max_retries: Maximum retry attempts on transient failures
            connect_timeout: Connection timeout in seconds
            read_timeout: Read timeout in seconds
            circuit_breaker_threshold: Failures before opening circuit
            circuit_breaker_timeout: Seconds before retrying after circuit opens
            max_connections: Maximum connection pool size
            max_keepalive_connections: Maximum keepalive connections
            adaptive_retry: Enable adaptive retry with backpressure detection
            retry_strategy: 'exponential' or 'linear' backoff
            retry_jitter: Add random jitter to retry delays
            read_only: Enable read-only mode (simulate writes without executing)
            audit_handler: Handler for audit logging (implements AuditHandler protocol)
            audit_callback: Custom callback function for audit logging
            user_context: Optional dict with user/application context for audit logs
            rate_limit_calls_per_min: Max calls per minute (monitoring only)
            rate_limit_calls_per_5min: Max calls per 5 minutes (monitoring only)
            rate_limit_calls_per_hour: Max calls per hour (monitoring only)
            rate_limit_errors_per_min: Max errors per minute (monitoring only)
            rate_limit_errors_per_5min: Max errors per 5 minutes (monitoring only)
            rate_limit_errors_per_hour: Max errors per hour (monitoring only)
            rate_limit: Enable rate limiting enforcement
            rate_limit_strategy: 'queue' or 'reject'
            rate_limit_max_requests: Max requests per window
            rate_limit_window_seconds: Time window in seconds
            rate_limit_queue_size: Max queue size
            rate_limit_queue_timeout: Max wait time in queue
            rate_limit_queue_overflow: 'block' or 'drop' on overflow
            circuit_breaker: Enable circuit breaker
            circuit_breaker_half_open_calls: Calls to test in half-open state
            session_idle_timeout: Session idle timeout in seconds (default: 900 = 15 min)
        """
        self.url = url
        self.client = HTTPClientJSONRPC(
            url=url,
            username=username,
            password=password,
            api_key=api_key,
            verify=verify,
            adom=adom,
            max_retries=max_retries,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            circuit_breaker_threshold=circuit_breaker_threshold,
            circuit_breaker_timeout=circuit_breaker_timeout,
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
            adaptive_retry=adaptive_retry,
            retry_strategy=retry_strategy,
            retry_jitter=retry_jitter,
            read_only=read_only,
            audit_handler=audit_handler,
            audit_callback=audit_callback,
            user_context=user_context,
            rate_limit_calls_per_min=rate_limit_calls_per_min,
            rate_limit_calls_per_5min=rate_limit_calls_per_5min,
            rate_limit_calls_per_hour=rate_limit_calls_per_hour,
            rate_limit_errors_per_min=rate_limit_errors_per_min,
            rate_limit_errors_per_5min=rate_limit_errors_per_5min,
            rate_limit_errors_per_hour=rate_limit_errors_per_hour,
            rate_limit=rate_limit,
            rate_limit_strategy=rate_limit_strategy,
            rate_limit_max_requests=rate_limit_max_requests,
            rate_limit_window_seconds=rate_limit_window_seconds,
            rate_limit_queue_size=rate_limit_queue_size,
            rate_limit_queue_timeout=rate_limit_queue_timeout,
            rate_limit_queue_overflow=rate_limit_queue_overflow,
            circuit_breaker=circuit_breaker,
            circuit_breaker_half_open_calls=circuit_breaker_half_open_calls,
            session_idle_timeout=session_idle_timeout,
        )
        
        # Initialize type-safe API navigation (class-based, like FortiOS)
        from hfortix_fortianalyzer.api import API
        self.api = API(self.client)
    
    def login(self) -> None:
        """Login to FortiAnalyzer (session-based auth only)."""
        self.client.login()
    
    def logout(self) -> None:
        """Logout from FortiAnalyzer (session-based auth only)."""
        self.client.logout()
    
    def __enter__(self) -> FortiAnalyzer:
        """Context manager entry."""
        self.login()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.logout()
    
    def __repr__(self) -> str:
        """String representation."""
        return f"FortiAnalyzer(url={self.url!r})"

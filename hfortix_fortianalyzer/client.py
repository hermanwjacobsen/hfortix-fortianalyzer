"""FortiAnalyzer main client class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC

if TYPE_CHECKING:
    from hfortix_fortianalyzer.api import API


class FortiAnalyzer:
    """
    FortiAnalyzer API client with type-safe endpoint access.

    This class provides a convenient interface to FortiAnalyzer APIs with
    generated endpoint classes that offer full type hints and IDE support.

    Example:
        >>> from hfortix_fortianalyzer import FortiAnalyzer
        >>> faz = FortiAnalyzer(
        ...     host="faz.example.com",
        ...     username="admin",
        ...     password="password"
        ... )
        >>> faz.login()
        >>>
        >>> # Access endpoints through the api attribute
        >>> devices = faz.api.dvmdb.adom.device.get(adom="root")
        >>> alerts = faz.api.eventmgmt.adom.alerts.get(adom="root")
        >>>
        >>> faz.logout()

    Attributes:
        client: The underlying HTTPClientJSONRPC instance
        api: Access to all generated API endpoints
    """

    api: "API"

    def __init__(
        self,
        host: str,
        username: str | None = None,
        password: str | None = None,
        api_key: str | None = None,
        api_user: str | None = None,
        port: int | None = None,
        verify: bool = True,
        adom: str | None = None,
    ):
        """
        Initialize FortiAnalyzer client.

        Args:
            host: FortiAnalyzer hostname or URL. All of these are equivalent:
                ``"faz.example.com"``, ``"https://faz.example.com"``,
                ``"https://faz.example.com/jsonrpc"``.
                Use ``http://`` prefix for plain HTTP. Recommended form: bare hostname.
            username: Username for session-based authentication
            password: Password for session-based authentication
            api_key: API key for token-based authentication (alternative to username/password)
            api_user: API username for the access_user header (FAZ 7.6.6+, optional).
                Helps FortiAnalyzer resolve the correct API user on the first request
                when multiple API users share a key pool.
            port: Override the TCP port (e.g. ``8443``). If omitted, the port embedded
                in the host is used, or the scheme default (443 for https, 80 for http).
            verify: Whether to verify SSL certificates
            adom: Default ADOM to use for operations
        """
        self.host = host
        self.client = HTTPClientJSONRPC(
            url=host,
            username=username,
            password=password,
            api_key=api_key,
            api_user=api_user,
            port=port,
            verify=verify,
            adom=adom,
        )

        # Import api module and create API instance
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
        return f"FortiAnalyzer(host={self.host!r})"

"""Type stubs for cli.global.system.log-fetch.server-settings"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogFetchServerSettingsGetItem:
    """Item yielded when iterating over CliGlobalSystemLogFetchServerSettingsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def max_conn_per_session(self) -> int: ...
    @property
    def max_sessions(self) -> int: ...
    @property
    def session_timeout(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogFetchServerSettingsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogFetchServerSettingsGet endpoint with autocomplete support."""

    # ========================================================================
    # HTTP Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def http_status_code(self) -> int | None: ...
    @property
    def http_response_time(self) -> float | None: ...
    @property
    def http_method(self) -> str | None: ...
    @property
    def http_url(self) -> str | None: ...

    # ========================================================================
    # API Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def api_status_code(self) -> int | None: ...
    @property
    def api_status_message(self) -> str | None: ...
    @property
    def api_id(self) -> int | None: ...
    @property
    def api_url(self) -> str | None: ...
    @property
    def api_raw(self) -> dict[str, Any]: ...

    # ========================================================================
    # Data Fields (specific to this endpoint)
    # ========================================================================
    @property
    def oid(self) -> int | None:
        """Object ID (dynamically added by FortiAnalyzer API, not in Swagger schema)"""
        ...

    @property
    def max_conn_per_session(self) -> int | None:
        """Field: max-conn-per-session"""
        ...

    @property
    def max_sessions(self) -> int | None:
        """Field: max-sessions"""
        ...

    @property
    def session_timeout(self) -> int | None:
        """Field: session-timeout"""
        ...


    # Inherited methods from FortiAnalyzerResponse
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[CliGlobalSystemLogFetchServerSettingsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogFetchServerSettings:
    """FortiAnalyzer endpoint: cli.global.system.log-fetch.server-settings"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogFetchServerSettingsGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        max_conn_per_session: int | None = None,
        max_sessions: int | None = None,
        session_timeout: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        max_conn_per_session: int | None = None,
        max_sessions: int | None = None,
        session_timeout: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogFetchServerSettings", "CliGlobalSystemLogFetchServerSettingsGetResponse"]
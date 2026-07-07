"""Type stubs for cli.global.fmupdate.av-ips.advanced-log"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateAvIpsAdvancedLogGetItem:
    """Item yielded when iterating over CliGlobalFmupdateAvIpsAdvancedLogGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def log_fortigate(self) -> Literal["disable", "enable"]: ...
    @property
    def log_server(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalFmupdateAvIpsAdvancedLogGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateAvIpsAdvancedLogGet endpoint with autocomplete support."""

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
    def log_fortigate(self) -> Literal["disable", "enable"] | None:
        """Field: log-fortigate"""
        ...

    @property
    def log_server(self) -> Literal["disable", "enable"] | None:
        """Field: log-server"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateAvIpsAdvancedLogGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateAvIpsAdvancedLog:
    """FortiAnalyzer endpoint: cli.global.fmupdate.av-ips.advanced-log"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateAvIpsAdvancedLogGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        log_fortigate: Literal["disable", "enable"] | None = None,
        log_server: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        log_fortigate: Literal["disable", "enable"] | None = None,
        log_server: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateAvIpsAdvancedLog", "CliGlobalFmupdateAvIpsAdvancedLogGetResponse"]
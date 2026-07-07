"""Type stubs for cli.global.system.report.auto-cache"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemReportAutoCacheGetItem:
    """Item yielded when iterating over CliGlobalSystemReportAutoCacheGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def aggressive_schedule(self) -> Literal["disable", "enable"]: ...
    @property
    def order(self) -> Literal["oldest-first"]: ...
    @property
    def sche_rpt_only(self) -> Literal["disable", "enable"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemReportAutoCacheGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemReportAutoCacheGet endpoint with autocomplete support."""

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
    def aggressive_schedule(self) -> Literal["disable", "enable"] | None:
        """Field: aggressive-schedule"""
        ...

    @property
    def order(self) -> Literal["oldest-first"] | None:
        """Field: order"""
        ...

    @property
    def sche_rpt_only(self) -> Literal["disable", "enable"] | None:
        """Field: sche-rpt-only"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemReportAutoCacheGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemReportAutoCache:
    """FortiAnalyzer endpoint: cli.global.system.report.auto-cache"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemReportAutoCacheGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        aggressive_schedule: Literal["disable", "enable"] | None = None,
        order: Literal["oldest-first"] | None = None,
        sche_rpt_only: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        aggressive_schedule: Literal["disable", "enable"] | None = None,
        order: Literal["oldest-first"] | None = None,
        sche_rpt_only: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemReportAutoCache", "CliGlobalSystemReportAutoCacheGetResponse"]
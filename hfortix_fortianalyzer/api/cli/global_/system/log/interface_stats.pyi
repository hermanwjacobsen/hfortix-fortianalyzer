"""Type stubs for cli.global.system.log.interface-stats"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogInterfaceStatsGetItem:
    """Item yielded when iterating over CliGlobalSystemLogInterfaceStatsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def billing_report(self) -> Literal["disable", "enable"]: ...
    @property
    def retention_days(self) -> int: ...
    @property
    def sampling_interval(self) -> int: ...
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


class CliGlobalSystemLogInterfaceStatsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogInterfaceStatsGet endpoint with autocomplete support."""

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
    def billing_report(self) -> Literal["disable", "enable"] | None:
        """Field: billing-report"""
        ...

    @property
    def retention_days(self) -> int | None:
        """Field: retention-days"""
        ...

    @property
    def sampling_interval(self) -> int | None:
        """Field: sampling-interval"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogInterfaceStatsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogInterfaceStats:
    """FortiAnalyzer endpoint: cli.global.system.log.interface-stats"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogInterfaceStatsGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        billing_report: Literal["disable", "enable"] | None = None,
        retention_days: int | None = None,
        sampling_interval: int | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        billing_report: Literal["disable", "enable"] | None = None,
        retention_days: int | None = None,
        sampling_interval: int | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogInterfaceStats", "CliGlobalSystemLogInterfaceStatsGetResponse"]
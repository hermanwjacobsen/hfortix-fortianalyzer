"""Type stubs for cli.global.system.report.group.chart-alternative"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemReportGroupChartAlternativeGetItem:
    """Item yielded when iterating over CliGlobalSystemReportGroupChartAlternativeGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def chart_name(self) -> str: ...
    @property
    def chart_replace(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemReportGroupChartAlternativeGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemReportGroupChartAlternativeGet endpoint with autocomplete support."""

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
    def chart_name(self) -> str | None:
        """Field: chart-name"""
        ...

    @property
    def chart_replace(self) -> str | None:
        """Field: chart-replace"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemReportGroupChartAlternativeGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemReportGroupChartAlternative:
    """FortiAnalyzer endpoint: cli.global.system.report.group.chart-alternative"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        group: str,
        chart_alternative: int | str | None = None,
        fields: list[Literal["chart-name", "chart-replace"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemReportGroupChartAlternativeGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        group: str,
        chart_alternative: int | str | None = None,
        chart_name: str | None = None,
        chart_replace: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        group: str,
        chart_alternative: int | str | None = None,
        chart_name: str | None = None,
        chart_replace: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        group: str,
        chart_alternative: int | str | None = None,
        chart_name: str | None = None,
        chart_replace: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        group: str,
        chart_alternative: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemReportGroupChartAlternative", "CliGlobalSystemReportGroupChartAlternativeGetResponse"]
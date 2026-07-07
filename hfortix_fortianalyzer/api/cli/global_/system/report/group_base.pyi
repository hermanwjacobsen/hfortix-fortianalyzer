"""Type stubs for cli.global.system.report.group"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemReportGroupGetItem:
    """Item yielded when iterating over CliGlobalSystemReportGroupGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def adom(self) -> str: ...
    @property
    def case_insensitive(self) -> Literal["disable", "enable"]: ...
    @property
    def chart_alternative(self) -> list[ChartAlternativeItem]: ...
    @property
    def group_by(self) -> list[GroupByItem]: ...
    @property
    def group_id(self) -> int: ...
    @property
    def report_like(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class ChartAlternativeItem:
    """Nested item type for chart-alternative array."""

    @property
    def chart_name(self) -> str: ...
    @property
    def chart_replace(self) -> str: ...

class GroupByItem:
    """Nested item type for group-by array."""

    @property
    def var_expression(self) -> str: ...
    @property
    def var_name(self) -> str: ...
    @property
    def var_type(self) -> Literal["integer", "string", "enum", "ip"]: ...


class CliGlobalSystemReportGroupGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemReportGroupGet endpoint with autocomplete support."""

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
    def adom(self) -> str | None:
        """Field: adom"""
        ...

    @property
    def case_insensitive(self) -> Literal["disable", "enable"] | None:
        """Field: case-insensitive"""
        ...

    @property
    def chart_alternative(self) -> list[ChartAlternativeItem]:
        """Field: chart-alternative"""
        ...

    @property
    def group_by(self) -> list[GroupByItem]:
        """Field: group-by"""
        ...

    @property
    def group_id(self) -> int | None:
        """Field: group-id"""
        ...

    @property
    def report_like(self) -> str | None:
        """Field: report-like"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemReportGroupGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemReportGroup:
    """FortiAnalyzer endpoint: cli.global.system.report.group"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        group: int | str | None = None,
        fields: list[Literal["adom", "case-insensitive", "group-id", "report-like"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemReportGroupGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        group: int | str | None = None,
        adom: str | None = None,
        case_insensitive: Literal["disable", "enable"] | None = None,
        chart_alternative: list[dict[str, Any]] | None = None,
        group_by: list[dict[str, Any]] | None = None,
        group_id: int | None = None,
        report_like: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        group: int | str | None = None,
        adom: str | None = None,
        case_insensitive: Literal["disable", "enable"] | None = None,
        chart_alternative: list[dict[str, Any]] | None = None,
        group_by: list[dict[str, Any]] | None = None,
        group_id: int | None = None,
        report_like: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        group: int | str | None = None,
        adom: str | None = None,
        case_insensitive: Literal["disable", "enable"] | None = None,
        chart_alternative: list[dict[str, Any]] | None = None,
        group_by: list[dict[str, Any]] | None = None,
        group_id: int | None = None,
        report_like: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        group: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemReportGroup", "CliGlobalSystemReportGroupGetResponse"]
"""Type stubs for cli.global.system.report.group.group-by"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemReportGroupGroupByGetItem:
    """Item yielded when iterating over CliGlobalSystemReportGroupGroupByGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def var_expression(self) -> str: ...
    @property
    def var_name(self) -> str: ...
    @property
    def var_type(self) -> Literal["integer", "string", "enum", "ip"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemReportGroupGroupByGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemReportGroupGroupByGet endpoint with autocomplete support."""

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
    def var_expression(self) -> str | None:
        """Field: var-expression"""
        ...

    @property
    def var_name(self) -> str | None:
        """Field: var-name"""
        ...

    @property
    def var_type(self) -> Literal["integer", "string", "enum", "ip"] | None:
        """Field: var-type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemReportGroupGroupByGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemReportGroupGroupBy:
    """FortiAnalyzer endpoint: cli.global.system.report.group.group-by"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        group: str,
        group_by: int | str | None = None,
        fields: list[Literal["var-expression", "var-name", "var-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemReportGroupGroupByGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        group: str,
        group_by: int | str | None = None,
        var_expression: str | None = None,
        var_name: str | None = None,
        var_type: Literal["integer", "string", "enum", "ip"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        group: str,
        group_by: int | str | None = None,
        var_expression: str | None = None,
        var_name: str | None = None,
        var_type: Literal["integer", "string", "enum", "ip"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        group: str,
        group_by: int | str | None = None,
        var_expression: str | None = None,
        var_name: str | None = None,
        var_type: Literal["integer", "string", "enum", "ip"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        group: str,
        group_by: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemReportGroupGroupBy", "CliGlobalSystemReportGroupGroupByGetResponse"]
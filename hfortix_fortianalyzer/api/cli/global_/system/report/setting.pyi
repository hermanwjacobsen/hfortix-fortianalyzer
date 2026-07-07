"""Type stubs for cli.global.system.report.setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemReportSettingGetItem:
    """Item yielded when iterating over CliGlobalSystemReportSettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def aggregate_report(self) -> Literal["disable", "enable"]: ...
    @property
    def capwap_port(self) -> int: ...
    @property
    def capwap_service(self) -> str: ...
    @property
    def exclude_capwap(self) -> Literal["disable", "by-port", "by-service"]: ...
    @property
    def hcache_lossless(self) -> Literal["disable", "enable"]: ...
    @property
    def ldap_cache_timeout(self) -> int: ...
    @property
    def max_rpt_pdf_rows(self) -> int: ...
    @property
    def max_table_rows(self) -> int: ...
    @property
    def report_priority(self) -> Literal["high", "low", "auto"]: ...
    @property
    def template_auto_install(self) -> Literal["default", "english"]: ...
    @property
    def week_start(self) -> Literal["sun", "mon"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemReportSettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemReportSettingGet endpoint with autocomplete support."""

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
    def aggregate_report(self) -> Literal["disable", "enable"] | None:
        """Field: aggregate-report"""
        ...

    @property
    def capwap_port(self) -> int | None:
        """Field: capwap-port"""
        ...

    @property
    def capwap_service(self) -> str | None:
        """Field: capwap-service"""
        ...

    @property
    def exclude_capwap(self) -> Literal["disable", "by-port", "by-service"] | None:
        """Field: exclude-capwap"""
        ...

    @property
    def hcache_lossless(self) -> Literal["disable", "enable"] | None:
        """Field: hcache-lossless"""
        ...

    @property
    def ldap_cache_timeout(self) -> int | None:
        """Field: ldap-cache-timeout"""
        ...

    @property
    def max_rpt_pdf_rows(self) -> int | None:
        """Field: max-rpt-pdf-rows"""
        ...

    @property
    def max_table_rows(self) -> int | None:
        """Field: max-table-rows"""
        ...

    @property
    def report_priority(self) -> Literal["high", "low", "auto"] | None:
        """Field: report-priority"""
        ...

    @property
    def template_auto_install(self) -> Literal["default", "english"] | None:
        """Field: template-auto-install"""
        ...

    @property
    def week_start(self) -> Literal["sun", "mon"] | None:
        """Field: week-start"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemReportSettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemReportSetting:
    """FortiAnalyzer endpoint: cli.global.system.report.setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemReportSettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        aggregate_report: Literal["disable", "enable"] | None = None,
        capwap_port: int | None = None,
        capwap_service: str | None = None,
        exclude_capwap: Literal["disable", "by-port", "by-service"] | None = None,
        hcache_lossless: Literal["disable", "enable"] | None = None,
        ldap_cache_timeout: int | None = None,
        max_rpt_pdf_rows: int | None = None,
        max_table_rows: int | None = None,
        report_priority: Literal["high", "low", "auto"] | None = None,
        template_auto_install: Literal["default", "english"] | None = None,
        week_start: Literal["sun", "mon"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        aggregate_report: Literal["disable", "enable"] | None = None,
        capwap_port: int | None = None,
        capwap_service: str | None = None,
        exclude_capwap: Literal["disable", "by-port", "by-service"] | None = None,
        hcache_lossless: Literal["disable", "enable"] | None = None,
        ldap_cache_timeout: int | None = None,
        max_rpt_pdf_rows: int | None = None,
        max_table_rows: int | None = None,
        report_priority: Literal["high", "low", "auto"] | None = None,
        template_auto_install: Literal["default", "english"] | None = None,
        week_start: Literal["sun", "mon"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemReportSetting", "CliGlobalSystemReportSettingGetResponse"]
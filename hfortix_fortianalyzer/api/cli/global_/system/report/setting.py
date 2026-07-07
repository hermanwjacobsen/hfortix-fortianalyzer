"""
FortiAnalyzer API endpoint: cli.global.system.report.setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemReportSetting:
    """
    FortiAnalyzer endpoint: cli.global.system.report.setting
    
    
    Available methods: get, set, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/report/setting"
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        aggregate_report: Literal["disable", "enable"] | None = None,
        capwap_port: int | None = None,
        exclude_capwap: Literal["disable", "by-port", "by-service"] | None = None,
        hcache_lossless: Literal["disable", "enable"] | None = None,
        ldap_cache_timeout: int | None = None,
        max_rpt_pdf_rows: int | None = None,
        max_table_rows: int | None = None,
        report_priority: Literal["high", "low", "auto"] | None = None,
        template_auto_install: Literal["default", "english"] | None = None,
        week_start: Literal["sun", "mon"] | None = None,
        capwap_service: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            aggregate_report: aggregate-report parameter
            capwap_port: capwap-port parameter
            capwap_service: capwap-service parameter
            exclude_capwap: exclude-capwap parameter
            hcache_lossless: hcache-lossless parameter
            ldap_cache_timeout: ldap-cache-timeout parameter
            max_rpt_pdf_rows: max-rpt-pdf-rows parameter
            max_table_rows: max-table-rows parameter
            report_priority: report-priority parameter
            template_auto_install: template-auto-install parameter
            ... (1 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/report/setting"
        
        # Build data payload
        data = {}
        if aggregate_report is not None:
            data["aggregate-report"] = aggregate_report
        if capwap_port is not None:
            data["capwap-port"] = capwap_port
        if capwap_service is not None:
            data["capwap-service"] = capwap_service
        if exclude_capwap is not None:
            data["exclude-capwap"] = exclude_capwap
        if hcache_lossless is not None:
            data["hcache-lossless"] = hcache_lossless
        if ldap_cache_timeout is not None:
            data["ldap-cache-timeout"] = ldap_cache_timeout
        if max_rpt_pdf_rows is not None:
            data["max-rpt-pdf-rows"] = max_rpt_pdf_rows
        if max_table_rows is not None:
            data["max-table-rows"] = max_table_rows
        if report_priority is not None:
            data["report-priority"] = report_priority
        if template_auto_install is not None:
            data["template-auto-install"] = template_auto_install
        if week_start is not None:
            data["week-start"] = week_start
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def update(
        self,
        aggregate_report: Literal["disable", "enable"] | None = None,
        capwap_port: int | None = None,
        exclude_capwap: Literal["disable", "by-port", "by-service"] | None = None,
        hcache_lossless: Literal["disable", "enable"] | None = None,
        ldap_cache_timeout: int | None = None,
        max_rpt_pdf_rows: int | None = None,
        max_table_rows: int | None = None,
        report_priority: Literal["high", "low", "auto"] | None = None,
        template_auto_install: Literal["default", "english"] | None = None,
        week_start: Literal["sun", "mon"] | None = None,
        capwap_service: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            aggregate_report: aggregate-report parameter
            capwap_port: capwap-port parameter
            capwap_service: capwap-service parameter
            exclude_capwap: exclude-capwap parameter
            hcache_lossless: hcache-lossless parameter
            ldap_cache_timeout: ldap-cache-timeout parameter
            max_rpt_pdf_rows: max-rpt-pdf-rows parameter
            max_table_rows: max-table-rows parameter
            report_priority: report-priority parameter
            template_auto_install: template-auto-install parameter
            ... (1 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/report/setting"
        
        # Build data payload
        data = {}
        if aggregate_report is not None:
            data["aggregate-report"] = aggregate_report
        if capwap_port is not None:
            data["capwap-port"] = capwap_port
        if capwap_service is not None:
            data["capwap-service"] = capwap_service
        if exclude_capwap is not None:
            data["exclude-capwap"] = exclude_capwap
        if hcache_lossless is not None:
            data["hcache-lossless"] = hcache_lossless
        if ldap_cache_timeout is not None:
            data["ldap-cache-timeout"] = ldap_cache_timeout
        if max_rpt_pdf_rows is not None:
            data["max-rpt-pdf-rows"] = max_rpt_pdf_rows
        if max_table_rows is not None:
            data["max-table-rows"] = max_table_rows
        if report_priority is not None:
            data["report-priority"] = report_priority
        if template_auto_install is not None:
            data["template-auto-install"] = template_auto_install
        if week_start is not None:
            data["week-start"] = week_start
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

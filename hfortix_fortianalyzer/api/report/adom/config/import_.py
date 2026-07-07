"""
FortiAnalyzer API endpoint: report.adom.config.import

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomConfigImport:
    """
    FortiAnalyzer endpoint: report.adom.config.import
    
    Request of importing report config files.
    
    Available methods: add
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def add(
        self,
        adom: str,
        data: str,
        adoms: list[str] | None = None,
        apiver: int = 3,
        check_only: bool | None = None,
        conflict_option: Literal["skip", "replace", "fail"] | None = None,
        report_folder: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Request of importing report config files.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/config/import"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "data": data
        }]
        if adoms is not None:
            params[0]["adoms"] = adoms
        if apiver is not None:
            params[0]["apiver"] = apiver
        if check_only is not None:
            params[0]["check-only"] = check_only
        if conflict_option is not None:
            params[0]["conflict-option"] = conflict_option
        if report_folder is not None:
            params[0]["report-folder"] = report_folder
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

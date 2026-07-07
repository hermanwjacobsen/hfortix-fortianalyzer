"""
FortiAnalyzer API endpoint: report.template.import

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportTemplateImport:
    """
    FortiAnalyzer endpoint: report.template.import
    
    Request of importing report templates.
    
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
        data: str,
        dev_type: str,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Request of importing report templates.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/template/import"
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "data": data,
            "dev-type": dev_type
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

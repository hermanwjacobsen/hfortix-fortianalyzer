"""
FortiAnalyzer API endpoint: report.template.delete

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportTemplateDelete:
    """
    FortiAnalyzer endpoint: report.template.delete
    
    Request of deleting language sepcified report templates file.
    
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
        dev_type: str,
        language: str,
        apiver: int = 3,
        title: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Request of deleting language sepcified report templates file.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/template/delete"
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "dev-type": dev_type,
            "language": language
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if title is not None:
            params[0]["title"] = title
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

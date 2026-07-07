"""
FortiAnalyzer API endpoint: report.adom.template.install

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomTemplateInstall:
    """
    FortiAnalyzer endpoint: report.adom.template.install
    
    Request of installing language sepcified report templates from file.
    
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
        language: str,
        apiver: int = 3,
        data: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Request of installing language sepcified report templates from file.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/template/install"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "language": language
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if data is not None:
            params[0]["data"] = data
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

"""
FortiAnalyzer API endpoint: report.adom.graph-file.data

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomGraphFileData:
    """
    FortiAnalyzer endpoint: report.adom.graph-file.data
    
    Request to download a graph file.
    
    Available methods: get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(
        self,
        adom: str,
        file_name: str,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Request to download a graph file.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            file_name: Graph file name.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/graph-file/data"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if file_name is not None:
            request_params["file-name"] = file_name
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            **request_params
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

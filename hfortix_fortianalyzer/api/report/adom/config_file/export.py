"""
FortiAnalyzer API endpoint: report.adom.config-file.export

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomConfigFileExport:
    """
    FortiAnalyzer endpoint: report.adom.config-file.export
    
    Request of exporting report config files.
    
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
        apiver: int = 3,
        layout_id: float | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Request of exporting report config files.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            layout_id: ID of the exported layout.
            name: Title of the exported layout.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/config-file/export"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if layout_id is not None:
            request_params["layout-id"] = layout_id
        if name is not None:
            request_params["name"] = name
        
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

"""
FortiAnalyzer API endpoint: fazsys.adom.storage-info-history

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysAdomStorageInfoHistory:
    """
    FortiAnalyzer endpoint: fazsys.adom.storage-info-history
    
    Get Storage Info History.
    
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
        time_range: dict[str, Any],
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get Storage Info History.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            time_range: Time range for source data selection.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/fazsys/adom/{adom}/storage-info-history"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if time_range is not None:
            request_params["time-range"] = time_range
        
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

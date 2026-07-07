"""
FortiAnalyzer API endpoint: soar.adom.indicator.unblock

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomIndicatorUnblock:
    """
    FortiAnalyzer endpoint: soar.adom.indicator.unblock
    
    Unblock Indicator
    
    Available methods: execute
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def execute(
        self,
        adom: str,
        indicator_uuid: list[str],
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        EXECUTE operation.
        
        Unblock Indicator
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/indicator/unblock"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "indicator-uuid": indicator_uuid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        
        response = self._client.execute(
            method="execute",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

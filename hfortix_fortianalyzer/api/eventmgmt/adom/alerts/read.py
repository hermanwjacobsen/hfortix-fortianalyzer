"""
FortiAnalyzer API endpoint: eventmgmt.adom.alerts.read

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertsRead:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.alerts.read
    
    Mark a specific alert event as read.
    
    Available methods: update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def update(
        self,
        adom: str,
        alertid: list[str],
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Mark a specific alert event as read.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/alerts/read"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "alertid": alertid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

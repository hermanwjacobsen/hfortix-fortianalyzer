"""
FortiAnalyzer API endpoint: eventmgmt.adom.alerts.extra-details

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertsExtraDetails:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.alerts.extra-details
    
    List alert extra details information.
    
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
        alertids: list[str],
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        List alert extra details information.
        
        Args:
            adom: adom path parameter.
            alertids: Alert IDs.
            apiver: Current API version.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/alerts/extra-details"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        if alertids is not None:
            request_params["alertids"] = alertids
        request_params["apiver"] = apiver
        
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

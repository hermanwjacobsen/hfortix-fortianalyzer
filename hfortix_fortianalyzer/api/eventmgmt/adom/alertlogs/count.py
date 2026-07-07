"""
FortiAnalyzer API endpoint: eventmgmt.adom.alertlogs.count

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertlogsCount:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.alertlogs.count
    
    Get logs count for a specific event alert.
    
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
        alertid: list[str],
        apiver: int = 3,
        rulename: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get logs count for a specific event alert.
        
        Args:
            adom: adom path parameter.
            alertid: Alert IDs.
            apiver: Current API version.
            rulename: The rule name of the rule configured in correlated typed handler.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/alertlogs/count"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        if alertid is not None:
            request_params["alertid"] = alertid
        request_params["apiver"] = apiver
        if rulename is not None:
            request_params["rulename"] = rulename
        
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

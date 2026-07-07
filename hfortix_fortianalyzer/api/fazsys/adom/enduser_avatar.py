"""
FortiAnalyzer API endpoint: fazsys.adom.enduser-avatar

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysAdomEnduserAvatar:
    """
    FortiAnalyzer endpoint: fazsys.adom.enduser-avatar
    
    Get Enduser Avatar.
    
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
        user: list[dict[str, Any]],
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get Enduser Avatar.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            user: A structure that hold the users info. One user is identified by ('epid' and 'euid') or ('name' and 'fctuid')
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/fazsys/adom/{adom}/enduser-avatar"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if user is not None:
            request_params["user"] = user
        
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

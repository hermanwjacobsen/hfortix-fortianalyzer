"""
FortiAnalyzer API endpoint: ioc.license.state

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IocLicenseState:
    """
    FortiAnalyzer endpoint: ioc.license.state
    
    Get IOC license state.
    
    Available methods: get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self, apiver: int = 3) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get IOC license state.
        
        Args:
            apiver: Current API version.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/ioc/license/state"
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
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

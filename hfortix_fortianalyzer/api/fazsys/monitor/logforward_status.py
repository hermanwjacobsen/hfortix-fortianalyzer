"""
FortiAnalyzer API endpoint: fazsys.monitor.logforward-status

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysMonitorLogforwardStatus:
    """
    FortiAnalyzer endpoint: fazsys.monitor.logforward-status
    
    Get Log Forwarding Server Status.
    
    Available methods: get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self, apiver: int = 3, id: list[float] | None = None) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get Log Forwarding Server Status.
        
        Args:
            apiver: Current API version.
            id: An array of the log forwarding server ID. If the ID array is empty or omitted, status of all log forwarding servers will be returned.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/fazsys/monitor/logforward-status"
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if id is not None:
            request_params["id"] = id
        
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

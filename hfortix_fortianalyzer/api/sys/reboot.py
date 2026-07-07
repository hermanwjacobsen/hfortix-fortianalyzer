"""
FortiAnalyzer API endpoint: sys.reboot

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysReboot:
    """
    FortiAnalyzer endpoint: sys.reboot
    
    
    Available methods: exec
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def exec(self, message: str | None = None) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            message: Optional message to be stored in event log.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/sys/reboot"
        
        # Build data payload
        data = {}
        if message is not None:
            data["message"] = message
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="exec",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

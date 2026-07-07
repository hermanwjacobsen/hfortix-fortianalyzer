"""
FortiAnalyzer API endpoint: sys.login.user

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysLoginUser:
    """
    FortiAnalyzer endpoint: sys.login.user
    
    
    Available methods: exec
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def exec(self, passwd: str | None = None, user: str | None = None) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            passwd: passwd parameter
            user: user parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/sys/login/user"
        
        # Build data payload
        data = {}
        if passwd is not None:
            data["passwd"] = passwd
        if user is not None:
            data["user"] = user
        
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

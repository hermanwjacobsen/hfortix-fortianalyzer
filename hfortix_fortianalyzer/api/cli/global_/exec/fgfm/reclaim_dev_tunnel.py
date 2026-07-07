"""
FortiAnalyzer API endpoint: cli.global.exec.fgfm.reclaim-dev-tunnel

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalExecFgfmReclaimDevTunnel:
    """
    FortiAnalyzer endpoint: cli.global.exec.fgfm.reclaim-dev-tunnel
    
    
    Available methods: exec
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def exec(self, flags: list[Any] | None = None) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            flags: flags parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/exec/fgfm/reclaim-dev-tunnel"
        
        # Build data payload
        data = {}
        if flags is not None:
            data["flags"] = flags
        
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

"""
FortiAnalyzer API endpoint: sys.generate.wsdl

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysGenerateWsdl:
    """
    FortiAnalyzer endpoint: sys.generate.wsdl
    
    
    Available methods: exec
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def exec(self, endpoint: str | None = None, target: str | None = None) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            endpoint: endpoint parameter
            target: URL to the module, ADOM, and object.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/sys/generate/wsdl"
        
        # Build data payload
        data = {}
        if endpoint is not None:
            data["endpoint"] = endpoint
        if target is not None:
            data["target"] = target
        
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

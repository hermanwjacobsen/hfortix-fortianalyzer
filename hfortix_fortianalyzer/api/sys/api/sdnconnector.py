"""
FortiAnalyzer API endpoint: sys.api.sdnconnector

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysApiSdnconnector:
    """
    FortiAnalyzer endpoint: sys.api.sdnconnector
    
    
    Available methods: exec
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def exec(
        self,
        adom: str | None = None,
        command: str | None = None,
        connector_name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            adom: ADOM name.
            command: For ACI and Nuage connector only, can be either <b>egps</b> or <b>tenants</b>.
            connector_name: Connector object in ADOM to be queried.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/sys/api/sdnconnector"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if command is not None:
            data["command"] = command
        if connector_name is not None:
            data["connector_name"] = connector_name
        
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

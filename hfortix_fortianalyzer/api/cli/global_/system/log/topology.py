"""
FortiAnalyzer API endpoint: cli.global.system.log.topology

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogTopology:
    """
    FortiAnalyzer endpoint: cli.global.system.log.topology
    
    
    Available methods: get, set, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/topology"
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(self, max_depth: int | None = None, max_depth_share: int | None = None) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            max_depth: max-depth parameter
            max_depth_share: max-depth-share parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/topology"
        
        # Build data payload
        data = {}
        if max_depth is not None:
            data["max-depth"] = max_depth
        if max_depth_share is not None:
            data["max-depth-share"] = max_depth_share
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def update(self, max_depth: int | None = None, max_depth_share: int | None = None) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            max_depth: max-depth parameter
            max_depth_share: max-depth-share parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/topology"
        
        # Build data payload
        data = {}
        if max_depth is not None:
            data["max-depth"] = max_depth
        if max_depth_share is not None:
            data["max-depth-share"] = max_depth_share
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

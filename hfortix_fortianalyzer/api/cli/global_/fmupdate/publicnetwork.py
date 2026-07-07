"""
FortiAnalyzer API endpoint: cli.global.fmupdate.publicnetwork

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdatePublicnetwork:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.publicnetwork
    
    
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
        url = "/cli/global/fmupdate/publicnetwork"
        
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

    def set(self, status: Literal["disable", "enable"] | None = None, update_server_location: Literal["global", "usa", "eu"] | None = None) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            status: status parameter
            update_server_location: update-server-location parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/publicnetwork"
        
        # Build data payload
        data = {}
        if status is not None:
            data["status"] = status
        if update_server_location is not None:
            data["update-server-location"] = update_server_location
        
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

    def update(self, status: Literal["disable", "enable"] | None = None, update_server_location: Literal["global", "usa", "eu"] | None = None) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            status: status parameter
            update_server_location: update-server-location parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/publicnetwork"
        
        # Build data payload
        data = {}
        if status is not None:
            data["status"] = status
        if update_server_location is not None:
            data["update-server-location"] = update_server_location
        
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

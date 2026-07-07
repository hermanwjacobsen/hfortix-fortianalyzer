"""
FortiAnalyzer API endpoint: cli.global.fmupdate.multilayer

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateMultilayer:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.multilayer
    
    
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
        url = "/cli/global/fmupdate/multilayer"
        
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

    def set(self, webspam_rating: Literal["disable", "enable"] | None = None) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            webspam_rating: webspam-rating parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/multilayer"
        
        # Build data payload
        data = {}
        if webspam_rating is not None:
            data["webspam-rating"] = webspam_rating
        
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

    def update(self, webspam_rating: Literal["disable", "enable"] | None = None) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            webspam_rating: webspam-rating parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/multilayer"
        
        # Build data payload
        data = {}
        if webspam_rating is not None:
            data["webspam-rating"] = webspam_rating
        
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

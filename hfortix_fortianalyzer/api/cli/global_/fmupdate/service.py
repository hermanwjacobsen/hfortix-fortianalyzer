"""
FortiAnalyzer API endpoint: cli.global.fmupdate.service

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateService:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.service
    
    
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
        url = "/cli/global/fmupdate/service"
        
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

    def set(self, avips: Literal["disable", "enable"] | None = None, geoip: Literal["disable", "enable"] | None = None) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            avips: avips parameter
            geoip: geoip parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/service"
        
        # Build data payload
        data = {}
        if avips is not None:
            data["avips"] = avips
        if geoip is not None:
            data["geoip"] = geoip
        
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

    def update(self, avips: Literal["disable", "enable"] | None = None, geoip: Literal["disable", "enable"] | None = None) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            avips: avips parameter
            geoip: geoip parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/service"
        
        # Build data payload
        data = {}
        if avips is not None:
            data["avips"] = avips
        if geoip is not None:
            data["geoip"] = geoip
        
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

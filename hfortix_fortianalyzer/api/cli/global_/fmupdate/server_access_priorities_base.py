"""
FortiAnalyzer API endpoint: cli.global.fmupdate.server-access-priorities

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateServerAccessPriorities:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.server-access-priorities
    
    
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
        url = "/cli/global/fmupdate/server-access-priorities"
        
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

    def set(
        self,
        access_public: Literal["disable", "enable"] | None = None,
        av_ips: Literal["disable", "enable"] | None = None,
        web_spam: Literal["disable", "enable"] | None = None,
        private_server: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            access_public: access-public parameter
            av_ips: av-ips parameter
            private_server: private-server parameter
            web_spam: web-spam parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/server-access-priorities"
        
        # Build data payload
        data = {}
        if access_public is not None:
            data["access-public"] = access_public
        if av_ips is not None:
            data["av-ips"] = av_ips
        if private_server is not None:
            data["private-server"] = private_server
        if web_spam is not None:
            data["web-spam"] = web_spam
        
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

    def update(
        self,
        access_public: Literal["disable", "enable"] | None = None,
        av_ips: Literal["disable", "enable"] | None = None,
        web_spam: Literal["disable", "enable"] | None = None,
        private_server: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            access_public: access-public parameter
            av_ips: av-ips parameter
            private_server: private-server parameter
            web_spam: web-spam parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/server-access-priorities"
        
        # Build data payload
        data = {}
        if access_public is not None:
            data["access-public"] = access_public
        if av_ips is not None:
            data["av-ips"] = av_ips
        if private_server is not None:
            data["private-server"] = private_server
        if web_spam is not None:
            data["web-spam"] = web_spam
        
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

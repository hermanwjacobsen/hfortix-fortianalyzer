"""
FortiAnalyzer API endpoint: cli.global.system.web-proxy

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemWebProxy:
    """
    FortiAnalyzer endpoint: cli.global.system.web-proxy
    
    
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
        url = "/cli/global/system/web-proxy"
        
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
        mode: Literal["proxy", "tunnel"] | None = None,
        port: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        address: str | None = None,
        password: list[Any] | None = None,
        username: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            address: address parameter
            mode: mode parameter
            password: password parameter
            port: port parameter
            status: status parameter
            username: username parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/web-proxy"
        
        # Build data payload
        data = {}
        if address is not None:
            data["address"] = address
        if mode is not None:
            data["mode"] = mode
        if password is not None:
            data["password"] = password
        if port is not None:
            data["port"] = port
        if status is not None:
            data["status"] = status
        if username is not None:
            data["username"] = username
        
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
        mode: Literal["proxy", "tunnel"] | None = None,
        port: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        address: str | None = None,
        password: list[Any] | None = None,
        username: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            address: address parameter
            mode: mode parameter
            password: password parameter
            port: port parameter
            status: status parameter
            username: username parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/web-proxy"
        
        # Build data payload
        data = {}
        if address is not None:
            data["address"] = address
        if mode is not None:
            data["mode"] = mode
        if password is not None:
            data["password"] = password
        if port is not None:
            data["port"] = port
        if status is not None:
            data["status"] = status
        if username is not None:
            data["username"] = username
        
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

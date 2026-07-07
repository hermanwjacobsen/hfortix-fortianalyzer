"""
FortiAnalyzer API endpoint: cli.global.system.soc-fabric

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSocFabric:
    """
    FortiAnalyzer endpoint: cli.global.system.soc-fabric
    
    
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
        url = "/cli/global/system/soc-fabric"
        
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
        port: int | None = None,
        role: Literal["member", "supervisor"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        name: str | None = None,
        supervisor: str | None = None,
        trusted_list: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            name: name parameter
            port: port parameter
            role: role parameter
            secure_connection: secure-connection parameter
            status: status parameter
            supervisor: supervisor parameter
            trusted_list: trusted-list parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/soc-fabric"
        
        # Build data payload
        data = {}
        if name is not None:
            data["name"] = name
        if port is not None:
            data["port"] = port
        if role is not None:
            data["role"] = role
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if status is not None:
            data["status"] = status
        if supervisor is not None:
            data["supervisor"] = supervisor
        if trusted_list is not None:
            data["trusted-list"] = trusted_list
        
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
        port: int | None = None,
        role: Literal["member", "supervisor"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        name: str | None = None,
        supervisor: str | None = None,
        trusted_list: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            name: name parameter
            port: port parameter
            role: role parameter
            secure_connection: secure-connection parameter
            status: status parameter
            supervisor: supervisor parameter
            trusted_list: trusted-list parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/soc-fabric"
        
        # Build data payload
        data = {}
        if name is not None:
            data["name"] = name
        if port is not None:
            data["port"] = port
        if role is not None:
            data["role"] = role
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if status is not None:
            data["status"] = status
        if supervisor is not None:
            data["supervisor"] = supervisor
        if trusted_list is not None:
            data["trusted-list"] = trusted_list
        
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

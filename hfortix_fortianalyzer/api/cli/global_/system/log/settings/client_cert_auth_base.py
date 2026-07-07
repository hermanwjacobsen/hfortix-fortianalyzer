"""
FortiAnalyzer API endpoint: cli.global.system.log.settings.client-cert-auth

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogSettingsClientCertAuth:
    """
    FortiAnalyzer endpoint: cli.global.system.log.settings.client-cert-auth
    
    
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
        url = "/cli/global/system/log/settings/client-cert-auth"
        
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
        mode: Literal["basic", "strict"] | None = None,
        tls_port: Literal["both", "514", "6514"] | None = None,
        trusted_client: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            mode: mode parameter
            tls_port: tls-port parameter
            trusted_client: trusted-client parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/settings/client-cert-auth"
        
        # Build data payload
        data = {}
        if mode is not None:
            data["mode"] = mode
        if tls_port is not None:
            data["tls-port"] = tls_port
        if trusted_client is not None:
            data["trusted-client"] = trusted_client
        
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
        mode: Literal["basic", "strict"] | None = None,
        tls_port: Literal["both", "514", "6514"] | None = None,
        trusted_client: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            mode: mode parameter
            tls_port: tls-port parameter
            trusted_client: trusted-client parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/settings/client-cert-auth"
        
        # Build data payload
        data = {}
        if mode is not None:
            data["mode"] = mode
        if tls_port is not None:
            data["tls-port"] = tls_port
        if trusted_client is not None:
            data["trusted-client"] = trusted_client
        
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

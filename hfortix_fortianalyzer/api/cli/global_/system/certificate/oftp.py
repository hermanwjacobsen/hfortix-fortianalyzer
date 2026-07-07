"""
FortiAnalyzer API endpoint: cli.global.system.certificate.oftp

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCertificateOftp:
    """
    FortiAnalyzer endpoint: cli.global.system.certificate.oftp
    
    
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
        url = "/cli/global/system/certificate/oftp"
        
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
        mode: Literal["default", "custom", "local"] | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        local: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            certificate: certificate parameter
            comment: comment parameter
            local: local parameter
            mode: mode parameter
            password: password parameter
            private_key: private-key parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/certificate/oftp"
        
        # Build data payload
        data = {}
        if certificate is not None:
            data["certificate"] = certificate
        if comment is not None:
            data["comment"] = comment
        if local is not None:
            data["local"] = local
        if mode is not None:
            data["mode"] = mode
        if password is not None:
            data["password"] = password
        if private_key is not None:
            data["private-key"] = private_key
        
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
        mode: Literal["default", "custom", "local"] | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        local: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            certificate: certificate parameter
            comment: comment parameter
            local: local parameter
            mode: mode parameter
            password: password parameter
            private_key: private-key parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/certificate/oftp"
        
        # Build data payload
        data = {}
        if certificate is not None:
            data["certificate"] = certificate
        if comment is not None:
            data["comment"] = comment
        if local is not None:
            data["local"] = local
        if mode is not None:
            data["mode"] = mode
        if password is not None:
            data["password"] = password
        if private_key is not None:
            data["private-key"] = private_key
        
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

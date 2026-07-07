"""
FortiAnalyzer API endpoint: cli.global.system.log.ueba

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogUeba:
    """
    FortiAnalyzer endpoint: cli.global.system.log.ueba
    
    
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
        url = "/cli/global/system/log/ueba"
        
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
        hostname_ep_unifier: Literal["disable", "enable"] | None = None,
        ip_only_ep: Literal["disable", "enable"] | None = None,
        ip_unique_scope: Literal["adom", "vdom"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            hostname_ep_unifier: hostname-ep-unifier parameter
            ip_only_ep: ip-only-ep parameter
            ip_unique_scope: ip-unique-scope parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/ueba"
        
        # Build data payload
        data = {}
        if hostname_ep_unifier is not None:
            data["hostname-ep-unifier"] = hostname_ep_unifier
        if ip_only_ep is not None:
            data["ip-only-ep"] = ip_only_ep
        if ip_unique_scope is not None:
            data["ip-unique-scope"] = ip_unique_scope
        
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
        hostname_ep_unifier: Literal["disable", "enable"] | None = None,
        ip_only_ep: Literal["disable", "enable"] | None = None,
        ip_unique_scope: Literal["adom", "vdom"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            hostname_ep_unifier: hostname-ep-unifier parameter
            ip_only_ep: ip-only-ep parameter
            ip_unique_scope: ip-unique-scope parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/ueba"
        
        # Build data payload
        data = {}
        if hostname_ep_unifier is not None:
            data["hostname-ep-unifier"] = hostname_ep_unifier
        if ip_only_ep is not None:
            data["ip-only-ep"] = ip_only_ep
        if ip_unique_scope is not None:
            data["ip-unique-scope"] = ip_unique_scope
        
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

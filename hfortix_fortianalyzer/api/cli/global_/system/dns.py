"""
FortiAnalyzer API endpoint: cli.global.system.dns

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemDns:
    """
    FortiAnalyzer endpoint: cli.global.system.dns
    
    
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
        url = "/cli/global/system/dns"
        
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
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        primary: str | None = None,
        secondary: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            ip6_primary: ip6-primary parameter
            ip6_secondary: ip6-secondary parameter
            primary: primary parameter
            secondary: secondary parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/dns"
        
        # Build data payload
        data = {}
        if ip6_primary is not None:
            data["ip6-primary"] = ip6_primary
        if ip6_secondary is not None:
            data["ip6-secondary"] = ip6_secondary
        if primary is not None:
            data["primary"] = primary
        if secondary is not None:
            data["secondary"] = secondary
        
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
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        primary: str | None = None,
        secondary: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            ip6_primary: ip6-primary parameter
            ip6_secondary: ip6-secondary parameter
            primary: primary parameter
            secondary: secondary parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/dns"
        
        # Build data payload
        data = {}
        if ip6_primary is not None:
            data["ip6-primary"] = ip6_primary
        if ip6_secondary is not None:
            data["ip6-secondary"] = ip6_secondary
        if primary is not None:
            data["primary"] = primary
        if secondary is not None:
            data["secondary"] = secondary
        
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

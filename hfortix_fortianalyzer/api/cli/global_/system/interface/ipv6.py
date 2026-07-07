"""
FortiAnalyzer API endpoint: cli.global.system.interface.ipv6

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemInterfaceIpv6:
    """
    FortiAnalyzer endpoint: cli.global.system.interface.ipv6
    
    
    Available methods: get, set, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self, interface: str) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            interface: interface parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/interface/{interface}/ipv6"
        url = url.replace("{interface}", interface)
        
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
        interface: str,
        ip6_address: str | None = None,
        ip6_autoconf: Literal["disable", "enable"] | None = None,
        ip6_allowaccess: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            interface: interface parameter
            ip6_address: ip6-address parameter
            ip6_allowaccess: ip6-allowaccess parameter
            ip6_autoconf: ip6-autoconf parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/interface/{interface}/ipv6"
        url = url.replace("{interface}", interface)
        
        # Build data payload
        data = {}
        if ip6_address is not None:
            data["ip6-address"] = ip6_address
        if ip6_allowaccess is not None:
            data["ip6-allowaccess"] = ip6_allowaccess
        if ip6_autoconf is not None:
            data["ip6-autoconf"] = ip6_autoconf
        
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
        interface: str,
        ip6_address: str | None = None,
        ip6_autoconf: Literal["disable", "enable"] | None = None,
        ip6_allowaccess: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            interface: interface parameter
            ip6_address: ip6-address parameter
            ip6_allowaccess: ip6-allowaccess parameter
            ip6_autoconf: ip6-autoconf parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/interface/{interface}/ipv6"
        url = url.replace("{interface}", interface)
        
        # Build data payload
        data = {}
        if ip6_address is not None:
            data["ip6-address"] = ip6_address
        if ip6_allowaccess is not None:
            data["ip6-allowaccess"] = ip6_allowaccess
        if ip6_autoconf is not None:
            data["ip6-autoconf"] = ip6_autoconf
        
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

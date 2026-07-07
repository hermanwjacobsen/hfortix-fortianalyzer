"""
FortiAnalyzer API endpoint: cli.global.system.log.pcap-file

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogPcapFile:
    """
    FortiAnalyzer endpoint: cli.global.system.log.pcap-file
    
    
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
        url = "/cli/global/system/log/pcap-file"
        
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

    def set(self, download_mode: Literal["plain", "zip", "zip-with-password"] | None = None) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            download_mode: download-mode parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/pcap-file"
        
        # Build data payload
        data = {}
        if download_mode is not None:
            data["download-mode"] = download_mode
        
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

    def update(self, download_mode: Literal["plain", "zip", "zip-with-password"] | None = None) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            download_mode: download-mode parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/pcap-file"
        
        # Build data payload
        data = {}
        if download_mode is not None:
            data["download-mode"] = download_mode
        
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

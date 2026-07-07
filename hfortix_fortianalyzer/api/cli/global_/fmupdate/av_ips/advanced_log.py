"""
FortiAnalyzer API endpoint: cli.global.fmupdate.av-ips.advanced-log

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateAvIpsAdvancedLog:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.av-ips.advanced-log
    
    
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
        url = "/cli/global/fmupdate/av-ips/advanced-log"
        
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

    def set(self, log_fortigate: Literal["disable", "enable"] | None = None, log_server: Literal["disable", "enable"] | None = None) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            log_fortigate: log-fortigate parameter
            log_server: log-server parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/av-ips/advanced-log"
        
        # Build data payload
        data = {}
        if log_fortigate is not None:
            data["log-fortigate"] = log_fortigate
        if log_server is not None:
            data["log-server"] = log_server
        
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

    def update(self, log_fortigate: Literal["disable", "enable"] | None = None, log_server: Literal["disable", "enable"] | None = None) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            log_fortigate: log-fortigate parameter
            log_server: log-server parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/av-ips/advanced-log"
        
        # Build data payload
        data = {}
        if log_fortigate is not None:
            data["log-fortigate"] = log_fortigate
        if log_server is not None:
            data["log-server"] = log_server
        
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

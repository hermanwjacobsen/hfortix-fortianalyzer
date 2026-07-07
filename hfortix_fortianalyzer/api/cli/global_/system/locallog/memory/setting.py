"""
FortiAnalyzer API endpoint: cli.global.system.locallog.memory.setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogMemorySetting:
    """
    FortiAnalyzer endpoint: cli.global.system.locallog.memory.setting
    
    
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
        url = "/cli/global/system/locallog/memory/setting"
        
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
        diskfull: Literal["overwrite", "nolog"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            diskfull: diskfull parameter
            severity: severity parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/memory/setting"
        
        # Build data payload
        data = {}
        if diskfull is not None:
            data["diskfull"] = diskfull
        if severity is not None:
            data["severity"] = severity
        if status is not None:
            data["status"] = status
        
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
        diskfull: Literal["overwrite", "nolog"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            diskfull: diskfull parameter
            severity: severity parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/memory/setting"
        
        # Build data payload
        data = {}
        if diskfull is not None:
            data["diskfull"] = diskfull
        if severity is not None:
            data["severity"] = severity
        if status is not None:
            data["status"] = status
        
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

"""
FortiAnalyzer API endpoint: cli.global.system.alert-console

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAlertConsole:
    """
    FortiAnalyzer endpoint: cli.global.system.alert-console
    
    
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
        url = "/cli/global/system/alert-console"
        
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

    def set(self, period: Literal["1", "2", "3", "4", "5", "6", "7"] | None = None, severity_level: Literal["emergency", "alert", "critical", "error", "warning", "notify", "information", "debug"] | None = None) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            period: period parameter
            severity_level: severity-level parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/alert-console"
        
        # Build data payload
        data = {}
        if period is not None:
            data["period"] = period
        if severity_level is not None:
            data["severity-level"] = severity_level
        
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

    def update(self, period: Literal["1", "2", "3", "4", "5", "6", "7"] | None = None, severity_level: Literal["emergency", "alert", "critical", "error", "warning", "notify", "information", "debug"] | None = None) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            period: period parameter
            severity_level: severity-level parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/alert-console"
        
        # Build data payload
        data = {}
        if period is not None:
            data["period"] = period
        if severity_level is not None:
            data["severity-level"] = severity_level
        
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

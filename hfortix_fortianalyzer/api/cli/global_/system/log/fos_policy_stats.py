"""
FortiAnalyzer API endpoint: cli.global.system.log.fos-policy-stats

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogFosPolicyStats:
    """
    FortiAnalyzer endpoint: cli.global.system.log.fos-policy-stats
    
    
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
        url = "/cli/global/system/log/fos-policy-stats"
        
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
        retention_days: int | None = None,
        sampling_interval: int | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            retention_days: retention-days parameter
            sampling_interval: sampling-interval parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/fos-policy-stats"
        
        # Build data payload
        data = {}
        if retention_days is not None:
            data["retention-days"] = retention_days
        if sampling_interval is not None:
            data["sampling-interval"] = sampling_interval
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
        retention_days: int | None = None,
        sampling_interval: int | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            retention_days: retention-days parameter
            sampling_interval: sampling-interval parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/fos-policy-stats"
        
        # Build data payload
        data = {}
        if retention_days is not None:
            data["retention-days"] = retention_days
        if sampling_interval is not None:
            data["sampling-interval"] = sampling_interval
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

"""
FortiAnalyzer API endpoint: cli.global.system.log-forward-service

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogForwardService:
    """
    FortiAnalyzer endpoint: cli.global.system.log-forward-service
    
    
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
        url = "/cli/global/system/log-forward-service"
        
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
        accept_aggregation: Literal["disable", "enable"] | None = None,
        aggregation_disk_quota: int | None = None,
        collector_auth: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            accept_aggregation: accept-aggregation parameter
            aggregation_disk_quota: aggregation-disk-quota parameter
            collector_auth: collector-auth parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log-forward-service"
        
        # Build data payload
        data = {}
        if accept_aggregation is not None:
            data["accept-aggregation"] = accept_aggregation
        if aggregation_disk_quota is not None:
            data["aggregation-disk-quota"] = aggregation_disk_quota
        if collector_auth is not None:
            data["collector-auth"] = collector_auth
        
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
        accept_aggregation: Literal["disable", "enable"] | None = None,
        aggregation_disk_quota: int | None = None,
        collector_auth: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            accept_aggregation: accept-aggregation parameter
            aggregation_disk_quota: aggregation-disk-quota parameter
            collector_auth: collector-auth parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log-forward-service"
        
        # Build data payload
        data = {}
        if accept_aggregation is not None:
            data["accept-aggregation"] = accept_aggregation
        if aggregation_disk_quota is not None:
            data["aggregation-disk-quota"] = aggregation_disk_quota
        if collector_auth is not None:
            data["collector-auth"] = collector_auth
        
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

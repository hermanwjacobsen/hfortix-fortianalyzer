"""
FortiAnalyzer API endpoint: cli.global.system.log.interface-stats

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogInterfaceStats:
    """
    FortiAnalyzer endpoint: cli.global.system.log.interface-stats
    
    
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
        url = "/cli/global/system/log/interface-stats"
        
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
        billing_report: Literal["disable", "enable"] | None = None,
        retention_days: int | None = None,
        sampling_interval: int | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            billing_report: billing-report parameter
            retention_days: retention-days parameter
            sampling_interval: sampling-interval parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/interface-stats"
        
        # Build data payload
        data = {}
        if billing_report is not None:
            data["billing-report"] = billing_report
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
        billing_report: Literal["disable", "enable"] | None = None,
        retention_days: int | None = None,
        sampling_interval: int | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            billing_report: billing-report parameter
            retention_days: retention-days parameter
            sampling_interval: sampling-interval parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/interface-stats"
        
        # Build data payload
        data = {}
        if billing_report is not None:
            data["billing-report"] = billing_report
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

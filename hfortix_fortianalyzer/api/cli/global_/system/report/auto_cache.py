"""
FortiAnalyzer API endpoint: cli.global.system.report.auto-cache

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemReportAutoCache:
    """
    FortiAnalyzer endpoint: cli.global.system.report.auto-cache
    
    
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
        url = "/cli/global/system/report/auto-cache"
        
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
        aggressive_schedule: Literal["disable", "enable"] | None = None,
        order: Literal["oldest-first"] | None = None,
        sche_rpt_only: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            aggressive_schedule: aggressive-schedule parameter
            order: order parameter
            sche_rpt_only: sche-rpt-only parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/report/auto-cache"
        
        # Build data payload
        data = {}
        if aggressive_schedule is not None:
            data["aggressive-schedule"] = aggressive_schedule
        if order is not None:
            data["order"] = order
        if sche_rpt_only is not None:
            data["sche-rpt-only"] = sche_rpt_only
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
        aggressive_schedule: Literal["disable", "enable"] | None = None,
        order: Literal["oldest-first"] | None = None,
        sche_rpt_only: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            aggressive_schedule: aggressive-schedule parameter
            order: order parameter
            sche_rpt_only: sche-rpt-only parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/report/auto-cache"
        
        # Build data payload
        data = {}
        if aggressive_schedule is not None:
            data["aggressive-schedule"] = aggressive_schedule
        if order is not None:
            data["order"] = order
        if sche_rpt_only is not None:
            data["sche-rpt-only"] = sche_rpt_only
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

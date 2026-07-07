"""
FortiAnalyzer API endpoint: cli.global.system.fortiview.auto-cache

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemFortiviewAutoCache:
    """
    FortiAnalyzer endpoint: cli.global.system.fortiview.auto-cache
    
    
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
        url = "/cli/global/system/fortiview/auto-cache"
        
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
        aggressive_fortiview: Literal["disable", "enable"] | None = None,
        incr_fortiview: Literal["disable", "enable"] | None = None,
        interval: int | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            aggressive_fortiview: aggressive-fortiview parameter
            incr_fortiview: incr-fortiview parameter
            interval: interval parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/fortiview/auto-cache"
        
        # Build data payload
        data = {}
        if aggressive_fortiview is not None:
            data["aggressive-fortiview"] = aggressive_fortiview
        if incr_fortiview is not None:
            data["incr-fortiview"] = incr_fortiview
        if interval is not None:
            data["interval"] = interval
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
        aggressive_fortiview: Literal["disable", "enable"] | None = None,
        incr_fortiview: Literal["disable", "enable"] | None = None,
        interval: int | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            aggressive_fortiview: aggressive-fortiview parameter
            incr_fortiview: incr-fortiview parameter
            interval: interval parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/fortiview/auto-cache"
        
        # Build data payload
        data = {}
        if aggressive_fortiview is not None:
            data["aggressive-fortiview"] = aggressive_fortiview
        if incr_fortiview is not None:
            data["incr-fortiview"] = incr_fortiview
        if interval is not None:
            data["interval"] = interval
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

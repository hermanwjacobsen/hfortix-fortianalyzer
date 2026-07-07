"""
FortiAnalyzer API endpoint: cli.global.system.log.ratelimit

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogRatelimit:
    """
    FortiAnalyzer endpoint: cli.global.system.log.ratelimit
    
    
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
        url = "/cli/global/system/log/ratelimit"
        
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
        device_ratelimit_default: int | None = None,
        mode: Literal["disable", "manual"] | None = None,
        system_ratelimit: int | None = None,
        ratelimits: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            device_ratelimit_default: device-ratelimit-default parameter
            mode: mode parameter
            ratelimits: ratelimits parameter
            system_ratelimit: system-ratelimit parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/ratelimit"
        
        # Build data payload
        data = {}
        if device_ratelimit_default is not None:
            data["device-ratelimit-default"] = device_ratelimit_default
        if mode is not None:
            data["mode"] = mode
        if ratelimits is not None:
            data["ratelimits"] = ratelimits
        if system_ratelimit is not None:
            data["system-ratelimit"] = system_ratelimit
        
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
        device_ratelimit_default: int | None = None,
        mode: Literal["disable", "manual"] | None = None,
        system_ratelimit: int | None = None,
        ratelimits: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            device_ratelimit_default: device-ratelimit-default parameter
            mode: mode parameter
            ratelimits: ratelimits parameter
            system_ratelimit: system-ratelimit parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/ratelimit"
        
        # Build data payload
        data = {}
        if device_ratelimit_default is not None:
            data["device-ratelimit-default"] = device_ratelimit_default
        if mode is not None:
            data["mode"] = mode
        if ratelimits is not None:
            data["ratelimits"] = ratelimits
        if system_ratelimit is not None:
            data["system-ratelimit"] = system_ratelimit
        
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

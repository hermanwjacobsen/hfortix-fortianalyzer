"""
FortiAnalyzer API endpoint: cli.global.system.log.api-ratelimit

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogApiRatelimit:
    """
    FortiAnalyzer endpoint: cli.global.system.log.api-ratelimit
    
    
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
        url = "/cli/global/system/log/api-ratelimit"
        
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

    def set(self, read_limit: int | None = None, write_limit: int | None = None) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            read_limit: read-limit parameter
            write_limit: write-limit parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/api-ratelimit"
        
        # Build data payload
        data = {}
        if read_limit is not None:
            data["read-limit"] = read_limit
        if write_limit is not None:
            data["write-limit"] = write_limit
        
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

    def update(self, read_limit: int | None = None, write_limit: int | None = None) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            read_limit: read-limit parameter
            write_limit: write-limit parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/api-ratelimit"
        
        # Build data payload
        data = {}
        if read_limit is not None:
            data["read-limit"] = read_limit
        if write_limit is not None:
            data["write-limit"] = write_limit
        
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

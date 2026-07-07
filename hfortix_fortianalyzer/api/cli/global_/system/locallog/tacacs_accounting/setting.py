"""
FortiAnalyzer API endpoint: cli.global.system.locallog.tacacs+accounting.setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogTacacsAccountingSetting:
    """
    FortiAnalyzer endpoint: cli.global.system.locallog.tacacs+accounting.setting
    
    
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
        url = "/cli/global/system/locallog/tacacs+accounting/setting"
        
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
        status: Literal["disable", "enable"] | None = None,
        timeout: int | None = None,
        tacacs_name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            status: status parameter
            tacacs_name: tacacs-name parameter
            timeout: timeout parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/tacacs+accounting/setting"
        
        # Build data payload
        data = {}
        if status is not None:
            data["status"] = status
        if tacacs_name is not None:
            data["tacacs-name"] = tacacs_name
        if timeout is not None:
            data["timeout"] = timeout
        
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
        status: Literal["disable", "enable"] | None = None,
        timeout: int | None = None,
        tacacs_name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            status: status parameter
            tacacs_name: tacacs-name parameter
            timeout: timeout parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/tacacs+accounting/setting"
        
        # Build data payload
        data = {}
        if status is not None:
            data["status"] = status
        if tacacs_name is not None:
            data["tacacs-name"] = tacacs_name
        if timeout is not None:
            data["timeout"] = timeout
        
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

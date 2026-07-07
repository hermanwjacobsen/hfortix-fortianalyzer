"""
FortiAnalyzer API endpoint: cli.global.system.locallog.tacacs+accounting.filter

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogTacacsAccountingFilter:
    """
    FortiAnalyzer endpoint: cli.global.system.locallog.tacacs+accounting.filter
    
    
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
        url = "/cli/global/system/locallog/tacacs+accounting/filter"
        
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
        cli_cmd_audit: Literal["disable", "enable"] | None = None,
        config_change_audit: Literal["disable", "enable"] | None = None,
        login_audit: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            cli_cmd_audit: cli-cmd-audit parameter
            config_change_audit: config-change-audit parameter
            login_audit: login-audit parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/tacacs+accounting/filter"
        
        # Build data payload
        data = {}
        if cli_cmd_audit is not None:
            data["cli-cmd-audit"] = cli_cmd_audit
        if config_change_audit is not None:
            data["config-change-audit"] = config_change_audit
        if login_audit is not None:
            data["login-audit"] = login_audit
        
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
        cli_cmd_audit: Literal["disable", "enable"] | None = None,
        config_change_audit: Literal["disable", "enable"] | None = None,
        login_audit: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            cli_cmd_audit: cli-cmd-audit parameter
            config_change_audit: config-change-audit parameter
            login_audit: login-audit parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/tacacs+accounting/filter"
        
        # Build data payload
        data = {}
        if cli_cmd_audit is not None:
            data["cli-cmd-audit"] = cli_cmd_audit
        if config_change_audit is not None:
            data["config-change-audit"] = config_change_audit
        if login_audit is not None:
            data["login-audit"] = login_audit
        
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

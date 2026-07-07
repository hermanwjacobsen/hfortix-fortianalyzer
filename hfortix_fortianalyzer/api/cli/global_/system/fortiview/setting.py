"""
FortiAnalyzer API endpoint: cli.global.system.fortiview.setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemFortiviewSetting:
    """
    FortiAnalyzer endpoint: cli.global.system.fortiview.setting
    
    
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
        url = "/cli/global/system/fortiview/setting"
        
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
        data_source: Literal["auto", "cache-only", "log-and-cache"] | None = None,
        not_scanned_apps: Literal["exclude", "include"] | None = None,
        query_run_mode: Literal["auto", "boost"] | None = None,
        resolve_ip: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            data_source: data-source parameter
            not_scanned_apps: not-scanned-apps parameter
            query_run_mode: query-run-mode parameter
            resolve_ip: resolve-ip parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/fortiview/setting"
        
        # Build data payload
        data = {}
        if data_source is not None:
            data["data-source"] = data_source
        if not_scanned_apps is not None:
            data["not-scanned-apps"] = not_scanned_apps
        if query_run_mode is not None:
            data["query-run-mode"] = query_run_mode
        if resolve_ip is not None:
            data["resolve-ip"] = resolve_ip
        
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
        data_source: Literal["auto", "cache-only", "log-and-cache"] | None = None,
        not_scanned_apps: Literal["exclude", "include"] | None = None,
        query_run_mode: Literal["auto", "boost"] | None = None,
        resolve_ip: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            data_source: data-source parameter
            not_scanned_apps: not-scanned-apps parameter
            query_run_mode: query-run-mode parameter
            resolve_ip: resolve-ip parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/fortiview/setting"
        
        # Build data payload
        data = {}
        if data_source is not None:
            data["data-source"] = data_source
        if not_scanned_apps is not None:
            data["not-scanned-apps"] = not_scanned_apps
        if query_run_mode is not None:
            data["query-run-mode"] = query_run_mode
        if resolve_ip is not None:
            data["resolve-ip"] = resolve_ip
        
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

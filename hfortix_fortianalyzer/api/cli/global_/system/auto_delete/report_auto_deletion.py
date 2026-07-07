"""
FortiAnalyzer API endpoint: cli.global.system.auto-delete.report-auto-deletion

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAutoDeleteReportAutoDeletion:
    """
    FortiAnalyzer endpoint: cli.global.system.auto-delete.report-auto-deletion
    
    
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
        url = "/cli/global/system/auto-delete/report-auto-deletion"
        
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
        retention: Literal["days", "weeks", "months"] | None = None,
        runat: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        value: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            retention: retention parameter
            runat: runat parameter
            status: status parameter
            value: value parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/auto-delete/report-auto-deletion"
        
        # Build data payload
        data = {}
        if retention is not None:
            data["retention"] = retention
        if runat is not None:
            data["runat"] = runat
        if status is not None:
            data["status"] = status
        if value is not None:
            data["value"] = value
        
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
        retention: Literal["days", "weeks", "months"] | None = None,
        runat: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        value: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            retention: retention parameter
            runat: runat parameter
            status: status parameter
            value: value parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/auto-delete/report-auto-deletion"
        
        # Build data payload
        data = {}
        if retention is not None:
            data["retention"] = retention
        if runat is not None:
            data["runat"] = runat
        if status is not None:
            data["status"] = status
        if value is not None:
            data["value"] = value
        
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

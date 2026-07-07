"""
FortiAnalyzer API endpoint: cli.global.system.log.ioc

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogIoc:
    """
    FortiAnalyzer endpoint: cli.global.system.log.ioc
    
    
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
        url = "/cli/global/system/log/ioc"
        
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
        notification: Literal["disable", "enable"] | None = None,
        notification_throttle: int | None = None,
        rescan_max_runner: int | None = None,
        rescan_run_at: int | None = None,
        rescan_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            notification: notification parameter
            notification_throttle: notification-throttle parameter
            rescan_max_runner: rescan-max-runner parameter
            rescan_run_at: rescan-run-at parameter
            rescan_status: rescan-status parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/ioc"
        
        # Build data payload
        data = {}
        if notification is not None:
            data["notification"] = notification
        if notification_throttle is not None:
            data["notification-throttle"] = notification_throttle
        if rescan_max_runner is not None:
            data["rescan-max-runner"] = rescan_max_runner
        if rescan_run_at is not None:
            data["rescan-run-at"] = rescan_run_at
        if rescan_status is not None:
            data["rescan-status"] = rescan_status
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
        notification: Literal["disable", "enable"] | None = None,
        notification_throttle: int | None = None,
        rescan_max_runner: int | None = None,
        rescan_run_at: int | None = None,
        rescan_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            notification: notification parameter
            notification_throttle: notification-throttle parameter
            rescan_max_runner: rescan-max-runner parameter
            rescan_run_at: rescan-run-at parameter
            rescan_status: rescan-status parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/ioc"
        
        # Build data payload
        data = {}
        if notification is not None:
            data["notification"] = notification
        if notification_throttle is not None:
            data["notification-throttle"] = notification_throttle
        if rescan_max_runner is not None:
            data["rescan-max-runner"] = rescan_max_runner
        if rescan_run_at is not None:
            data["rescan-run-at"] = rescan_run_at
        if rescan_status is not None:
            data["rescan-status"] = rescan_status
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

"""
FortiAnalyzer API endpoint: cli.global.fmupdate.fds-setting.update-schedule

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFdsSettingUpdateSchedule:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.fds-setting.update-schedule
    
    
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
        url = "/cli/global/fmupdate/fds-setting/update-schedule"
        
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
        day: Literal["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] | None = None,
        frequency: Literal["every", "daily", "weekly"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        time: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            day: day parameter
            frequency: frequency parameter
            status: status parameter
            time: time parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fds-setting/update-schedule"
        
        # Build data payload
        data = {}
        if day is not None:
            data["day"] = day
        if frequency is not None:
            data["frequency"] = frequency
        if status is not None:
            data["status"] = status
        if time is not None:
            data["time"] = time
        
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
        day: Literal["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] | None = None,
        frequency: Literal["every", "daily", "weekly"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        time: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            day: day parameter
            frequency: frequency parameter
            status: status parameter
            time: time parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fds-setting/update-schedule"
        
        # Build data payload
        data = {}
        if day is not None:
            data["day"] = day
        if frequency is not None:
            data["frequency"] = frequency
        if status is not None:
            data["status"] = status
        if time is not None:
            data["time"] = time
        
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

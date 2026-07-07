"""
FortiAnalyzer API endpoint: cli.global.system.log.alert

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogAlert:
    """
    FortiAnalyzer endpoint: cli.global.system.log.alert
    
    
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
        url = "/cli/global/system/log/alert"
        
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

    def set(self, max_alert_count: int | None = None, min_severity_to_raise_incident_by_grouping: Literal["none", "critical", "high"] | None = None) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            max_alert_count: max-alert-count parameter
            min_severity_to_raise_incident_by_grouping: min-severity-to-raise-incident-by-grouping parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/alert"
        
        # Build data payload
        data = {}
        if max_alert_count is not None:
            data["max-alert-count"] = max_alert_count
        if min_severity_to_raise_incident_by_grouping is not None:
            data["min-severity-to-raise-incident-by-grouping"] = min_severity_to_raise_incident_by_grouping
        
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

    def update(self, max_alert_count: int | None = None, min_severity_to_raise_incident_by_grouping: Literal["none", "critical", "high"] | None = None) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            max_alert_count: max-alert-count parameter
            min_severity_to_raise_incident_by_grouping: min-severity-to-raise-incident-by-grouping parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/alert"
        
        # Build data payload
        data = {}
        if max_alert_count is not None:
            data["max-alert-count"] = max_alert_count
        if min_severity_to_raise_incident_by_grouping is not None:
            data["min-severity-to-raise-incident-by-grouping"] = min_severity_to_raise_incident_by_grouping
        
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

"""
FortiAnalyzer API endpoint: incidentmgmt.adom.incident.stats

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomIncidentStats:
    """
    FortiAnalyzer endpoint: incidentmgmt.adom.incident.stats
    
    Get statistics of incidents.
    
    Available methods: get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(
        self,
        adom: str,
        stats_item: list[Literal["total", "severity", "category", "status", "outbreak"]],
        apiver: int = 3,
        filter: str | None = None,
        time_range: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get statistics of incidents.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            filter: The query filter.
            stats_item: The stats item list.
            time_range: time-range parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/incident/stats"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if filter is not None:
            request_params["filter"] = filter
        if stats_item is not None:
            request_params["stats-item"] = stats_item
        if time_range is not None:
            request_params["time-range"] = time_range
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            **request_params
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

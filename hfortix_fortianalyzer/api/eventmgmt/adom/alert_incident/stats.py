"""
FortiAnalyzer API endpoint: eventmgmt.adom.alert-incident.stats

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertIncidentStats:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.alert-incident.stats
    
    Get the stats of alert-incident.
    
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
        apiver: int = 3,
        time_range: dict[str, Any] | None = None,
        timescale: Literal["month", "hour"] | None = None,
        timezone: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get the stats of alert-incident.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            time_range: Time range for source data selection.
            timescale: Time scale. Only valid for type 'severity-timescale'.
            timezone: The timezone index or name. Time range in request and date/time if any in response will follow this timezone. See Appendix
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/alert-incident/stats"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if time_range is not None:
            request_params["time-range"] = time_range
        if timescale is not None:
            request_params["timescale"] = timescale
        if timezone is not None:
            request_params["timezone"] = timezone
        
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

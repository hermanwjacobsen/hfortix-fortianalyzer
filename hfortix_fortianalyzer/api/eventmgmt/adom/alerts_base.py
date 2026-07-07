"""
FortiAnalyzer API endpoint: eventmgmt.adom.alerts

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlerts:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.alerts
    
    Get alert events.
    
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
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get alert events.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            filter: Filter expression. 'event_value', 'severity', 'trigger_name', 'count', 'comment' and 'flags' are supported. i.e.: trigger_name='Local Device Event' and severity >= 3
            limit: The max number of records to get.
            offset: offset of records to get.
            time_range: Time range for data selection.
            timezone: The timezone index or name. Time range in request and date/time if any in response will follow this timezone. See Appendix
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/alerts"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if filter is not None:
            request_params["filter"] = filter
        if limit is not None:
            request_params["limit"] = limit
        if offset is not None:
            request_params["offset"] = offset
        if time_range is not None:
            request_params["time-range"] = time_range
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

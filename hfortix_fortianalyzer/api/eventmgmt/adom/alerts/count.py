"""
FortiAnalyzer API endpoint: eventmgmt.adom.alerts.count

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertsCount:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.alerts.count
    
    Get the count of alert events.
    
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
        group_by: Literal["severity", "trigger", "severity_timescale", "eventtype", "mgmt_state", "severity_epdevtype"] | None = None,
        time_range: dict[str, Any] | None = None,
        timescale: Literal["month", "hour"] | None = None,
        timezone: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get the count of alert events.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            filter: Filter expression. 'ackflag', 'assigned', 'mgmt_state', 'triggername', 'eventtype', 'severity', 'eventstatus' and 'tag' are supported. i.e.: ackflag = no and triggername='Local Device Event'. Note: the field 'ackflag' supports = yes/no, !=yes/no and <>yes/no ,  the field 'assigned' only supports = yes/no or !=yes/no, the field 'mgmt_state' only supports (!)= acknowledged/triaged/pending_triage
            group_by: Get alert count by group.
            time_range: Time range for source data selection.
            timescale: Time scale. Only valid for type 'severity-timescale'.
            timezone: The timezone index or name. Time range in request and date/time if any in response will follow this timezone. See Appendix
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/alerts/count"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if filter is not None:
            request_params["filter"] = filter
        if group_by is not None:
            request_params["group-by"] = group_by
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

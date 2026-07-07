"""
FortiAnalyzer API endpoint: report.adom.reports.state

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomReportsState:
    """
    FortiAnalyzer endpoint: report.adom.reports.state
    
    It will list all reports in pending-running or generated state.
    
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
        state: str,
        apiver: int = 3,
        sort_by: list[dict[str, Any]] | None = None,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None,
        title: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        It will list all reports in pending-running or generated state.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            sort_by: Sort by fields. Only support <b>one field</b> for this API.
            state: pending-running, or generated.
            time_range: Time range for source data selection. It is required only if "state" is "generated".
            timezone: The timezone index or name. Time range in request and date/time if any in response will follow this timezone. See Appendix
            title: Title of a report.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/reports/state"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if sort_by is not None:
            request_params["sort-by"] = sort_by
        if state is not None:
            request_params["state"] = state
        if time_range is not None:
            request_params["time-range"] = time_range
        if timezone is not None:
            request_params["timezone"] = timezone
        if title is not None:
            request_params["title"] = title
        
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

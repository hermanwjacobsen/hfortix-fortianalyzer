"""
FortiAnalyzer API endpoint: report.adom.config.schedule.report-layout

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomConfigScheduleReportLayout:
    """
    FortiAnalyzer endpoint: report.adom.config.schedule.report-layout
    
    support method: add, set, get, update, delete<br>table: /report/adom/&lt;adom-name&gt;/config/schedule/&lt;schedule_name&gt;/report-layout<br>object: /report/adom/&lt;adom-name&gt;/config/schedule/&lt;schedule_name&gt;/report-layout/&lt;layout-id&gt;
    
    Available methods: add
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def add(
        self,
        schedule_name: str,
        adom: str,
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        support method: add, set, get, update, delete<br>table: /report/adom/&lt;adom-name&gt;/config/schedule/&lt;schedule_name&gt;/report-layout<br>object: /report/adom/&lt;adom-name&gt;/config/schedule/&lt;schedule_name&gt;/report-layout/&lt;layout-id&gt;
        
        Args:
            schedule_name: schedule_name parameter
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/config/schedule/{schedule_name}/report-layout"
        url = url.replace("{schedule_name}", schedule_name)
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if data is not None:
            params[0]["data"] = data
        if filter is not None:
            params[0]["filter"] = filter
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

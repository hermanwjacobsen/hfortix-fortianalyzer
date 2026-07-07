"""
FortiAnalyzer API endpoint: report.adom.config.chart.drill-down-table

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomConfigChartDrillDownTable:
    """
    FortiAnalyzer endpoint: report.adom.config.chart.drill-down-table
    
    support method: add, set, get, update, delete<br>table: /report/config/chart/&lt;chart_name&gt;/drill-down-table<br>object: /report/config/chart/&lt;chart_name&gt;/drill-down-table/&lt;table-id&gt;
    
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
        chart_name: str,
        adom: str,
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        support method: add, set, get, update, delete<br>table: /report/config/chart/&lt;chart_name&gt;/drill-down-table<br>object: /report/config/chart/&lt;chart_name&gt;/drill-down-table/&lt;table-id&gt;
        
        Args:
            chart_name: chart_name parameter
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/config/chart/{chart_name}/drill-down-table"
        url = url.replace("{chart_name}", chart_name)
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

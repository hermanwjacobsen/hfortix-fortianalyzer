"""
FortiAnalyzer API endpoint: report.adom.reports.data

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomReportsData:
    """
    FortiAnalyzer endpoint: report.adom.reports.data
    
    Delete a generated report.
    
    Available methods: delete, get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def delete(
        self,
        tid: str,
        adom: str,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Delete a generated report.
        
        Args:
            tid: tid parameter
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/reports/data/{tid}"
        url = url.replace("{tid}", tid)
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def get(
        self,
        tid: str,
        adom: str,
        apiver: int = 3,
        data_type: str | None = None,
        format: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Delete a generated report.
        
        Args:
            tid: tid parameter
            adom: adom path parameter.
            apiver: Current API version.
            data_type: One option to download the text format of XML or CSV reports, e.g. 'text'.
            format: One format got by /report/adom/&lt;adom-name&gt;/reports/state. Such as HTML, PDF, XML, CSV.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/reports/data/{tid}"
        url = url.replace("{tid}", tid)
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if data_type is not None:
            request_params["data-type"] = data_type
        if format is not None:
            request_params["format"] = format
        
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

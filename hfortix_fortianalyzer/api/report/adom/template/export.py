"""
FortiAnalyzer API endpoint: report.adom.template.export

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomTemplateExport:
    """
    FortiAnalyzer endpoint: report.adom.template.export
    
    Request of exporting report templates to file.
    
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
        dev_type: str | None = None,
        language: str | None = None,
        title: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Request of exporting report templates to file.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            dev_type: Device type abbreviation, e.g. 'fgt', 'fml' etc.
            language: Language name, e.g. 'en', 'zh', 'ja' etc, filter for exporting report template.
            title: Template title, filter for exporting report template.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/template/export"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if dev_type is not None:
            request_params["dev-type"] = dev_type
        if language is not None:
            request_params["language"] = language
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

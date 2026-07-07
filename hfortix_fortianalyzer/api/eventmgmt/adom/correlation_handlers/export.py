"""
FortiAnalyzer API endpoint: eventmgmt.adom.correlation-handlers.export

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomCorrelationHandlersExport:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.correlation-handlers.export
    
    Request of exporting correlation handlers.
    
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
        attachment: list[str] | None = None,
        data_format: Literal["zip", "txt", "cli"] | None = None,
        filter: list[str] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Request of exporting correlation handlers.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            attachment: Objects that will be exported with correlation handlers.
            data_format: The format of the exporting data.
            filter: A filter for selecting exporting correlation handlers. <a href="objects.htm#filter">Filter Refrence</a>
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/correlation-handlers/export"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if attachment is not None:
            request_params["attachment"] = attachment
        if data_format is not None:
            request_params["data-format"] = data_format
        if filter is not None:
            request_params["filter"] = filter
        
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

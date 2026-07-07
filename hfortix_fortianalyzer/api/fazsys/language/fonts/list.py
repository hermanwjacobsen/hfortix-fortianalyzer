"""
FortiAnalyzer API endpoint: fazsys.language.fonts.list

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysLanguageFontsList:
    """
    FortiAnalyzer endpoint: fazsys.language.fonts.list
    
    Get system fonts list.
    
    Available methods: get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self, apiver: int = 3, font: list[str] | None = None) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get system fonts list.
        
        Args:
            apiver: Current API version.
            font: Font name, e.g. 'UnBatang', 'Open Sans', etc, filter for exporting font file.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/fazsys/language/fonts/list"
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if font is not None:
            request_params["font"] = font
        
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

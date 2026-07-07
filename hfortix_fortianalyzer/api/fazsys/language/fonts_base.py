"""
FortiAnalyzer API endpoint: fazsys.language.fonts

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysLanguageFonts:
    """
    FortiAnalyzer endpoint: fazsys.language.fonts
    
    Delete font.
    
    Available methods: delete
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def delete(self, font_name: str, apiver: int = 3) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Delete font.
        
        Args:
            font_name: font-name parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/fazsys/language/fonts/{font-name}"
        url = url.replace("{font-name}", font_name)
        
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

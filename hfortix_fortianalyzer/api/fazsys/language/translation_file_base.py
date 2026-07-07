"""
FortiAnalyzer API endpoint: fazsys.language.translation-file

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysLanguageTranslationFile:
    """
    FortiAnalyzer endpoint: fazsys.language.translation-file
    
    Delete language translation file.
    
    Available methods: delete
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def delete(self, language_code: str, apiver: int = 3) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Delete language translation file.
        
        Args:
            language_code: language-code parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/fazsys/language/translation-file/{language-code}"
        url = url.replace("{language-code}", language_code)
        
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

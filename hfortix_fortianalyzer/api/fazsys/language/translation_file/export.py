"""
FortiAnalyzer API endpoint: fazsys.language.translation-file.export

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysLanguageTranslationFileExport:
    """
    FortiAnalyzer endpoint: fazsys.language.translation-file.export
    
    Request of exporting language translation file.
    
    Available methods: get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self, apiver: int = 3, language: list[str] | None = None) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Request of exporting language translation file.
        
        Args:
            apiver: Current API version.
            language: Language code list, e.g. 'en', 'zh', 'ja' etc, filter for exporting language translation file.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/fazsys/language/translation-file/export"
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if language is not None:
            request_params["language"] = language
        
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

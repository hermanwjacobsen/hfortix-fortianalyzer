"""
FortiAnalyzer API endpoint: logview.pcapfile

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewPcapfile:
    """
    FortiAnalyzer endpoint: logview.pcapfile
    
    Get the pcapfile associated with a log.
    
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
        key_data: str,
        key_type: Literal["log-data", "pcapurl"],
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get the pcapfile associated with a log.
        
        Args:
            apiver: Current API version.
            key_data: The key for searching pcapfile. It supports three type of data: 1) JSON format log , 2) txt format log and 3) pcapurl. A pcapurl can be found in the logsearch result if the log does have an associated pcapfile. e.g. 'pcapfile?ZGV2aWQ9IkZHMjAwRTRRMTc5MTYwNTkiIHZkPSJyb290IiBzdWJ0eXBlPSJhcHAtY3RybCIgY2hlY2tzdW09IiIgZXBvY2g9MCBpbmNpZGVudHNlcmlhbG5vPTM4NjE4Mzg5OSBzZXJ2aWNlPSJTU0wiIHR5cGU9InV0bSIgZXZlbnRpZD0wIGluZGVudGlkeD0wIGZpbGVwYXRoPSIvaXBzX2ZpbGVzL0ZHMjAwRTRRMTc5MTYwNTkvcm9vdC8xNjM0ODUxNTU0LzM4NjE4Mzg5OTowIg==\\'. For more details, please click 'Show examples...' .
            key_type: The type of the given key-data.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/logview/pcapfile"
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if key_data is not None:
            request_params["key-data"] = key_data
        if key_type is not None:
            request_params["key-type"] = key_type
        
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

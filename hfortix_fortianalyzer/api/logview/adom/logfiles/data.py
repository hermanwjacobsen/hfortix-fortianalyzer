"""
FortiAnalyzer API endpoint: logview.adom.logfiles.data

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogfilesData:
    """
    FortiAnalyzer endpoint: logview.adom.logfiles.data
    
    Get the content of the specified log file.
    
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
        devid: str,
        filename: str,
        vdom: str,
        apiver: int = 3,
        data_type: Literal["base64", "csv/gzip/base64", "text/gzip/base64"] | None = None,
        length: float | None = None,
        offset: float | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get the content of the specified log file.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            data_type: The type of return data, e.g. 'text/gzip/base64'.
            devid: ID of the device hosting the logfile.
            filename: Name of the file.
            length: Length in byte of the file content to return. Default is 1MB, the maximum is 50MB.
            offset: Offset bytes from the beginning of the file.
            vdom: Name of the VDOM. If left empty, all VDOM under the <devid> will be considered.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/logview/adom/{adom}/logfiles/data"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if data_type is not None:
            request_params["data-type"] = data_type
        if devid is not None:
            request_params["devid"] = devid
        if filename is not None:
            request_params["filename"] = filename
        if length is not None:
            request_params["length"] = length
        if offset is not None:
            request_params["offset"] = offset
        if vdom is not None:
            request_params["vdom"] = vdom
        
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

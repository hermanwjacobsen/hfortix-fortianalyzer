"""
FortiAnalyzer API endpoint: logview.adom.logstats

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogstats:
    """
    FortiAnalyzer endpoint: logview.adom.logstats
    
    the last log time and log rate per device[vdom].
    
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
        device: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        the last log time and log rate per device[vdom].
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            device: Device filter. For all devices in some type please use the All-Device ID. <b><i>See Appendix</i></b>
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/logview/adom/{adom}/logstats"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if device is not None:
            request_params["device"] = device
        
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

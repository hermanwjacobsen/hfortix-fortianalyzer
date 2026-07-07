"""
FortiAnalyzer API endpoint: logview.adom.logfields

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogfields:
    """
    FortiAnalyzer endpoint: logview.adom.logfields
    
    Get all log fields.
    
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
        devtype: str | None = None,
        logtype: Literal["traffic", "app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "history", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "waf", "gtp", "ztna", "security"] | None = None,
        subtype: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get all log fields.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            devtype: Device type name, such as FortiGate, FortiClient, FortiMail, FortiWeb, FortiSandbox, FortiDDos, FortiDeceptor, FortiADC, FortiFirewall
            logtype: Logtype names
            subtype: Subtype names.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/logview/adom/{adom}/logfields"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if devtype is not None:
            request_params["devtype"] = devtype
        if logtype is not None:
            request_params["logtype"] = logtype
        if subtype is not None:
            request_params["subtype"] = subtype
        
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

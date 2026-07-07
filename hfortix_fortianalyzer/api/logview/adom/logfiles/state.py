"""
FortiAnalyzer API endpoint: logview.adom.logfiles.state

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogfilesState:
    """
    FortiAnalyzer endpoint: logview.adom.logfiles.state
    
    Get file state of log file(s).
    
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
        devid: Literal["device-id", "All_FortiGate", "All_FortiMail", "All_FortiWeb", "All_FortiManager", "All_Syslog", "All_FortiClient", "All_FortiCache", "All_FortiProxy", "All_FortiAnalyzer", "All_FortiSandbox", "All_FortiAuthenticator", "All_FortiDDoS"] | None = None,
        filename: str | None = None,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None,
        vdom: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get file state of log file(s).
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            devid: ID of the device. If left empty, all devices under the <adom-name> will be considered. See Appendix for available options
            filename: name of the file. If left empty, all files under the <vdom> will be considered
            time_range: Time range for data selection.
            timezone: The timezone index or name. Time range in request and date/time if any in response will follow this timezone. See Appendix
            vdom: Name of the VDOM. If left empty, all VDOM under the <devid> will be considered.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/logview/adom/{adom}/logfiles/state"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if devid is not None:
            request_params["devid"] = devid
        if filename is not None:
            request_params["filename"] = filename
        if time_range is not None:
            request_params["time-range"] = time_range
        if timezone is not None:
            request_params["timezone"] = timezone
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

"""
FortiAnalyzer API endpoint: logview.adom.logfiles.search

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogfilesSearch:
    """
    FortiAnalyzer endpoint: logview.adom.logfiles.search
    
    Run a log search task on a single log file.
    
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
        logtype: Literal["traffic", "app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "history", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "waf", "gtp"],
        vdom: str,
        apiver: int = 3,
        case_sensitive: bool | None = None,
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Run a log search task on a single log file.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            case_sensitive: Case sensitivty.
            devid: ID of the device hosting the logfile.
            filename: File name to search.
            filter: Filter to apply.
            limit: Maximum number of log records to fetch.
            logtype: Name of the logtype.
            offset: Offset number of log records from the beginning of the log file.
            vdom: Name of the VDOM hosting the logfile.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/logview/adom/{adom}/logfiles/search"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if case_sensitive is not None:
            request_params["case-sensitive"] = case_sensitive
        if devid is not None:
            request_params["devid"] = devid
        if filename is not None:
            request_params["filename"] = filename
        if filter is not None:
            request_params["filter"] = filter
        if limit is not None:
            request_params["limit"] = limit
        if logtype is not None:
            request_params["logtype"] = logtype
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

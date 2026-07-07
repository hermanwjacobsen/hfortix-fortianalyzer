"""
FortiAnalyzer API endpoint: logview.adom.logsearch

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogsearch:
    """
    FortiAnalyzer endpoint: logview.adom.logsearch
    
    Start a new task to search logs.
    
    Available methods: add, delete, get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def add(
        self,
        adom: str,
        device: list[dict[str, Any]],
        logtype: Literal["traffic", "app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "history", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "waf", "gtp"],
        time_range: dict[str, Any],
        tid: int | str | None = None,
        apiver: int = 3,
        case_sensitive: bool | None = None,
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None,
        time_order: Literal["desc", "asc"] | None = None,
        timezone: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Start a new task to search logs.
        
        Args:
            adom: adom path parameter.
            tid: tid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/logview/adom/{adom}/logsearch"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "device": device,
            "logtype": logtype,
            "time-range": time_range
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if case_sensitive is not None:
            params[0]["case-sensitive"] = case_sensitive
        if filter is not None:
            params[0]["filter"] = filter
        if limit is not None:
            params[0]["limit"] = limit
        if offset is not None:
            params[0]["offset"] = offset
        if time_order is not None:
            params[0]["time-order"] = time_order
        if timezone is not None:
            params[0]["timezone"] = timezone
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Start a new task to search logs.
        
        Args:
            adom: adom path parameter.
            tid: tid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and tid is not None:
            url = "/logview/adom/{adom}/logsearch/{tid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{tid}", str(tid))
        else:
            url = "/logview/adom/{adom}/logsearch"
            url = url.replace("{adom}", adom)
        
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

    def get(
        self,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3,
        limit: float | None = None,
        offset: float | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Start a new task to search logs.
        
        Args:
            adom: adom path parameter.
            tid: tid parameter
            apiver: Current API version.
            limit: Number of records to return.
            offset: Number of records to offset.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and tid is not None:
            url = "/logview/adom/{adom}/logsearch/{tid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{tid}", str(tid))
        else:
            url = "/logview/adom/{adom}/logsearch"
            url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if limit is not None:
            request_params["limit"] = limit
        if offset is not None:
            request_params["offset"] = offset
        
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

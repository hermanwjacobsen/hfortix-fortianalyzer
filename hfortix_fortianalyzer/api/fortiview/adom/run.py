"""
FortiAnalyzer API endpoint: fortiview.adom.run

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FortiviewAdomRun:
    """
    FortiAnalyzer endpoint: fortiview.adom.run
    
    Run a FortiView new task.
    
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
        view_name: str,
        adom: str,
        time_range: dict[str, Any],
        tid: int | str | None = None,
        apiver: int = 3,
        count_total: bool | None = None,
        device: list[dict[str, Any]] | None = None,
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None,
        sort_by: list[dict[str, Any]] | None = None,
        timezone: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Run a FortiView new task.
        
        Args:
            view_name: view-name parameter
            adom: adom path parameter.
            tid: tid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/fortiview/adom/{adom}/{view-name}/run"
        url = url.replace("{view-name}", view_name)
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "time-range": time_range
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if count_total is not None:
            params[0]["count-total"] = count_total
        if device is not None:
            params[0]["device"] = device
        if filter is not None:
            params[0]["filter"] = filter
        if limit is not None:
            params[0]["limit"] = limit
        if offset is not None:
            params[0]["offset"] = offset
        if sort_by is not None:
            params[0]["sort-by"] = sort_by
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
        view_name: str,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Run a FortiView new task.
        
        Args:
            view_name: view-name parameter
            adom: adom path parameter.
            tid: tid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if view_name is not None and adom is not None and tid is not None:
            url = "/fortiview/adom/{adom}/{view-name}/run/{tid}"
            url = url.replace("{view-name}", view_name)
            url = url.replace("{adom}", adom)
            url = url.replace("{tid}", str(tid))
        else:
            url = "/fortiview/adom/{adom}/{view-name}/run"
            url = url.replace("{view-name}", view_name)
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
        view_name: str,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Run a FortiView new task.
        
        Args:
            view_name: view-name parameter
            adom: adom path parameter.
            tid: tid parameter
            apiver: Current API version.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if view_name is not None and adom is not None and tid is not None:
            url = "/fortiview/adom/{adom}/{view-name}/run/{tid}"
            url = url.replace("{view-name}", view_name)
            url = url.replace("{adom}", adom)
            url = url.replace("{tid}", str(tid))
        else:
            url = "/fortiview/adom/{adom}/{view-name}/run"
            url = url.replace("{view-name}", view_name)
            url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        
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

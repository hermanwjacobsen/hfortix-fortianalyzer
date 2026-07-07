"""
FortiAnalyzer API endpoint: report.adom.run

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomRun:
    """
    FortiAnalyzer endpoint: report.adom.run
    
    Start a task to run a report.
    
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
        tid: int | str | None = None,
        apiver: int = 3,
        schedule: str | None = None,
        schedule_param: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Start a task to run a report.
        
        Args:
            adom: adom path parameter.
            tid: tid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/run"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if schedule is not None:
            params[0]["schedule"] = schedule
        if schedule_param is not None:
            params[0]["schedule-param"] = schedule_param
        
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
        
        Start a task to run a report.
        
        Args:
            adom: adom path parameter.
            tid: tid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and tid is not None:
            url = "/report/adom/{adom}/run/{tid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{tid}", str(tid))
        else:
            url = "/report/adom/{adom}/run"
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
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Start a task to run a report.
        
        Args:
            adom: adom path parameter.
            tid: tid parameter
            apiver: Current API version.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and tid is not None:
            url = "/report/adom/{adom}/run/{tid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{tid}", str(tid))
        else:
            url = "/report/adom/{adom}/run"
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

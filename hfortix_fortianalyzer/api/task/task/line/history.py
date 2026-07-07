"""
FortiAnalyzer API endpoint: task.task.line.history

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class TaskTaskLineHistory:
    """
    FortiAnalyzer endpoint: task.task.line.history
    
    
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
        task: str,
        line: str,
        history: int | str | None = None,
        fields: list[Literal["detail", "name", "percent", "state", "vdom"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            task: task parameter
            line: line parameter
            history: history parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
            range: Limit the number of output. For a range of [a, n], the output will contain <i>n</i> elements, starting from the <i>a<sup>th</sup></i> matching result.
            sortings: Specify the sorting of the returned result.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if task is not None and line is not None and history is not None:
            url = "/task/task/{task}/line/{line}/history/{history}"
            url = url.replace("{task}", task)
            url = url.replace("{line}", line)
            url = url.replace("{history}", str(history))
        else:
            url = "/task/task/{task}/line/{line}/history"
            url = url.replace("{task}", task)
            url = url.replace("{line}", line)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        if fields is not None and fields and not isinstance(fields[0], list):
            fields = [fields]
        
        request_params = {}
        if fields is not None:
            request_params["fields"] = fields
        if filter is not None:
            request_params["filter"] = filter
        if loadsub is not None:
            request_params["loadsub"] = loadsub
        if option is not None:
            request_params["option"] = option
        if range is not None:
            request_params["range"] = range
        if sortings is not None:
            request_params["sortings"] = sortings
        
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

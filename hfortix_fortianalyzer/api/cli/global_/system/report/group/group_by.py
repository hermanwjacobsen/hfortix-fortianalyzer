"""
FortiAnalyzer API endpoint: cli.global.system.report.group.group-by

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemReportGroupGroupBy:
    """
    FortiAnalyzer endpoint: cli.global.system.report.group.group-by
    
    
    Available methods: get, add, set, update, delete
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
        group: str,
        group_by: int | str | None = None,
        fields: list[Literal["var-expression", "var-name", "var-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            group: group parameter
            group_by: group-by parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None and group_by is not None:
            url = "/cli/global/system/report/group/{group}/group-by/{group-by}"
            url = url.replace("{group}", group)
            url = url.replace("{group-by}", str(group_by))
        else:
            url = "/cli/global/system/report/group/{group}/group-by"
            url = url.replace("{group}", group)
        
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

    def add(
        self,
        group: str,
        group_by: int | str | None = None,
        var_type: Literal["integer", "string", "enum", "ip"] | None = None,
        var_expression: str | None = None,
        var_name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            group: group parameter
            group_by: group-by parameter
            var_expression: var-expression parameter
            var_name: var-name parameter
            var_type: var-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/report/group/{group}/group-by"
        url = url.replace("{group}", group)
        
        # Build data payload
        data = {}
        if var_expression is not None:
            data["var-expression"] = var_expression
        if var_name is not None:
            data["var-name"] = var_name
        if var_type is not None:
            data["var-type"] = var_type
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        group: str,
        group_by: int | str | None = None,
        var_type: Literal["integer", "string", "enum", "ip"] | None = None,
        var_expression: str | None = None,
        var_name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            group: group parameter
            group_by: group-by parameter
            var_expression: var-expression parameter
            var_name: var-name parameter
            var_type: var-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None and group_by is not None:
            url = "/cli/global/system/report/group/{group}/group-by/{group-by}"
            url = url.replace("{group}", group)
            url = url.replace("{group-by}", str(group_by))
        else:
            url = "/cli/global/system/report/group/{group}/group-by"
            url = url.replace("{group}", group)
        
        # Build data payload
        data = {}
        if var_expression is not None:
            data["var-expression"] = var_expression
        if var_name is not None:
            data["var-name"] = var_name
        if var_type is not None:
            data["var-type"] = var_type
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def update(
        self,
        group: str,
        group_by: int | str | None = None,
        var_type: Literal["integer", "string", "enum", "ip"] | None = None,
        var_expression: str | None = None,
        var_name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            group: group parameter
            group_by: group-by parameter
            var_expression: var-expression parameter
            var_name: var-name parameter
            var_type: var-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None and group_by is not None:
            url = "/cli/global/system/report/group/{group}/group-by/{group-by}"
            url = url.replace("{group}", group)
            url = url.replace("{group-by}", str(group_by))
        else:
            url = "/cli/global/system/report/group/{group}/group-by"
            url = url.replace("{group}", group)
        
        # Build data payload
        data = {}
        if var_expression is not None:
            data["var-expression"] = var_expression
        if var_name is not None:
            data["var-name"] = var_name
        if var_type is not None:
            data["var-type"] = var_type
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(self, group: str, group_by: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            group: group parameter
            group_by: group-by parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None and group_by is not None:
            url = "/cli/global/system/report/group/{group}/group-by/{group-by}"
            url = url.replace("{group}", group)
            url = url.replace("{group-by}", str(group_by))
        else:
            url = "/cli/global/system/report/group/{group}/group-by"
            url = url.replace("{group}", group)
        
        data = {}
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

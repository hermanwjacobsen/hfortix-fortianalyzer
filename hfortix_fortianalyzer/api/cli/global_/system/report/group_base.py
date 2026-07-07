"""
FortiAnalyzer API endpoint: cli.global.system.report.group

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemReportGroup:
    """
    FortiAnalyzer endpoint: cli.global.system.report.group
    
    
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
        group: int | str | None = None,
        fields: list[Literal["adom", "case-insensitive", "group-id", "report-like"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            group: group parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None:
            url = "/cli/global/system/report/group/{group}"
            url = url.replace("{group}", str(group))
        else:
            url = "/cli/global/system/report/group"
        
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
        group: int | str | None = None,
        case_insensitive: Literal["disable", "enable"] | None = None,
        group_id: int | None = None,
        adom: str | None = None,
        chart_alternative: list[Any] | None = None,
        group_by: list[Any] | None = None,
        report_like: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            group: group parameter
            adom: adom parameter
            case_insensitive: case-insensitive parameter
            chart_alternative: chart-alternative parameter
            group_by: group-by parameter
            group_id: group-id parameter
            report_like: report-like parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/report/group"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if case_insensitive is not None:
            data["case-insensitive"] = case_insensitive
        if chart_alternative is not None:
            data["chart-alternative"] = chart_alternative
        if group_by is not None:
            data["group-by"] = group_by
        if group_id is not None:
            data["group-id"] = group_id
        if report_like is not None:
            data["report-like"] = report_like
        
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
        group: int | str | None = None,
        case_insensitive: Literal["disable", "enable"] | None = None,
        group_id: int | None = None,
        adom: str | None = None,
        chart_alternative: list[Any] | None = None,
        group_by: list[Any] | None = None,
        report_like: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            group: group parameter
            adom: adom parameter
            case_insensitive: case-insensitive parameter
            chart_alternative: chart-alternative parameter
            group_by: group-by parameter
            group_id: group-id parameter
            report_like: report-like parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None:
            url = "/cli/global/system/report/group/{group}"
            url = url.replace("{group}", str(group))
        else:
            url = "/cli/global/system/report/group"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if case_insensitive is not None:
            data["case-insensitive"] = case_insensitive
        if chart_alternative is not None:
            data["chart-alternative"] = chart_alternative
        if group_by is not None:
            data["group-by"] = group_by
        if group_id is not None:
            data["group-id"] = group_id
        if report_like is not None:
            data["report-like"] = report_like
        
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
        group: int | str | None = None,
        case_insensitive: Literal["disable", "enable"] | None = None,
        group_id: int | None = None,
        adom: str | None = None,
        chart_alternative: list[Any] | None = None,
        group_by: list[Any] | None = None,
        report_like: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            group: group parameter
            adom: adom parameter
            case_insensitive: case-insensitive parameter
            chart_alternative: chart-alternative parameter
            group_by: group-by parameter
            group_id: group-id parameter
            report_like: report-like parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None:
            url = "/cli/global/system/report/group/{group}"
            url = url.replace("{group}", str(group))
        else:
            url = "/cli/global/system/report/group"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if case_insensitive is not None:
            data["case-insensitive"] = case_insensitive
        if chart_alternative is not None:
            data["chart-alternative"] = chart_alternative
        if group_by is not None:
            data["group-by"] = group_by
        if group_id is not None:
            data["group-id"] = group_id
        if report_like is not None:
            data["report-like"] = report_like
        
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

    def delete(self, group: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            group: group parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None:
            url = "/cli/global/system/report/group/{group}"
            url = url.replace("{group}", str(group))
        else:
            url = "/cli/global/system/report/group"
        
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

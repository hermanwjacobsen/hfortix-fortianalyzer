"""
FortiAnalyzer API endpoint: cli.global.system.snmp.community

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSnmpCommunity:
    """
    FortiAnalyzer endpoint: cli.global.system.snmp.community
    
    
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
        community: int | str | None = None,
        fields: list[Literal["events", "id", "name", "query_v1_port", "query_v1_status", "query_v2c_port", "query_v2c_status", "status", "trap_v1_rport", "trap_v1_status", "trap_v2c_rport", "trap_v2c_status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            community: community parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if community is not None:
            url = "/cli/global/system/snmp/community/{community}"
            url = url.replace("{community}", str(community))
        else:
            url = "/cli/global/system/snmp/community"
        
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
        community: int | str | None = None,
        id: int | None = None,
        query_v1_port: int | None = None,
        query_v1_status: Literal["disable", "enable"] | None = None,
        query_v2c_port: int | None = None,
        query_v2c_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_v1_rport: int | None = None,
        trap_v1_status: Literal["disable", "enable"] | None = None,
        trap_v2c_rport: int | None = None,
        trap_v2c_status: Literal["disable", "enable"] | None = None,
        events: list[Any] | None = None,
        hosts: list[Any] | None = None,
        hosts6: list[Any] | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            community: community parameter
            events: events parameter
            hosts: hosts parameter
            hosts6: hosts6 parameter
            id: id parameter
            name: name parameter
            query_v1_port: query_v1_port parameter
            query_v1_status: query_v1_status parameter
            query_v2c_port: query_v2c_port parameter
            query_v2c_status: query_v2c_status parameter
            status: status parameter
            ... (4 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/snmp/community"
        
        # Build data payload
        data = {}
        if events is not None:
            data["events"] = events
        if hosts is not None:
            data["hosts"] = hosts
        if hosts6 is not None:
            data["hosts6"] = hosts6
        if id is not None:
            data["id"] = id
        if name is not None:
            data["name"] = name
        if query_v1_port is not None:
            data["query_v1_port"] = query_v1_port
        if query_v1_status is not None:
            data["query_v1_status"] = query_v1_status
        if query_v2c_port is not None:
            data["query_v2c_port"] = query_v2c_port
        if query_v2c_status is not None:
            data["query_v2c_status"] = query_v2c_status
        if status is not None:
            data["status"] = status
        if trap_v1_rport is not None:
            data["trap_v1_rport"] = trap_v1_rport
        if trap_v1_status is not None:
            data["trap_v1_status"] = trap_v1_status
        if trap_v2c_rport is not None:
            data["trap_v2c_rport"] = trap_v2c_rport
        if trap_v2c_status is not None:
            data["trap_v2c_status"] = trap_v2c_status
        
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
        community: int | str | None = None,
        id: int | None = None,
        query_v1_port: int | None = None,
        query_v1_status: Literal["disable", "enable"] | None = None,
        query_v2c_port: int | None = None,
        query_v2c_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_v1_rport: int | None = None,
        trap_v1_status: Literal["disable", "enable"] | None = None,
        trap_v2c_rport: int | None = None,
        trap_v2c_status: Literal["disable", "enable"] | None = None,
        events: list[Any] | None = None,
        hosts: list[Any] | None = None,
        hosts6: list[Any] | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            community: community parameter
            events: events parameter
            hosts: hosts parameter
            hosts6: hosts6 parameter
            id: id parameter
            name: name parameter
            query_v1_port: query_v1_port parameter
            query_v1_status: query_v1_status parameter
            query_v2c_port: query_v2c_port parameter
            query_v2c_status: query_v2c_status parameter
            status: status parameter
            ... (4 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if community is not None:
            url = "/cli/global/system/snmp/community/{community}"
            url = url.replace("{community}", str(community))
        else:
            url = "/cli/global/system/snmp/community"
        
        # Build data payload
        data = {}
        if events is not None:
            data["events"] = events
        if hosts is not None:
            data["hosts"] = hosts
        if hosts6 is not None:
            data["hosts6"] = hosts6
        if id is not None:
            data["id"] = id
        if name is not None:
            data["name"] = name
        if query_v1_port is not None:
            data["query_v1_port"] = query_v1_port
        if query_v1_status is not None:
            data["query_v1_status"] = query_v1_status
        if query_v2c_port is not None:
            data["query_v2c_port"] = query_v2c_port
        if query_v2c_status is not None:
            data["query_v2c_status"] = query_v2c_status
        if status is not None:
            data["status"] = status
        if trap_v1_rport is not None:
            data["trap_v1_rport"] = trap_v1_rport
        if trap_v1_status is not None:
            data["trap_v1_status"] = trap_v1_status
        if trap_v2c_rport is not None:
            data["trap_v2c_rport"] = trap_v2c_rport
        if trap_v2c_status is not None:
            data["trap_v2c_status"] = trap_v2c_status
        
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
        community: int | str | None = None,
        id: int | None = None,
        query_v1_port: int | None = None,
        query_v1_status: Literal["disable", "enable"] | None = None,
        query_v2c_port: int | None = None,
        query_v2c_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_v1_rport: int | None = None,
        trap_v1_status: Literal["disable", "enable"] | None = None,
        trap_v2c_rport: int | None = None,
        trap_v2c_status: Literal["disable", "enable"] | None = None,
        events: list[Any] | None = None,
        hosts: list[Any] | None = None,
        hosts6: list[Any] | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            community: community parameter
            events: events parameter
            hosts: hosts parameter
            hosts6: hosts6 parameter
            id: id parameter
            name: name parameter
            query_v1_port: query_v1_port parameter
            query_v1_status: query_v1_status parameter
            query_v2c_port: query_v2c_port parameter
            query_v2c_status: query_v2c_status parameter
            status: status parameter
            ... (4 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if community is not None:
            url = "/cli/global/system/snmp/community/{community}"
            url = url.replace("{community}", str(community))
        else:
            url = "/cli/global/system/snmp/community"
        
        # Build data payload
        data = {}
        if events is not None:
            data["events"] = events
        if hosts is not None:
            data["hosts"] = hosts
        if hosts6 is not None:
            data["hosts6"] = hosts6
        if id is not None:
            data["id"] = id
        if name is not None:
            data["name"] = name
        if query_v1_port is not None:
            data["query_v1_port"] = query_v1_port
        if query_v1_status is not None:
            data["query_v1_status"] = query_v1_status
        if query_v2c_port is not None:
            data["query_v2c_port"] = query_v2c_port
        if query_v2c_status is not None:
            data["query_v2c_status"] = query_v2c_status
        if status is not None:
            data["status"] = status
        if trap_v1_rport is not None:
            data["trap_v1_rport"] = trap_v1_rport
        if trap_v1_status is not None:
            data["trap_v1_status"] = trap_v1_status
        if trap_v2c_rport is not None:
            data["trap_v2c_rport"] = trap_v2c_rport
        if trap_v2c_status is not None:
            data["trap_v2c_status"] = trap_v2c_status
        
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

    def delete(self, community: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            community: community parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if community is not None:
            url = "/cli/global/system/snmp/community/{community}"
            url = url.replace("{community}", str(community))
        else:
            url = "/cli/global/system/snmp/community"
        
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

"""
FortiAnalyzer API endpoint: cli.global.system.local-in-policy

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocalInPolicy:
    """
    FortiAnalyzer endpoint: cli.global.system.local-in-policy
    
    
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
        local_in_policy: int | str | None = None,
        fields: list[Literal["action", "description", "id", "protocol"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            local_in_policy: local-in-policy parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if local_in_policy is not None:
            url = "/cli/global/system/local-in-policy/{local-in-policy}"
            url = url.replace("{local-in-policy}", str(local_in_policy))
        else:
            url = "/cli/global/system/local-in-policy"
        
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
        local_in_policy: int | str | None = None,
        action: Literal["drop", "reject", "accept"] | None = None,
        id: int | None = None,
        protocol: Literal["tcp", "udp", "tcp_udp"] | None = None,
        description: str | None = None,
        dport: list[Any] | None = None,
        dst: list[Any] | None = None,
        intf: list[Any] | None = None,
        src: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            local_in_policy: local-in-policy parameter
            action: action parameter
            description: description parameter
            dport: dport parameter
            dst: dst parameter
            id: id parameter
            intf: intf parameter
            protocol: protocol parameter
            src: src parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/local-in-policy"
        
        # Build data payload
        data = {}
        if action is not None:
            data["action"] = action
        if description is not None:
            data["description"] = description
        if dport is not None:
            data["dport"] = dport
        if dst is not None:
            data["dst"] = dst
        if id is not None:
            data["id"] = id
        if intf is not None:
            data["intf"] = intf
        if protocol is not None:
            data["protocol"] = protocol
        if src is not None:
            data["src"] = src
        
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
        local_in_policy: int | str | None = None,
        action: Literal["drop", "reject", "accept"] | None = None,
        id: int | None = None,
        protocol: Literal["tcp", "udp", "tcp_udp"] | None = None,
        description: str | None = None,
        dport: list[Any] | None = None,
        dst: list[Any] | None = None,
        intf: list[Any] | None = None,
        src: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            local_in_policy: local-in-policy parameter
            action: action parameter
            description: description parameter
            dport: dport parameter
            dst: dst parameter
            id: id parameter
            intf: intf parameter
            protocol: protocol parameter
            src: src parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if local_in_policy is not None:
            url = "/cli/global/system/local-in-policy/{local-in-policy}"
            url = url.replace("{local-in-policy}", str(local_in_policy))
        else:
            url = "/cli/global/system/local-in-policy"
        
        # Build data payload
        data = {}
        if action is not None:
            data["action"] = action
        if description is not None:
            data["description"] = description
        if dport is not None:
            data["dport"] = dport
        if dst is not None:
            data["dst"] = dst
        if id is not None:
            data["id"] = id
        if intf is not None:
            data["intf"] = intf
        if protocol is not None:
            data["protocol"] = protocol
        if src is not None:
            data["src"] = src
        
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
        local_in_policy: int | str | None = None,
        action: Literal["drop", "reject", "accept"] | None = None,
        id: int | None = None,
        protocol: Literal["tcp", "udp", "tcp_udp"] | None = None,
        description: str | None = None,
        dport: list[Any] | None = None,
        dst: list[Any] | None = None,
        intf: list[Any] | None = None,
        src: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            local_in_policy: local-in-policy parameter
            action: action parameter
            description: description parameter
            dport: dport parameter
            dst: dst parameter
            id: id parameter
            intf: intf parameter
            protocol: protocol parameter
            src: src parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if local_in_policy is not None:
            url = "/cli/global/system/local-in-policy/{local-in-policy}"
            url = url.replace("{local-in-policy}", str(local_in_policy))
        else:
            url = "/cli/global/system/local-in-policy"
        
        # Build data payload
        data = {}
        if action is not None:
            data["action"] = action
        if description is not None:
            data["description"] = description
        if dport is not None:
            data["dport"] = dport
        if dst is not None:
            data["dst"] = dst
        if id is not None:
            data["id"] = id
        if intf is not None:
            data["intf"] = intf
        if protocol is not None:
            data["protocol"] = protocol
        if src is not None:
            data["src"] = src
        
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

    def delete(self, local_in_policy: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            local_in_policy: local-in-policy parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if local_in_policy is not None:
            url = "/cli/global/system/local-in-policy/{local-in-policy}"
            url = url.replace("{local-in-policy}", str(local_in_policy))
        else:
            url = "/cli/global/system/local-in-policy"
        
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

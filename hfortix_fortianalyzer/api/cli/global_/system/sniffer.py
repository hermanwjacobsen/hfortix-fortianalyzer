"""
FortiAnalyzer API endpoint: cli.global.system.sniffer

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSniffer:
    """
    FortiAnalyzer endpoint: cli.global.system.sniffer
    
    
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
        sniffer: int | str | None = None,
        fields: list[Literal["host", "id", "interface", "ipv6", "max-packet-count", "non-ip", "port", "protocol", "vlan"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            sniffer: sniffer parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if sniffer is not None:
            url = "/cli/global/system/sniffer/{sniffer}"
            url = url.replace("{sniffer}", str(sniffer))
        else:
            url = "/cli/global/system/sniffer"
        
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
        sniffer: int | str | None = None,
        id: int | None = None,
        ipv6: Literal["disable", "enable"] | None = None,
        max_packet_count: int | None = None,
        non_ip: Literal["disable", "enable"] | None = None,
        host: str | None = None,
        interface: str | None = None,
        port: str | None = None,
        protocol: str | None = None,
        vlan: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            sniffer: sniffer parameter
            host: host parameter
            id: id parameter
            interface: interface parameter
            ipv6: ipv6 parameter
            max_packet_count: max-packet-count parameter
            non_ip: non-ip parameter
            port: port parameter
            protocol: protocol parameter
            vlan: vlan parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/sniffer"
        
        # Build data payload
        data = {}
        if host is not None:
            data["host"] = host
        if id is not None:
            data["id"] = id
        if interface is not None:
            data["interface"] = interface
        if ipv6 is not None:
            data["ipv6"] = ipv6
        if max_packet_count is not None:
            data["max-packet-count"] = max_packet_count
        if non_ip is not None:
            data["non-ip"] = non_ip
        if port is not None:
            data["port"] = port
        if protocol is not None:
            data["protocol"] = protocol
        if vlan is not None:
            data["vlan"] = vlan
        
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
        sniffer: int | str | None = None,
        id: int | None = None,
        ipv6: Literal["disable", "enable"] | None = None,
        max_packet_count: int | None = None,
        non_ip: Literal["disable", "enable"] | None = None,
        host: str | None = None,
        interface: str | None = None,
        port: str | None = None,
        protocol: str | None = None,
        vlan: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            sniffer: sniffer parameter
            host: host parameter
            id: id parameter
            interface: interface parameter
            ipv6: ipv6 parameter
            max_packet_count: max-packet-count parameter
            non_ip: non-ip parameter
            port: port parameter
            protocol: protocol parameter
            vlan: vlan parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if sniffer is not None:
            url = "/cli/global/system/sniffer/{sniffer}"
            url = url.replace("{sniffer}", str(sniffer))
        else:
            url = "/cli/global/system/sniffer"
        
        # Build data payload
        data = {}
        if host is not None:
            data["host"] = host
        if id is not None:
            data["id"] = id
        if interface is not None:
            data["interface"] = interface
        if ipv6 is not None:
            data["ipv6"] = ipv6
        if max_packet_count is not None:
            data["max-packet-count"] = max_packet_count
        if non_ip is not None:
            data["non-ip"] = non_ip
        if port is not None:
            data["port"] = port
        if protocol is not None:
            data["protocol"] = protocol
        if vlan is not None:
            data["vlan"] = vlan
        
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
        sniffer: int | str | None = None,
        id: int | None = None,
        ipv6: Literal["disable", "enable"] | None = None,
        max_packet_count: int | None = None,
        non_ip: Literal["disable", "enable"] | None = None,
        host: str | None = None,
        interface: str | None = None,
        port: str | None = None,
        protocol: str | None = None,
        vlan: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            sniffer: sniffer parameter
            host: host parameter
            id: id parameter
            interface: interface parameter
            ipv6: ipv6 parameter
            max_packet_count: max-packet-count parameter
            non_ip: non-ip parameter
            port: port parameter
            protocol: protocol parameter
            vlan: vlan parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if sniffer is not None:
            url = "/cli/global/system/sniffer/{sniffer}"
            url = url.replace("{sniffer}", str(sniffer))
        else:
            url = "/cli/global/system/sniffer"
        
        # Build data payload
        data = {}
        if host is not None:
            data["host"] = host
        if id is not None:
            data["id"] = id
        if interface is not None:
            data["interface"] = interface
        if ipv6 is not None:
            data["ipv6"] = ipv6
        if max_packet_count is not None:
            data["max-packet-count"] = max_packet_count
        if non_ip is not None:
            data["non-ip"] = non_ip
        if port is not None:
            data["port"] = port
        if protocol is not None:
            data["protocol"] = protocol
        if vlan is not None:
            data["vlan"] = vlan
        
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

    def delete(self, sniffer: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            sniffer: sniffer parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if sniffer is not None:
            url = "/cli/global/system/sniffer/{sniffer}"
            url = url.replace("{sniffer}", str(sniffer))
        else:
            url = "/cli/global/system/sniffer"
        
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

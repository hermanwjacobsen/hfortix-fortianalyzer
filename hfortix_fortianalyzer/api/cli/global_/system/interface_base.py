"""
FortiAnalyzer API endpoint: cli.global.system.interface

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemInterface:
    """
    FortiAnalyzer endpoint: cli.global.system.interface
    
    
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
        interface: int | str | None = None,
        fields: list[Literal["aggregate", "alias", "allowaccess", "defaultgw", "description", "dhcp-client-identifier", "dns-server-override", "interface", "ip", "lacp-mode", "lacp-speed", "link-up-delay", "lldp", "min-links", "min-links-down", "mode", "mtu", "mtu-override", "name", "speed", "status", "type", "vlan-protocol", "vlanid"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            interface: interface parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if interface is not None:
            url = "/cli/global/system/interface/{interface}"
            url = url.replace("{interface}", str(interface))
        else:
            url = "/cli/global/system/interface"
        
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
        interface: int | str | None = None,
        defaultgw: Literal["disable", "enable"] | None = None,
        dns_server_override: Literal["disable", "enable"] | None = None,
        lacp_mode: Literal["active"] | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        link_up_delay: int | None = None,
        lldp: Literal["disable", "enable"] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        mode: Literal["static", "dhcp"] | None = None,
        mtu: int | None = None,
        mtu_override: Literal["disable", "enable"] | None = None,
        speed: Literal["auto", "10full", "100full", "1g/full", "2.5g/full", "5g/full", "10g/full", "14g/full", "20g/full", "25g/full", "40g/full", "50g/full", "56g/full", "100g/full", "200g/full", "400g/full", "1g/half", "100half", "10half"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        type: Literal["vlan", "physical", "aggregate"] | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
        aggregate: str | None = None,
        alias: str | None = None,
        allowaccess: list[Any] | None = None,
        description: str | None = None,
        dhcp_client_identifier: str | None = None,
        ip: list[Any] | None = None,
        ipv6: dict[str, Any] | None = None,
        member: list[Any] | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            interface: interface parameter
            aggregate: aggregate parameter
            alias: alias parameter
            allowaccess: allowaccess parameter
            defaultgw: defaultgw parameter
            description: description parameter
            dhcp_client_identifier: dhcp-client-identifier parameter
            dns_server_override: dns-server-override parameter
            ip: ip parameter
            ipv6: Nested object (schema: cli.system.interface.ipv6).
            lacp_mode: lacp-mode parameter
            ... (15 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/interface"
        
        # Build data payload
        data = {}
        if aggregate is not None:
            data["aggregate"] = aggregate
        if alias is not None:
            data["alias"] = alias
        if allowaccess is not None:
            data["allowaccess"] = allowaccess
        if defaultgw is not None:
            data["defaultgw"] = defaultgw
        if description is not None:
            data["description"] = description
        if dhcp_client_identifier is not None:
            data["dhcp-client-identifier"] = dhcp_client_identifier
        if dns_server_override is not None:
            data["dns-server-override"] = dns_server_override
        if interface is not None:
            data["interface"] = interface
        if ip is not None:
            data["ip"] = ip
        if ipv6 is not None:
            data["ipv6"] = ipv6
        if lacp_mode is not None:
            data["lacp-mode"] = lacp_mode
        if lacp_speed is not None:
            data["lacp-speed"] = lacp_speed
        if link_up_delay is not None:
            data["link-up-delay"] = link_up_delay
        if lldp is not None:
            data["lldp"] = lldp
        if member is not None:
            data["member"] = member
        if min_links is not None:
            data["min-links"] = min_links
        if min_links_down is not None:
            data["min-links-down"] = min_links_down
        if mode is not None:
            data["mode"] = mode
        if mtu is not None:
            data["mtu"] = mtu
        if mtu_override is not None:
            data["mtu-override"] = mtu_override
        if name is not None:
            data["name"] = name
        if speed is not None:
            data["speed"] = speed
        if status is not None:
            data["status"] = status
        if type is not None:
            data["type"] = type
        if vlan_protocol is not None:
            data["vlan-protocol"] = vlan_protocol
        if vlanid is not None:
            data["vlanid"] = vlanid
        
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
        interface: int | str | None = None,
        defaultgw: Literal["disable", "enable"] | None = None,
        dns_server_override: Literal["disable", "enable"] | None = None,
        lacp_mode: Literal["active"] | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        link_up_delay: int | None = None,
        lldp: Literal["disable", "enable"] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        mode: Literal["static", "dhcp"] | None = None,
        mtu: int | None = None,
        mtu_override: Literal["disable", "enable"] | None = None,
        speed: Literal["auto", "10full", "100full", "1g/full", "2.5g/full", "5g/full", "10g/full", "14g/full", "20g/full", "25g/full", "40g/full", "50g/full", "56g/full", "100g/full", "200g/full", "400g/full", "1g/half", "100half", "10half"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        type: Literal["vlan", "physical", "aggregate"] | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
        aggregate: str | None = None,
        alias: str | None = None,
        allowaccess: list[Any] | None = None,
        description: str | None = None,
        dhcp_client_identifier: str | None = None,
        ip: list[Any] | None = None,
        ipv6: dict[str, Any] | None = None,
        member: list[Any] | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            interface: interface parameter
            aggregate: aggregate parameter
            alias: alias parameter
            allowaccess: allowaccess parameter
            defaultgw: defaultgw parameter
            description: description parameter
            dhcp_client_identifier: dhcp-client-identifier parameter
            dns_server_override: dns-server-override parameter
            ip: ip parameter
            ipv6: Nested object (schema: cli.system.interface.ipv6).
            lacp_mode: lacp-mode parameter
            ... (15 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if interface is not None:
            url = "/cli/global/system/interface/{interface}"
            url = url.replace("{interface}", str(interface))
        else:
            url = "/cli/global/system/interface"
        
        # Build data payload
        data = {}
        if aggregate is not None:
            data["aggregate"] = aggregate
        if alias is not None:
            data["alias"] = alias
        if allowaccess is not None:
            data["allowaccess"] = allowaccess
        if defaultgw is not None:
            data["defaultgw"] = defaultgw
        if description is not None:
            data["description"] = description
        if dhcp_client_identifier is not None:
            data["dhcp-client-identifier"] = dhcp_client_identifier
        if dns_server_override is not None:
            data["dns-server-override"] = dns_server_override
        if ip is not None:
            data["ip"] = ip
        if ipv6 is not None:
            data["ipv6"] = ipv6
        if lacp_mode is not None:
            data["lacp-mode"] = lacp_mode
        if lacp_speed is not None:
            data["lacp-speed"] = lacp_speed
        if link_up_delay is not None:
            data["link-up-delay"] = link_up_delay
        if lldp is not None:
            data["lldp"] = lldp
        if member is not None:
            data["member"] = member
        if min_links is not None:
            data["min-links"] = min_links
        if min_links_down is not None:
            data["min-links-down"] = min_links_down
        if mode is not None:
            data["mode"] = mode
        if mtu is not None:
            data["mtu"] = mtu
        if mtu_override is not None:
            data["mtu-override"] = mtu_override
        if name is not None:
            data["name"] = name
        if speed is not None:
            data["speed"] = speed
        if status is not None:
            data["status"] = status
        if type is not None:
            data["type"] = type
        if vlan_protocol is not None:
            data["vlan-protocol"] = vlan_protocol
        if vlanid is not None:
            data["vlanid"] = vlanid
        
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
        interface: int | str | None = None,
        defaultgw: Literal["disable", "enable"] | None = None,
        dns_server_override: Literal["disable", "enable"] | None = None,
        lacp_mode: Literal["active"] | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        link_up_delay: int | None = None,
        lldp: Literal["disable", "enable"] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        mode: Literal["static", "dhcp"] | None = None,
        mtu: int | None = None,
        mtu_override: Literal["disable", "enable"] | None = None,
        speed: Literal["auto", "10full", "100full", "1g/full", "2.5g/full", "5g/full", "10g/full", "14g/full", "20g/full", "25g/full", "40g/full", "50g/full", "56g/full", "100g/full", "200g/full", "400g/full", "1g/half", "100half", "10half"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        type: Literal["vlan", "physical", "aggregate"] | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
        aggregate: str | None = None,
        alias: str | None = None,
        allowaccess: list[Any] | None = None,
        description: str | None = None,
        dhcp_client_identifier: str | None = None,
        ip: list[Any] | None = None,
        ipv6: dict[str, Any] | None = None,
        member: list[Any] | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            interface: interface parameter
            aggregate: aggregate parameter
            alias: alias parameter
            allowaccess: allowaccess parameter
            defaultgw: defaultgw parameter
            description: description parameter
            dhcp_client_identifier: dhcp-client-identifier parameter
            dns_server_override: dns-server-override parameter
            ip: ip parameter
            ipv6: Nested object (schema: cli.system.interface.ipv6).
            lacp_mode: lacp-mode parameter
            ... (15 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if interface is not None:
            url = "/cli/global/system/interface/{interface}"
            url = url.replace("{interface}", str(interface))
        else:
            url = "/cli/global/system/interface"
        
        # Build data payload
        data = {}
        if aggregate is not None:
            data["aggregate"] = aggregate
        if alias is not None:
            data["alias"] = alias
        if allowaccess is not None:
            data["allowaccess"] = allowaccess
        if defaultgw is not None:
            data["defaultgw"] = defaultgw
        if description is not None:
            data["description"] = description
        if dhcp_client_identifier is not None:
            data["dhcp-client-identifier"] = dhcp_client_identifier
        if dns_server_override is not None:
            data["dns-server-override"] = dns_server_override
        if ip is not None:
            data["ip"] = ip
        if ipv6 is not None:
            data["ipv6"] = ipv6
        if lacp_mode is not None:
            data["lacp-mode"] = lacp_mode
        if lacp_speed is not None:
            data["lacp-speed"] = lacp_speed
        if link_up_delay is not None:
            data["link-up-delay"] = link_up_delay
        if lldp is not None:
            data["lldp"] = lldp
        if member is not None:
            data["member"] = member
        if min_links is not None:
            data["min-links"] = min_links
        if min_links_down is not None:
            data["min-links-down"] = min_links_down
        if mode is not None:
            data["mode"] = mode
        if mtu is not None:
            data["mtu"] = mtu
        if mtu_override is not None:
            data["mtu-override"] = mtu_override
        if name is not None:
            data["name"] = name
        if speed is not None:
            data["speed"] = speed
        if status is not None:
            data["status"] = status
        if type is not None:
            data["type"] = type
        if vlan_protocol is not None:
            data["vlan-protocol"] = vlan_protocol
        if vlanid is not None:
            data["vlanid"] = vlanid
        
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

    def delete(self, interface: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            interface: interface parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if interface is not None:
            url = "/cli/global/system/interface/{interface}"
            url = url.replace("{interface}", str(interface))
        else:
            url = "/cli/global/system/interface"
        
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

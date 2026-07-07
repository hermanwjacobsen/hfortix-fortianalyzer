"""Type stubs for cli.global.system.interface"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemInterfaceGetItem:
    """Item yielded when iterating over CliGlobalSystemInterfaceGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def aggregate(self) -> str: ...
    @property
    def alias(self) -> str: ...
    @property
    def allowaccess(self) -> list[Any]: ...
    @property
    def defaultgw(self) -> Literal["disable", "enable"]: ...
    @property
    def description(self) -> str: ...
    @property
    def dhcp_client_identifier(self) -> str: ...
    @property
    def dns_server_override(self) -> Literal["disable", "enable"]: ...
    @property
    def interface(self) -> str: ...
    @property
    def ip(self) -> list[Any]: ...
    @property
    def ipv6(self) -> dict[str, Any]: ...
    @property
    def lacp_mode(self) -> Literal["active"]: ...
    @property
    def lacp_speed(self) -> Literal["slow", "fast"]: ...
    @property
    def link_up_delay(self) -> int: ...
    @property
    def lldp(self) -> Literal["disable", "enable"]: ...
    @property
    def member(self) -> list[MemberItem]: ...
    @property
    def min_links(self) -> int: ...
    @property
    def min_links_down(self) -> Literal["operational", "administrative"]: ...
    @property
    def mode(self) -> Literal["static", "dhcp"]: ...
    @property
    def mtu(self) -> int: ...
    @property
    def mtu_override(self) -> Literal["disable", "enable"]: ...
    @property
    def name(self) -> str: ...
    @property
    def speed(self) -> Literal["auto", "10full", "100full", "1g/full", "2.5g/full", "5g/full", "10g/full", "14g/full", "20g/full", "25g/full", "40g/full", "50g/full", "56g/full", "100g/full", "200g/full", "400g/full", "1g/half", "100half", "10half"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def type(self) -> Literal["vlan", "physical", "aggregate"]: ...
    @property
    def vlan_protocol(self) -> Literal["8021q", "8021ad"]: ...
    @property
    def vlanid(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class MemberItem:
    """Nested item type for member array."""

    @property
    def interface_name(self) -> str: ...


class CliGlobalSystemInterfaceGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemInterfaceGet endpoint with autocomplete support."""

    # ========================================================================
    # HTTP Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def http_status_code(self) -> int | None: ...
    @property
    def http_response_time(self) -> float | None: ...
    @property
    def http_method(self) -> str | None: ...
    @property
    def http_url(self) -> str | None: ...

    # ========================================================================
    # API Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def api_status_code(self) -> int | None: ...
    @property
    def api_status_message(self) -> str | None: ...
    @property
    def api_id(self) -> int | None: ...
    @property
    def api_url(self) -> str | None: ...
    @property
    def api_raw(self) -> dict[str, Any]: ...

    # ========================================================================
    # Data Fields (specific to this endpoint)
    # ========================================================================
    @property
    def oid(self) -> int | None:
        """Object ID (dynamically added by FortiAnalyzer API, not in Swagger schema)"""
        ...

    @property
    def aggregate(self) -> str | None:
        """Field: aggregate"""
        ...

    @property
    def alias(self) -> str | None:
        """Field: alias"""
        ...

    @property
    def allowaccess(self) -> list[Any] | None:
        """Field: allowaccess"""
        ...

    @property
    def defaultgw(self) -> Literal["disable", "enable"] | None:
        """Field: defaultgw"""
        ...

    @property
    def description(self) -> str | None:
        """Field: description"""
        ...

    @property
    def dhcp_client_identifier(self) -> str | None:
        """Field: dhcp-client-identifier"""
        ...

    @property
    def dns_server_override(self) -> Literal["disable", "enable"] | None:
        """Field: dns-server-override"""
        ...

    @property
    def interface(self) -> str | None:
        """Field: interface"""
        ...

    @property
    def ip(self) -> list[Any] | None:
        """Field: ip"""
        ...

    @property
    def ipv6(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.interface.ipv6)."""
        ...

    @property
    def lacp_mode(self) -> Literal["active"] | None:
        """Field: lacp-mode"""
        ...

    @property
    def lacp_speed(self) -> Literal["slow", "fast"] | None:
        """Field: lacp-speed"""
        ...

    @property
    def link_up_delay(self) -> int | None:
        """Field: link-up-delay"""
        ...

    @property
    def lldp(self) -> Literal["disable", "enable"] | None:
        """Field: lldp"""
        ...

    @property
    def member(self) -> list[MemberItem]:
        """Field: member"""
        ...

    @property
    def min_links(self) -> int | None:
        """Field: min-links"""
        ...

    @property
    def min_links_down(self) -> Literal["operational", "administrative"] | None:
        """Field: min-links-down"""
        ...

    @property
    def mode(self) -> Literal["static", "dhcp"] | None:
        """Field: mode"""
        ...

    @property
    def mtu(self) -> int | None:
        """Field: mtu"""
        ...

    @property
    def mtu_override(self) -> Literal["disable", "enable"] | None:
        """Field: mtu-override"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def speed(self) -> Literal["auto", "10full", "100full", "1g/full", "2.5g/full", "5g/full", "10g/full", "14g/full", "20g/full", "25g/full", "40g/full", "50g/full", "56g/full", "100g/full", "200g/full", "400g/full", "1g/half", "100half", "10half"] | None:
        """Field: speed"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def type(self) -> Literal["vlan", "physical", "aggregate"] | None:
        """Field: type"""
        ...

    @property
    def vlan_protocol(self) -> Literal["8021q", "8021ad"] | None:
        """Field: vlan-protocol"""
        ...

    @property
    def vlanid(self) -> int | None:
        """Field: vlanid"""
        ...


    # Inherited methods from FortiAnalyzerResponse
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[CliGlobalSystemInterfaceGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemInterface:
    """FortiAnalyzer endpoint: cli.global.system.interface"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        interface: int | str | None = None,
        fields: list[Literal["aggregate", "alias", "allowaccess", "defaultgw", "description", "dhcp-client-identifier", "dns-server-override", "interface", "ip", "lacp-mode", "lacp-speed", "link-up-delay", "lldp", "min-links", "min-links-down", "mode", "mtu", "mtu-override", "name", "speed", "status", "type", "vlan-protocol", "vlanid"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemInterfaceGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        interface: int | str | None = None,
        aggregate: str | None = None,
        alias: str | None = None,
        allowaccess: list[Any] | None = None,
        defaultgw: Literal["disable", "enable"] | None = None,
        description: str | None = None,
        dhcp_client_identifier: str | None = None,
        dns_server_override: Literal["disable", "enable"] | None = None,
        ip: list[Any] | None = None,
        ipv6: dict[str, Any] | None = None,
        lacp_mode: Literal["active"] | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        link_up_delay: int | None = None,
        lldp: Literal["disable", "enable"] | None = None,
        member: list[dict[str, Any]] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        mode: Literal["static", "dhcp"] | None = None,
        mtu: int | None = None,
        mtu_override: Literal["disable", "enable"] | None = None,
        name: str | None = None,
        speed: Literal["auto", "10full", "100full", "1g/full", "2.5g/full", "5g/full", "10g/full", "14g/full", "20g/full", "25g/full", "40g/full", "50g/full", "56g/full", "100g/full", "200g/full", "400g/full", "1g/half", "100half", "10half"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        type: Literal["vlan", "physical", "aggregate"] | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        interface: int | str | None = None,
        aggregate: str | None = None,
        alias: str | None = None,
        allowaccess: list[Any] | None = None,
        defaultgw: Literal["disable", "enable"] | None = None,
        description: str | None = None,
        dhcp_client_identifier: str | None = None,
        dns_server_override: Literal["disable", "enable"] | None = None,
        ip: list[Any] | None = None,
        ipv6: dict[str, Any] | None = None,
        lacp_mode: Literal["active"] | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        link_up_delay: int | None = None,
        lldp: Literal["disable", "enable"] | None = None,
        member: list[dict[str, Any]] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        mode: Literal["static", "dhcp"] | None = None,
        mtu: int | None = None,
        mtu_override: Literal["disable", "enable"] | None = None,
        name: str | None = None,
        speed: Literal["auto", "10full", "100full", "1g/full", "2.5g/full", "5g/full", "10g/full", "14g/full", "20g/full", "25g/full", "40g/full", "50g/full", "56g/full", "100g/full", "200g/full", "400g/full", "1g/half", "100half", "10half"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        type: Literal["vlan", "physical", "aggregate"] | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        interface: int | str | None = None,
        aggregate: str | None = None,
        alias: str | None = None,
        allowaccess: list[Any] | None = None,
        defaultgw: Literal["disable", "enable"] | None = None,
        description: str | None = None,
        dhcp_client_identifier: str | None = None,
        dns_server_override: Literal["disable", "enable"] | None = None,
        ip: list[Any] | None = None,
        ipv6: dict[str, Any] | None = None,
        lacp_mode: Literal["active"] | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        link_up_delay: int | None = None,
        lldp: Literal["disable", "enable"] | None = None,
        member: list[dict[str, Any]] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        mode: Literal["static", "dhcp"] | None = None,
        mtu: int | None = None,
        mtu_override: Literal["disable", "enable"] | None = None,
        name: str | None = None,
        speed: Literal["auto", "10full", "100full", "1g/full", "2.5g/full", "5g/full", "10g/full", "14g/full", "20g/full", "25g/full", "40g/full", "50g/full", "56g/full", "100g/full", "200g/full", "400g/full", "1g/half", "100half", "10half"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        type: Literal["vlan", "physical", "aggregate"] | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        interface: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemInterface", "CliGlobalSystemInterfaceGetResponse"]
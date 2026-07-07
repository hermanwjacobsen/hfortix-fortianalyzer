"""Type stubs for cli.global.system.sniffer"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSnifferGetItem:
    """Item yielded when iterating over CliGlobalSystemSnifferGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def host(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def interface(self) -> str: ...
    @property
    def ipv6(self) -> Literal["disable", "enable"]: ...
    @property
    def max_packet_count(self) -> int: ...
    @property
    def non_ip(self) -> Literal["disable", "enable"]: ...
    @property
    def port(self) -> str: ...
    @property
    def protocol(self) -> str: ...
    @property
    def vlan(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemSnifferGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSnifferGet endpoint with autocomplete support."""

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
    def host(self) -> str | None:
        """Field: host"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def interface(self) -> str | None:
        """Field: interface"""
        ...

    @property
    def ipv6(self) -> Literal["disable", "enable"] | None:
        """Field: ipv6"""
        ...

    @property
    def max_packet_count(self) -> int | None:
        """Field: max-packet-count"""
        ...

    @property
    def non_ip(self) -> Literal["disable", "enable"] | None:
        """Field: non-ip"""
        ...

    @property
    def port(self) -> str | None:
        """Field: port"""
        ...

    @property
    def protocol(self) -> str | None:
        """Field: protocol"""
        ...

    @property
    def vlan(self) -> str | None:
        """Field: vlan"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSnifferGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSniffer:
    """FortiAnalyzer endpoint: cli.global.system.sniffer"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        sniffer: int | str | None = None,
        fields: list[Literal["host", "id", "interface", "ipv6", "max-packet-count", "non-ip", "port", "protocol", "vlan"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemSnifferGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        sniffer: int | str | None = None,
        host: str | None = None,
        id: int | None = None,
        interface: str | None = None,
        ipv6: Literal["disable", "enable"] | None = None,
        max_packet_count: int | None = None,
        non_ip: Literal["disable", "enable"] | None = None,
        port: str | None = None,
        protocol: str | None = None,
        vlan: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        sniffer: int | str | None = None,
        host: str | None = None,
        id: int | None = None,
        interface: str | None = None,
        ipv6: Literal["disable", "enable"] | None = None,
        max_packet_count: int | None = None,
        non_ip: Literal["disable", "enable"] | None = None,
        port: str | None = None,
        protocol: str | None = None,
        vlan: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        sniffer: int | str | None = None,
        host: str | None = None,
        id: int | None = None,
        interface: str | None = None,
        ipv6: Literal["disable", "enable"] | None = None,
        max_packet_count: int | None = None,
        non_ip: Literal["disable", "enable"] | None = None,
        port: str | None = None,
        protocol: str | None = None,
        vlan: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        sniffer: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemSniffer", "CliGlobalSystemSnifferGetResponse"]
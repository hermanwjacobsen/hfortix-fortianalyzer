"""Type stubs for cli.global.system.snmp.community"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSnmpCommunityGetItem:
    """Item yielded when iterating over CliGlobalSystemSnmpCommunityGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def events(self) -> list[Any]: ...
    @property
    def hosts(self) -> list[HostsItem]: ...
    @property
    def hosts6(self) -> list[Hosts6Item]: ...
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def query_v1_port(self) -> int: ...
    @property
    def query_v1_status(self) -> Literal["disable", "enable"]: ...
    @property
    def query_v2c_port(self) -> int: ...
    @property
    def query_v2c_status(self) -> Literal["disable", "enable"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def trap_v1_rport(self) -> int: ...
    @property
    def trap_v1_status(self) -> Literal["disable", "enable"]: ...
    @property
    def trap_v2c_rport(self) -> int: ...
    @property
    def trap_v2c_status(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class HostsItem:
    """Nested item type for hosts array."""

    @property
    def id(self) -> int: ...
    @property
    def interface(self) -> str: ...
    @property
    def ip(self) -> list[Any]: ...

class Hosts6Item:
    """Nested item type for hosts6 array."""

    @property
    def id(self) -> int: ...
    @property
    def interface(self) -> str: ...
    @property
    def ip(self) -> str: ...


class CliGlobalSystemSnmpCommunityGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSnmpCommunityGet endpoint with autocomplete support."""

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
    def events(self) -> list[Any] | None:
        """Field: events"""
        ...

    @property
    def hosts(self) -> list[HostsItem]:
        """Field: hosts"""
        ...

    @property
    def hosts6(self) -> list[Hosts6Item]:
        """Field: hosts6"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def query_v1_port(self) -> int | None:
        """Field: query_v1_port"""
        ...

    @property
    def query_v1_status(self) -> Literal["disable", "enable"] | None:
        """Field: query_v1_status"""
        ...

    @property
    def query_v2c_port(self) -> int | None:
        """Field: query_v2c_port"""
        ...

    @property
    def query_v2c_status(self) -> Literal["disable", "enable"] | None:
        """Field: query_v2c_status"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def trap_v1_rport(self) -> int | None:
        """Field: trap_v1_rport"""
        ...

    @property
    def trap_v1_status(self) -> Literal["disable", "enable"] | None:
        """Field: trap_v1_status"""
        ...

    @property
    def trap_v2c_rport(self) -> int | None:
        """Field: trap_v2c_rport"""
        ...

    @property
    def trap_v2c_status(self) -> Literal["disable", "enable"] | None:
        """Field: trap_v2c_status"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSnmpCommunityGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSnmpCommunity:
    """FortiAnalyzer endpoint: cli.global.system.snmp.community"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        community: int | str | None = None,
        fields: list[Literal["events", "id", "name", "query_v1_port", "query_v1_status", "query_v2c_port", "query_v2c_status", "status", "trap_v1_rport", "trap_v1_status", "trap_v2c_rport", "trap_v2c_status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemSnmpCommunityGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        community: int | str | None = None,
        events: list[Any] | None = None,
        hosts: list[dict[str, Any]] | None = None,
        hosts6: list[dict[str, Any]] | None = None,
        id: int | None = None,
        name: str | None = None,
        query_v1_port: int | None = None,
        query_v1_status: Literal["disable", "enable"] | None = None,
        query_v2c_port: int | None = None,
        query_v2c_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_v1_rport: int | None = None,
        trap_v1_status: Literal["disable", "enable"] | None = None,
        trap_v2c_rport: int | None = None,
        trap_v2c_status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        community: int | str | None = None,
        events: list[Any] | None = None,
        hosts: list[dict[str, Any]] | None = None,
        hosts6: list[dict[str, Any]] | None = None,
        id: int | None = None,
        name: str | None = None,
        query_v1_port: int | None = None,
        query_v1_status: Literal["disable", "enable"] | None = None,
        query_v2c_port: int | None = None,
        query_v2c_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_v1_rport: int | None = None,
        trap_v1_status: Literal["disable", "enable"] | None = None,
        trap_v2c_rport: int | None = None,
        trap_v2c_status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        community: int | str | None = None,
        events: list[Any] | None = None,
        hosts: list[dict[str, Any]] | None = None,
        hosts6: list[dict[str, Any]] | None = None,
        id: int | None = None,
        name: str | None = None,
        query_v1_port: int | None = None,
        query_v1_status: Literal["disable", "enable"] | None = None,
        query_v2c_port: int | None = None,
        query_v2c_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_v1_rport: int | None = None,
        trap_v1_status: Literal["disable", "enable"] | None = None,
        trap_v2c_rport: int | None = None,
        trap_v2c_status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        community: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemSnmpCommunity", "CliGlobalSystemSnmpCommunityGetResponse"]
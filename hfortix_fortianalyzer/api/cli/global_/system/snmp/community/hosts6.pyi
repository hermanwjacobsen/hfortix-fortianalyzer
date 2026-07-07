"""Type stubs for cli.global.system.snmp.community.hosts6"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSnmpCommunityHosts6GetItem:
    """Item yielded when iterating over CliGlobalSystemSnmpCommunityHosts6GetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def interface(self) -> str: ...
    @property
    def ip(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemSnmpCommunityHosts6GetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSnmpCommunityHosts6Get endpoint with autocomplete support."""

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
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def interface(self) -> str | None:
        """Field: interface"""
        ...

    @property
    def ip(self) -> str | None:
        """Field: ip"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSnmpCommunityHosts6GetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSnmpCommunityHosts6:
    """FortiAnalyzer endpoint: cli.global.system.snmp.community.hosts6"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        community: str,
        hosts6: int | str | None = None,
        fields: list[Literal["id", "interface", "ip"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemSnmpCommunityHosts6GetResponse:
        """GET operation."""
        ...

    def add(
        self,
        community: str,
        hosts6: int | str | None = None,
        id: int | None = None,
        interface: str | None = None,
        ip: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        community: str,
        hosts6: int | str | None = None,
        id: int | None = None,
        interface: str | None = None,
        ip: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        community: str,
        hosts6: int | str | None = None,
        id: int | None = None,
        interface: str | None = None,
        ip: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        community: str,
        hosts6: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemSnmpCommunityHosts6", "CliGlobalSystemSnmpCommunityHosts6GetResponse"]
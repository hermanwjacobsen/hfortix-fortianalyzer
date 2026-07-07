"""Type stubs for cli.global.system.snmp.community.hosts"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSnmpCommunityHostsGetItem:
    """Item yielded when iterating over CliGlobalSystemSnmpCommunityHostsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def interface(self) -> str: ...
    @property
    def ip(self) -> list[Any]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemSnmpCommunityHostsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSnmpCommunityHostsGet endpoint with autocomplete support."""

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
    def ip(self) -> list[Any] | None:
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
    def __iter__(self) -> Iterator[CliGlobalSystemSnmpCommunityHostsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSnmpCommunityHosts:
    """FortiAnalyzer endpoint: cli.global.system.snmp.community.hosts"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        community: str,
        hosts: int | str | None = None,
        fields: list[Literal["id", "interface", "ip"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemSnmpCommunityHostsGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        community: str,
        hosts: int | str | None = None,
        id: int | None = None,
        interface: str | None = None,
        ip: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        community: str,
        hosts: int | str | None = None,
        id: int | None = None,
        interface: str | None = None,
        ip: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        community: str,
        hosts: int | str | None = None,
        id: int | None = None,
        interface: str | None = None,
        ip: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        community: str,
        hosts: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemSnmpCommunityHosts", "CliGlobalSystemSnmpCommunityHostsGetResponse"]
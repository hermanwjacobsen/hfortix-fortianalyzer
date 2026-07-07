"""Type stubs for cli.global.system.interface.ipv6"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemInterfaceIpv6GetItem:
    """Item yielded when iterating over CliGlobalSystemInterfaceIpv6GetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def ip6_address(self) -> str: ...
    @property
    def ip6_allowaccess(self) -> list[Any]: ...
    @property
    def ip6_autoconf(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemInterfaceIpv6GetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemInterfaceIpv6Get endpoint with autocomplete support."""

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
    def ip6_address(self) -> str | None:
        """Field: ip6-address"""
        ...

    @property
    def ip6_allowaccess(self) -> list[Any] | None:
        """Field: ip6-allowaccess"""
        ...

    @property
    def ip6_autoconf(self) -> Literal["disable", "enable"] | None:
        """Field: ip6-autoconf"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemInterfaceIpv6GetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemInterfaceIpv6:
    """FortiAnalyzer endpoint: cli.global.system.interface.ipv6"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        interface: str,
    ) -> CliGlobalSystemInterfaceIpv6GetResponse:
        """GET operation."""
        ...

    def set(
        self,
        interface: str,
        ip6_address: str | None = None,
        ip6_allowaccess: list[Any] | None = None,
        ip6_autoconf: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        interface: str,
        ip6_address: str | None = None,
        ip6_allowaccess: list[Any] | None = None,
        ip6_autoconf: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemInterfaceIpv6", "CliGlobalSystemInterfaceIpv6GetResponse"]
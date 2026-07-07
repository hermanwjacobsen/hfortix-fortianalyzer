"""Type stubs for cli.global.system.dns"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemDnsGetItem:
    """Item yielded when iterating over CliGlobalSystemDnsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def ip6_primary(self) -> str: ...
    @property
    def ip6_secondary(self) -> str: ...
    @property
    def primary(self) -> str: ...
    @property
    def secondary(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemDnsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemDnsGet endpoint with autocomplete support."""

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
    def ip6_primary(self) -> str | None:
        """Field: ip6-primary"""
        ...

    @property
    def ip6_secondary(self) -> str | None:
        """Field: ip6-secondary"""
        ...

    @property
    def primary(self) -> str | None:
        """Field: primary"""
        ...

    @property
    def secondary(self) -> str | None:
        """Field: secondary"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemDnsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemDns:
    """FortiAnalyzer endpoint: cli.global.system.dns"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemDnsGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        primary: str | None = None,
        secondary: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        primary: str | None = None,
        secondary: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemDns", "CliGlobalSystemDnsGetResponse"]
"""Type stubs for cli.global.system.log.ueba"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogUebaGetItem:
    """Item yielded when iterating over CliGlobalSystemLogUebaGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def hostname_ep_unifier(self) -> Literal["disable", "enable"]: ...
    @property
    def ip_only_ep(self) -> Literal["disable", "enable"]: ...
    @property
    def ip_unique_scope(self) -> Literal["adom", "vdom"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogUebaGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogUebaGet endpoint with autocomplete support."""

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
    def hostname_ep_unifier(self) -> Literal["disable", "enable"] | None:
        """Field: hostname-ep-unifier"""
        ...

    @property
    def ip_only_ep(self) -> Literal["disable", "enable"] | None:
        """Field: ip-only-ep"""
        ...

    @property
    def ip_unique_scope(self) -> Literal["adom", "vdom"] | None:
        """Field: ip-unique-scope"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogUebaGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogUeba:
    """FortiAnalyzer endpoint: cli.global.system.log.ueba"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogUebaGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        hostname_ep_unifier: Literal["disable", "enable"] | None = None,
        ip_only_ep: Literal["disable", "enable"] | None = None,
        ip_unique_scope: Literal["adom", "vdom"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        hostname_ep_unifier: Literal["disable", "enable"] | None = None,
        ip_only_ep: Literal["disable", "enable"] | None = None,
        ip_unique_scope: Literal["adom", "vdom"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogUeba", "CliGlobalSystemLogUebaGetResponse"]
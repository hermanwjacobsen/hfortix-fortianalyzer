"""Type stubs for cli.global.system.route6"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemRoute6GetItem:
    """Item yielded when iterating over CliGlobalSystemRoute6GetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def device(self) -> str: ...
    @property
    def dst(self) -> str: ...
    @property
    def gateway(self) -> str: ...
    @property
    def prio(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemRoute6GetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemRoute6Get endpoint with autocomplete support."""

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
    def device(self) -> str | None:
        """Field: device"""
        ...

    @property
    def dst(self) -> str | None:
        """Field: dst"""
        ...

    @property
    def gateway(self) -> str | None:
        """Field: gateway"""
        ...

    @property
    def prio(self) -> int | None:
        """Field: prio"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemRoute6GetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemRoute6:
    """FortiAnalyzer endpoint: cli.global.system.route6"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        route6: int | str | None = None,
        fields: list[Literal["device", "dst", "gateway", "prio"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemRoute6GetResponse:
        """GET operation."""
        ...

    def add(
        self,
        route6: int | str | None = None,
        device: str | None = None,
        dst: str | None = None,
        gateway: str | None = None,
        prio: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        route6: int | str | None = None,
        device: str | None = None,
        dst: str | None = None,
        gateway: str | None = None,
        prio: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        route6: int | str | None = None,
        device: str | None = None,
        dst: str | None = None,
        gateway: str | None = None,
        prio: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        route6: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemRoute6", "CliGlobalSystemRoute6GetResponse"]
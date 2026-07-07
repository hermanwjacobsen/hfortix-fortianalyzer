"""Type stubs for cli.global.system.route"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemRouteGetItem:
    """Item yielded when iterating over CliGlobalSystemRouteGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def device(self) -> str: ...
    @property
    def dst(self) -> list[Any]: ...
    @property
    def gateway(self) -> str: ...
    @property
    def seq_num(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemRouteGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemRouteGet endpoint with autocomplete support."""

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
    def dst(self) -> list[Any] | None:
        """Field: dst"""
        ...

    @property
    def gateway(self) -> str | None:
        """Field: gateway"""
        ...

    @property
    def seq_num(self) -> int | None:
        """Field: seq_num"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemRouteGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemRoute:
    """FortiAnalyzer endpoint: cli.global.system.route"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        route: int | str | None = None,
        fields: list[Literal["device", "dst", "gateway", "seq_num"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemRouteGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        route: int | str | None = None,
        device: str | None = None,
        dst: list[Any] | None = None,
        gateway: str | None = None,
        seq_num: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        route: int | str | None = None,
        device: str | None = None,
        dst: list[Any] | None = None,
        gateway: str | None = None,
        seq_num: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        route: int | str | None = None,
        device: str | None = None,
        dst: list[Any] | None = None,
        gateway: str | None = None,
        seq_num: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        route: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemRoute", "CliGlobalSystemRouteGetResponse"]
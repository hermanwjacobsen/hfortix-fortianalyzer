"""Type stubs for cli.global.system.ha.vip"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemHaVipGetItem:
    """Item yielded when iterating over CliGlobalSystemHaVipGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def vip(self) -> str: ...
    @property
    def vip_interface(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemHaVipGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemHaVipGet endpoint with autocomplete support."""

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
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def vip(self) -> str | None:
        """Field: vip"""
        ...

    @property
    def vip_interface(self) -> str | None:
        """Field: vip-interface"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemHaVipGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemHaVip:
    """FortiAnalyzer endpoint: cli.global.system.ha.vip"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        vip: int | str | None = None,
        fields: list[Literal["id", "status", "vip", "vip-interface"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemHaVipGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        vip: int | str | None = None,
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        vip_interface: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        vip: int | str | None = None,
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        vip_interface: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        vip: int | str | None = None,
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        vip_interface: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        vip: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemHaVip", "CliGlobalSystemHaVipGetResponse"]
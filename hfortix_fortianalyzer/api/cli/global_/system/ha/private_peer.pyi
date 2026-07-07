"""Type stubs for cli.global.system.ha.private-peer"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemHaPrivatePeerGetItem:
    """Item yielded when iterating over CliGlobalSystemHaPrivatePeerGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def ip(self) -> str: ...
    @property
    def ip6(self) -> str: ...
    @property
    def serial_number(self) -> str: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemHaPrivatePeerGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemHaPrivatePeerGet endpoint with autocomplete support."""

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
    def ip(self) -> str | None:
        """Field: ip"""
        ...

    @property
    def ip6(self) -> str | None:
        """Field: ip6"""
        ...

    @property
    def serial_number(self) -> str | None:
        """Field: serial-number"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemHaPrivatePeerGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemHaPrivatePeer:
    """FortiAnalyzer endpoint: cli.global.system.ha.private-peer"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        private_peer: int | str | None = None,
        fields: list[Literal["id", "ip", "ip6", "serial-number", "status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemHaPrivatePeerGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        private_peer: int | str | None = None,
        id: int | None = None,
        ip: str | None = None,
        ip6: str | None = None,
        serial_number: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        private_peer: int | str | None = None,
        id: int | None = None,
        ip: str | None = None,
        ip6: str | None = None,
        serial_number: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        private_peer: int | str | None = None,
        id: int | None = None,
        ip: str | None = None,
        ip6: str | None = None,
        serial_number: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        private_peer: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemHaPrivatePeer", "CliGlobalSystemHaPrivatePeerGetResponse"]
"""Type stubs for cli.global.system.ha.peer"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemHaPeerGetItem:
    """Item yielded when iterating over CliGlobalSystemHaPeerGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def addr(self) -> str: ...
    @property
    def addr_hb(self) -> str: ...
    @property
    def id(self) -> int: ...
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


class CliGlobalSystemHaPeerGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemHaPeerGet endpoint with autocomplete support."""

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
    def addr(self) -> str | None:
        """Field: addr"""
        ...

    @property
    def addr_hb(self) -> str | None:
        """Field: addr-hb"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemHaPeerGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemHaPeer:
    """FortiAnalyzer endpoint: cli.global.system.ha.peer"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        peer: int | str | None = None,
        fields: list[Literal["addr", "addr-hb", "id", "serial-number", "status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemHaPeerGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        peer: int | str | None = None,
        addr: str | None = None,
        addr_hb: str | None = None,
        id: int | None = None,
        serial_number: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        peer: int | str | None = None,
        addr: str | None = None,
        addr_hb: str | None = None,
        id: int | None = None,
        serial_number: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        peer: int | str | None = None,
        addr: str | None = None,
        addr_hb: str | None = None,
        id: int | None = None,
        serial_number: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        peer: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemHaPeer", "CliGlobalSystemHaPeerGetResponse"]
"""Type stubs for cli.global.system.local-in-policy"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocalInPolicyGetItem:
    """Item yielded when iterating over CliGlobalSystemLocalInPolicyGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def action(self) -> Literal["drop", "reject", "accept"]: ...
    @property
    def description(self) -> str: ...
    @property
    def dport(self) -> list[DportItem]: ...
    @property
    def dst(self) -> list[DstItem]: ...
    @property
    def id(self) -> int: ...
    @property
    def intf(self) -> list[IntfItem]: ...
    @property
    def protocol(self) -> Literal["tcp", "udp", "tcp_udp"]: ...
    @property
    def src(self) -> list[SrcItem]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class DportItem:
    """Nested item type for dport array."""

    @property
    def dport_value(self) -> str: ...

class DstItem:
    """Nested item type for dst array."""

    @property
    def dst_ip(self) -> str: ...

class IntfItem:
    """Nested item type for intf array."""

    @property
    def intf_name(self) -> str: ...

class SrcItem:
    """Nested item type for src array."""

    @property
    def src_ip(self) -> str: ...


class CliGlobalSystemLocalInPolicyGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocalInPolicyGet endpoint with autocomplete support."""

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
    def action(self) -> Literal["drop", "reject", "accept"] | None:
        """Field: action"""
        ...

    @property
    def description(self) -> str | None:
        """Field: description"""
        ...

    @property
    def dport(self) -> list[DportItem]:
        """Field: dport"""
        ...

    @property
    def dst(self) -> list[DstItem]:
        """Field: dst"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def intf(self) -> list[IntfItem]:
        """Field: intf"""
        ...

    @property
    def protocol(self) -> Literal["tcp", "udp", "tcp_udp"] | None:
        """Field: protocol"""
        ...

    @property
    def src(self) -> list[SrcItem]:
        """Field: src"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocalInPolicyGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocalInPolicy:
    """FortiAnalyzer endpoint: cli.global.system.local-in-policy"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        local_in_policy: int | str | None = None,
        fields: list[Literal["action", "description", "id", "protocol"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLocalInPolicyGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        local_in_policy: int | str | None = None,
        action: Literal["drop", "reject", "accept"] | None = None,
        description: str | None = None,
        dport: list[dict[str, Any]] | None = None,
        dst: list[dict[str, Any]] | None = None,
        id: int | None = None,
        intf: list[dict[str, Any]] | None = None,
        protocol: Literal["tcp", "udp", "tcp_udp"] | None = None,
        src: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        local_in_policy: int | str | None = None,
        action: Literal["drop", "reject", "accept"] | None = None,
        description: str | None = None,
        dport: list[dict[str, Any]] | None = None,
        dst: list[dict[str, Any]] | None = None,
        id: int | None = None,
        intf: list[dict[str, Any]] | None = None,
        protocol: Literal["tcp", "udp", "tcp_udp"] | None = None,
        src: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        local_in_policy: int | str | None = None,
        action: Literal["drop", "reject", "accept"] | None = None,
        description: str | None = None,
        dport: list[dict[str, Any]] | None = None,
        dst: list[dict[str, Any]] | None = None,
        id: int | None = None,
        intf: list[dict[str, Any]] | None = None,
        protocol: Literal["tcp", "udp", "tcp_udp"] | None = None,
        src: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        local_in_policy: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLocalInPolicy", "CliGlobalSystemLocalInPolicyGetResponse"]
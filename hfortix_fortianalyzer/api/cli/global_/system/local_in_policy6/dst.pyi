"""Type stubs for cli.global.system.local-in-policy6.dst"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocalInPolicy6DstGetItem:
    """Item yielded when iterating over CliGlobalSystemLocalInPolicy6DstGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def src_ip(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocalInPolicy6DstGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocalInPolicy6DstGet endpoint with autocomplete support."""

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
    def src_ip(self) -> str | None:
        """Field: src-ip"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocalInPolicy6DstGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocalInPolicy6Dst:
    """FortiAnalyzer endpoint: cli.global.system.local-in-policy6.dst"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        local_in_policy6: str,
        dst: int | str | None = None,
        fields: list[Literal["src-ip"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLocalInPolicy6DstGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        local_in_policy6: str,
        dst: int | str | None = None,
        src_ip: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        local_in_policy6: str,
        dst: int | str | None = None,
        src_ip: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        local_in_policy6: str,
        dst: int | str | None = None,
        src_ip: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        local_in_policy6: str,
        dst: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLocalInPolicy6Dst", "CliGlobalSystemLocalInPolicy6DstGetResponse"]
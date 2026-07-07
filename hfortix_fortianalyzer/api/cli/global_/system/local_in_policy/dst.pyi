"""Type stubs for cli.global.system.local-in-policy.dst"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocalInPolicyDstGetItem:
    """Item yielded when iterating over CliGlobalSystemLocalInPolicyDstGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def dst_ip(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocalInPolicyDstGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocalInPolicyDstGet endpoint with autocomplete support."""

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
    def dst_ip(self) -> str | None:
        """Field: dst-ip"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocalInPolicyDstGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocalInPolicyDst:
    """FortiAnalyzer endpoint: cli.global.system.local-in-policy.dst"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        local_in_policy: str,
        dst: int | str | None = None,
        fields: list[Literal["dst-ip"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLocalInPolicyDstGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        local_in_policy: str,
        dst: int | str | None = None,
        dst_ip: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        local_in_policy: str,
        dst: int | str | None = None,
        dst_ip: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        local_in_policy: str,
        dst: int | str | None = None,
        dst_ip: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        local_in_policy: str,
        dst: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLocalInPolicyDst", "CliGlobalSystemLocalInPolicyDstGetResponse"]
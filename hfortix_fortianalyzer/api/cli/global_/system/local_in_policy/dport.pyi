"""Type stubs for cli.global.system.local-in-policy.dport"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocalInPolicyDportGetItem:
    """Item yielded when iterating over CliGlobalSystemLocalInPolicyDportGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def dport_value(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocalInPolicyDportGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocalInPolicyDportGet endpoint with autocomplete support."""

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
    def dport_value(self) -> str | None:
        """Field: dport-value"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocalInPolicyDportGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocalInPolicyDport:
    """FortiAnalyzer endpoint: cli.global.system.local-in-policy.dport"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        local_in_policy: str,
        dport: int | str | None = None,
        fields: list[Literal["dport-value"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLocalInPolicyDportGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        local_in_policy: str,
        dport: int | str | None = None,
        dport_value: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        local_in_policy: str,
        dport: int | str | None = None,
        dport_value: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        local_in_policy: str,
        dport: int | str | None = None,
        dport_value: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        local_in_policy: str,
        dport: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLocalInPolicyDport", "CliGlobalSystemLocalInPolicyDportGetResponse"]
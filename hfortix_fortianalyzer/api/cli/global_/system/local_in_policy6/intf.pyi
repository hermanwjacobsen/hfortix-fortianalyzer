"""Type stubs for cli.global.system.local-in-policy6.intf"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocalInPolicy6IntfGetItem:
    """Item yielded when iterating over CliGlobalSystemLocalInPolicy6IntfGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def intf_name(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocalInPolicy6IntfGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocalInPolicy6IntfGet endpoint with autocomplete support."""

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
    def intf_name(self) -> str | None:
        """Field: intf-name"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocalInPolicy6IntfGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocalInPolicy6Intf:
    """FortiAnalyzer endpoint: cli.global.system.local-in-policy6.intf"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        local_in_policy6: str,
        intf: int | str | None = None,
        fields: list[Literal["intf-name"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLocalInPolicy6IntfGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        local_in_policy6: str,
        intf: int | str | None = None,
        intf_name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        local_in_policy6: str,
        intf: int | str | None = None,
        intf_name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        local_in_policy6: str,
        intf: int | str | None = None,
        intf_name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        local_in_policy6: str,
        intf: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLocalInPolicy6Intf", "CliGlobalSystemLocalInPolicy6IntfGetResponse"]
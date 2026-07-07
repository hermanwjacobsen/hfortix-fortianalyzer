"""Type stubs for cli.global.system.soc-fabric"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSocFabricGetItem:
    """Item yielded when iterating over CliGlobalSystemSocFabricGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def port(self) -> int: ...
    @property
    def role(self) -> Literal["member", "supervisor"]: ...
    @property
    def secure_connection(self) -> Literal["disable", "enable"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def supervisor(self) -> str: ...
    @property
    def trusted_list(self) -> list[TrustedListItem]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class TrustedListItem:
    """Nested item type for trusted-list array."""

    @property
    def id(self) -> int: ...
    @property
    def serial(self) -> str: ...


class CliGlobalSystemSocFabricGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSocFabricGet endpoint with autocomplete support."""

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
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def port(self) -> int | None:
        """Field: port"""
        ...

    @property
    def role(self) -> Literal["member", "supervisor"] | None:
        """Field: role"""
        ...

    @property
    def secure_connection(self) -> Literal["disable", "enable"] | None:
        """Field: secure-connection"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def supervisor(self) -> str | None:
        """Field: supervisor"""
        ...

    @property
    def trusted_list(self) -> list[TrustedListItem]:
        """Field: trusted-list"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSocFabricGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSocFabric:
    """FortiAnalyzer endpoint: cli.global.system.soc-fabric"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemSocFabricGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        name: str | None = None,
        port: int | None = None,
        role: Literal["member", "supervisor"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        supervisor: str | None = None,
        trusted_list: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        name: str | None = None,
        port: int | None = None,
        role: Literal["member", "supervisor"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        supervisor: str | None = None,
        trusted_list: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemSocFabric", "CliGlobalSystemSocFabricGetResponse"]
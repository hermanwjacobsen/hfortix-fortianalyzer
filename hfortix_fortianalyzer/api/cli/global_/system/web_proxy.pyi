"""Type stubs for cli.global.system.web-proxy"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemWebProxyGetItem:
    """Item yielded when iterating over CliGlobalSystemWebProxyGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def address(self) -> str: ...
    @property
    def mode(self) -> Literal["proxy", "tunnel"]: ...
    @property
    def password(self) -> list[Any]: ...
    @property
    def port(self) -> int: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def username(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemWebProxyGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemWebProxyGet endpoint with autocomplete support."""

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
    def address(self) -> str | None:
        """Field: address"""
        ...

    @property
    def mode(self) -> Literal["proxy", "tunnel"] | None:
        """Field: mode"""
        ...

    @property
    def password(self) -> list[Any] | None:
        """Field: password"""
        ...

    @property
    def port(self) -> int | None:
        """Field: port"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def username(self) -> str | None:
        """Field: username"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemWebProxyGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemWebProxy:
    """FortiAnalyzer endpoint: cli.global.system.web-proxy"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemWebProxyGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        address: str | None = None,
        mode: Literal["proxy", "tunnel"] | None = None,
        password: list[Any] | None = None,
        port: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        username: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        address: str | None = None,
        mode: Literal["proxy", "tunnel"] | None = None,
        password: list[Any] | None = None,
        port: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        username: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemWebProxy", "CliGlobalSystemWebProxyGetResponse"]
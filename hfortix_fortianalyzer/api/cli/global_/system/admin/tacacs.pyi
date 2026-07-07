"""Type stubs for cli.global.system.admin.tacacs"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminTacacsGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminTacacsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def authen_type(self) -> Literal["auto", "ascii", "pap", "chap", "mschap"]: ...
    @property
    def authorization(self) -> Literal["disable", "enable"]: ...
    @property
    def key(self) -> list[Any]: ...
    @property
    def name(self) -> str: ...
    @property
    def port(self) -> int: ...
    @property
    def secondary_key(self) -> list[Any]: ...
    @property
    def secondary_server(self) -> str: ...
    @property
    def server(self) -> str: ...
    @property
    def src_ip(self) -> str: ...
    @property
    def tertiary_key(self) -> list[Any]: ...
    @property
    def tertiary_server(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAdminTacacsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminTacacsGet endpoint with autocomplete support."""

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
    def authen_type(self) -> Literal["auto", "ascii", "pap", "chap", "mschap"] | None:
        """Field: authen-type"""
        ...

    @property
    def authorization(self) -> Literal["disable", "enable"] | None:
        """Field: authorization"""
        ...

    @property
    def key(self) -> list[Any] | None:
        """Field: key"""
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
    def secondary_key(self) -> list[Any] | None:
        """Field: secondary-key"""
        ...

    @property
    def secondary_server(self) -> str | None:
        """Field: secondary-server"""
        ...

    @property
    def server(self) -> str | None:
        """Field: server"""
        ...

    @property
    def src_ip(self) -> str | None:
        """Field: src-ip"""
        ...

    @property
    def tertiary_key(self) -> list[Any] | None:
        """Field: tertiary-key"""
        ...

    @property
    def tertiary_server(self) -> str | None:
        """Field: tertiary-server"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminTacacsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminTacacs:
    """FortiAnalyzer endpoint: cli.global.system.admin.tacacs"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        tacacs: int | str | None = None,
        fields: list[Literal["authen-type", "authorization", "key", "name", "port", "secondary-key", "secondary-server", "server", "src-ip", "tertiary-key", "tertiary-server"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminTacacsGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        tacacs: int | str | None = None,
        authen_type: Literal["auto", "ascii", "pap", "chap", "mschap"] | None = None,
        authorization: Literal["disable", "enable"] | None = None,
        key: list[Any] | None = None,
        name: str | None = None,
        port: int | None = None,
        secondary_key: list[Any] | None = None,
        secondary_server: str | None = None,
        server: str | None = None,
        src_ip: str | None = None,
        tertiary_key: list[Any] | None = None,
        tertiary_server: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        tacacs: int | str | None = None,
        authen_type: Literal["auto", "ascii", "pap", "chap", "mschap"] | None = None,
        authorization: Literal["disable", "enable"] | None = None,
        key: list[Any] | None = None,
        name: str | None = None,
        port: int | None = None,
        secondary_key: list[Any] | None = None,
        secondary_server: str | None = None,
        server: str | None = None,
        src_ip: str | None = None,
        tertiary_key: list[Any] | None = None,
        tertiary_server: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        tacacs: int | str | None = None,
        authen_type: Literal["auto", "ascii", "pap", "chap", "mschap"] | None = None,
        authorization: Literal["disable", "enable"] | None = None,
        key: list[Any] | None = None,
        name: str | None = None,
        port: int | None = None,
        secondary_key: list[Any] | None = None,
        secondary_server: str | None = None,
        server: str | None = None,
        src_ip: str | None = None,
        tertiary_key: list[Any] | None = None,
        tertiary_server: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        tacacs: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminTacacs", "CliGlobalSystemAdminTacacsGetResponse"]
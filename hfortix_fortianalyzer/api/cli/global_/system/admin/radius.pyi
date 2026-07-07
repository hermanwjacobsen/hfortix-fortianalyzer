"""Type stubs for cli.global.system.admin.radius"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminRadiusGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminRadiusGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def auth_type(self) -> Literal["any", "pap", "chap", "mschap2"]: ...
    @property
    def ca_cert(self) -> str: ...
    @property
    def client_cert(self) -> str: ...
    @property
    def message_authenticator(self) -> Literal["optional", "require"]: ...
    @property
    def name(self) -> str: ...
    @property
    def nas_ip(self) -> str: ...
    @property
    def port(self) -> int: ...
    @property
    def protocol(self) -> Literal["udp", "tls"]: ...
    @property
    def secondary_secret(self) -> list[Any]: ...
    @property
    def secondary_server(self) -> str: ...
    @property
    def secret(self) -> list[Any]: ...
    @property
    def server(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAdminRadiusGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminRadiusGet endpoint with autocomplete support."""

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
    def auth_type(self) -> Literal["any", "pap", "chap", "mschap2"] | None:
        """Field: auth-type"""
        ...

    @property
    def ca_cert(self) -> str | None:
        """Field: ca-cert"""
        ...

    @property
    def client_cert(self) -> str | None:
        """Field: client-cert"""
        ...

    @property
    def message_authenticator(self) -> Literal["optional", "require"] | None:
        """Field: message-authenticator"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def nas_ip(self) -> str | None:
        """Field: nas-ip"""
        ...

    @property
    def port(self) -> int | None:
        """Field: port"""
        ...

    @property
    def protocol(self) -> Literal["udp", "tls"] | None:
        """Field: protocol"""
        ...

    @property
    def secondary_secret(self) -> list[Any] | None:
        """Field: secondary-secret"""
        ...

    @property
    def secondary_server(self) -> str | None:
        """Field: secondary-server"""
        ...

    @property
    def secret(self) -> list[Any] | None:
        """Field: secret"""
        ...

    @property
    def server(self) -> str | None:
        """Field: server"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminRadiusGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminRadius:
    """FortiAnalyzer endpoint: cli.global.system.admin.radius"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        radius: int | str | None = None,
        fields: list[Literal["auth-type", "ca-cert", "client-cert", "message-authenticator", "name", "nas-ip", "port", "protocol", "secondary-secret", "secondary-server", "secret", "server"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminRadiusGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        radius: int | str | None = None,
        auth_type: Literal["any", "pap", "chap", "mschap2"] | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        message_authenticator: Literal["optional", "require"] | None = None,
        name: str | None = None,
        nas_ip: str | None = None,
        port: int | None = None,
        protocol: Literal["udp", "tls"] | None = None,
        secondary_secret: list[Any] | None = None,
        secondary_server: str | None = None,
        secret: list[Any] | None = None,
        server: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        radius: int | str | None = None,
        auth_type: Literal["any", "pap", "chap", "mschap2"] | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        message_authenticator: Literal["optional", "require"] | None = None,
        name: str | None = None,
        nas_ip: str | None = None,
        port: int | None = None,
        protocol: Literal["udp", "tls"] | None = None,
        secondary_secret: list[Any] | None = None,
        secondary_server: str | None = None,
        secret: list[Any] | None = None,
        server: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        radius: int | str | None = None,
        auth_type: Literal["any", "pap", "chap", "mschap2"] | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        message_authenticator: Literal["optional", "require"] | None = None,
        name: str | None = None,
        nas_ip: str | None = None,
        port: int | None = None,
        protocol: Literal["udp", "tls"] | None = None,
        secondary_secret: list[Any] | None = None,
        secondary_server: str | None = None,
        secret: list[Any] | None = None,
        server: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        radius: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminRadius", "CliGlobalSystemAdminRadiusGetResponse"]
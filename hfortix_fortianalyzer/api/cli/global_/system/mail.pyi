"""Type stubs for cli.global.system.mail"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemMailGetItem:
    """Item yielded when iterating over CliGlobalSystemMailGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def auth(self) -> Literal["disable", "enable"]: ...
    @property
    def auth_type(self) -> Literal["psk", "certificate", "oauth2"]: ...
    @property
    def from_(self) -> str: ...
    @property
    def id(self) -> str: ...
    @property
    def local_cert(self) -> str: ...
    @property
    def oauth2_auth_scope(self) -> str: ...
    @property
    def oauth2_auth_server(self) -> str: ...
    @property
    def oauth2_client_id(self) -> str: ...
    @property
    def oauth2_client_secret(self) -> list[Any]: ...
    @property
    def passwd(self) -> list[Any]: ...
    @property
    def port(self) -> int: ...
    @property
    def secure_option(self) -> Literal["default", "none", "smtps", "starttls"]: ...
    @property
    def server(self) -> str: ...
    @property
    def ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def user(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemMailGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemMailGet endpoint with autocomplete support."""

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
    def auth(self) -> Literal["disable", "enable"] | None:
        """Field: auth"""
        ...

    @property
    def auth_type(self) -> Literal["psk", "certificate", "oauth2"] | None:
        """Field: auth-type"""
        ...

    @property
    def from_(self) -> str | None:
        """Field: from"""
        ...

    @property
    def id(self) -> str | None:
        """Field: id"""
        ...

    @property
    def local_cert(self) -> str | None:
        """Field: local-cert"""
        ...

    @property
    def oauth2_auth_scope(self) -> str | None:
        """Field: oauth2-auth-scope"""
        ...

    @property
    def oauth2_auth_server(self) -> str | None:
        """Field: oauth2-auth-server"""
        ...

    @property
    def oauth2_client_id(self) -> str | None:
        """Field: oauth2-client-id"""
        ...

    @property
    def oauth2_client_secret(self) -> list[Any] | None:
        """Field: oauth2-client-secret"""
        ...

    @property
    def passwd(self) -> list[Any] | None:
        """Field: passwd"""
        ...

    @property
    def port(self) -> int | None:
        """Field: port"""
        ...

    @property
    def secure_option(self) -> Literal["default", "none", "smtps", "starttls"] | None:
        """Field: secure-option"""
        ...

    @property
    def server(self) -> str | None:
        """Field: server"""
        ...

    @property
    def ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: ssl-protocol"""
        ...

    @property
    def user(self) -> str | None:
        """Field: user"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemMailGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemMail:
    """FortiAnalyzer endpoint: cli.global.system.mail"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        mail: int | str | None = None,
        fields: list[Literal["auth", "auth-type", "from", "id", "local-cert", "oauth2-auth-scope", "oauth2-auth-server", "oauth2-client-id", "oauth2-client-secret", "passwd", "port", "secure-option", "server", "ssl-protocol", "user"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemMailGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        mail: int | str | None = None,
        auth: Literal["disable", "enable"] | None = None,
        auth_type: Literal["psk", "certificate", "oauth2"] | None = None,
        from_: str | None = None,
        id: str | None = None,
        local_cert: str | None = None,
        oauth2_auth_scope: str | None = None,
        oauth2_auth_server: str | None = None,
        oauth2_client_id: str | None = None,
        oauth2_client_secret: list[Any] | None = None,
        passwd: list[Any] | None = None,
        port: int | None = None,
        secure_option: Literal["default", "none", "smtps", "starttls"] | None = None,
        server: str | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        user: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        mail: int | str | None = None,
        auth: Literal["disable", "enable"] | None = None,
        auth_type: Literal["psk", "certificate", "oauth2"] | None = None,
        from_: str | None = None,
        id: str | None = None,
        local_cert: str | None = None,
        oauth2_auth_scope: str | None = None,
        oauth2_auth_server: str | None = None,
        oauth2_client_id: str | None = None,
        oauth2_client_secret: list[Any] | None = None,
        passwd: list[Any] | None = None,
        port: int | None = None,
        secure_option: Literal["default", "none", "smtps", "starttls"] | None = None,
        server: str | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        user: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        mail: int | str | None = None,
        auth: Literal["disable", "enable"] | None = None,
        auth_type: Literal["psk", "certificate", "oauth2"] | None = None,
        from_: str | None = None,
        id: str | None = None,
        local_cert: str | None = None,
        oauth2_auth_scope: str | None = None,
        oauth2_auth_server: str | None = None,
        oauth2_client_id: str | None = None,
        oauth2_client_secret: list[Any] | None = None,
        passwd: list[Any] | None = None,
        port: int | None = None,
        secure_option: Literal["default", "none", "smtps", "starttls"] | None = None,
        server: str | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        user: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        mail: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemMail", "CliGlobalSystemMailGetResponse"]
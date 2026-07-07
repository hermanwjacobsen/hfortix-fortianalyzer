"""Type stubs for cli.global.system.admin.ldap"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminLdapGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminLdapGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def adom(self) -> list[AdomItem]: ...
    @property
    def adom_access(self) -> Literal["all", "specify"]: ...
    @property
    def adom_attr(self) -> str: ...
    @property
    def attributes(self) -> str: ...
    @property
    def ca_cert(self) -> str: ...
    @property
    def cnid(self) -> str: ...
    @property
    def dn(self) -> str: ...
    @property
    def filter(self) -> str: ...
    @property
    def group(self) -> str: ...
    @property
    def memberof_attr(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def password(self) -> list[Any]: ...
    @property
    def port(self) -> int: ...
    @property
    def profile_attr(self) -> str: ...
    @property
    def secondary_server(self) -> str: ...
    @property
    def secure(self) -> Literal["disable", "starttls", "ldaps"]: ...
    @property
    def server(self) -> str: ...
    @property
    def ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def tertiary_server(self) -> str: ...
    @property
    def type(self) -> Literal["simple", "anonymous", "regular"]: ...
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


class AdomItem:
    """Nested item type for adom array."""

    @property
    def adom_name(self) -> str: ...


class CliGlobalSystemAdminLdapGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminLdapGet endpoint with autocomplete support."""

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
    def adom(self) -> list[AdomItem]:
        """Field: adom"""
        ...

    @property
    def adom_access(self) -> Literal["all", "specify"] | None:
        """Field: adom-access"""
        ...

    @property
    def adom_attr(self) -> str | None:
        """Field: adom-attr"""
        ...

    @property
    def attributes(self) -> str | None:
        """Field: attributes"""
        ...

    @property
    def ca_cert(self) -> str | None:
        """Field: ca-cert"""
        ...

    @property
    def cnid(self) -> str | None:
        """Field: cnid"""
        ...

    @property
    def dn(self) -> str | None:
        """Field: dn"""
        ...

    @property
    def filter(self) -> str | None:
        """Field: filter"""
        ...

    @property
    def group(self) -> str | None:
        """Field: group"""
        ...

    @property
    def memberof_attr(self) -> str | None:
        """Field: memberof-attr"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
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
    def profile_attr(self) -> str | None:
        """Field: profile-attr"""
        ...

    @property
    def secondary_server(self) -> str | None:
        """Field: secondary-server"""
        ...

    @property
    def secure(self) -> Literal["disable", "starttls", "ldaps"] | None:
        """Field: secure"""
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
    def tertiary_server(self) -> str | None:
        """Field: tertiary-server"""
        ...

    @property
    def type(self) -> Literal["simple", "anonymous", "regular"] | None:
        """Field: type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminLdapGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminLdap:
    """FortiAnalyzer endpoint: cli.global.system.admin.ldap"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        ldap: int | str | None = None,
        fields: list[Literal["adom-access", "adom-attr", "attributes", "ca-cert", "cnid", "dn", "filter", "group", "memberof-attr", "name", "password", "port", "profile-attr", "secondary-server", "secure", "server", "ssl-protocol", "tertiary-server", "type", "username"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminLdapGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        ldap: int | str | None = None,
        adom: list[dict[str, Any]] | None = None,
        adom_access: Literal["all", "specify"] | None = None,
        adom_attr: str | None = None,
        attributes: str | None = None,
        ca_cert: str | None = None,
        cnid: str | None = None,
        dn: str | None = None,
        filter: str | None = None,
        group: str | None = None,
        memberof_attr: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        port: int | None = None,
        profile_attr: str | None = None,
        secondary_server: str | None = None,
        secure: Literal["disable", "starttls", "ldaps"] | None = None,
        server: str | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        tertiary_server: str | None = None,
        type: Literal["simple", "anonymous", "regular"] | None = None,
        username: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        ldap: int | str | None = None,
        adom: list[dict[str, Any]] | None = None,
        adom_access: Literal["all", "specify"] | None = None,
        adom_attr: str | None = None,
        attributes: str | None = None,
        ca_cert: str | None = None,
        cnid: str | None = None,
        dn: str | None = None,
        filter: str | None = None,
        group: str | None = None,
        memberof_attr: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        port: int | None = None,
        profile_attr: str | None = None,
        secondary_server: str | None = None,
        secure: Literal["disable", "starttls", "ldaps"] | None = None,
        server: str | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        tertiary_server: str | None = None,
        type: Literal["simple", "anonymous", "regular"] | None = None,
        username: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        ldap: int | str | None = None,
        adom: list[dict[str, Any]] | None = None,
        adom_access: Literal["all", "specify"] | None = None,
        adom_attr: str | None = None,
        attributes: str | None = None,
        ca_cert: str | None = None,
        cnid: str | None = None,
        dn: str | None = None,
        filter: str | None = None,
        group: str | None = None,
        memberof_attr: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        port: int | None = None,
        profile_attr: str | None = None,
        secondary_server: str | None = None,
        secure: Literal["disable", "starttls", "ldaps"] | None = None,
        server: str | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        tertiary_server: str | None = None,
        type: Literal["simple", "anonymous", "regular"] | None = None,
        username: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        ldap: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminLdap", "CliGlobalSystemAdminLdapGetResponse"]
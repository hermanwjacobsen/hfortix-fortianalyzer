"""Type stubs for cli.global.system.snmp.user"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSnmpUserGetItem:
    """Item yielded when iterating over CliGlobalSystemSnmpUserGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def auth_proto(self) -> Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"]: ...
    @property
    def auth_pwd(self) -> list[Any]: ...
    @property
    def events(self) -> list[Any]: ...
    @property
    def name(self) -> str: ...
    @property
    def notify_hosts(self) -> str: ...
    @property
    def notify_hosts6(self) -> str: ...
    @property
    def notify_port(self) -> int: ...
    @property
    def priv_proto(self) -> Literal["aes", "des", "aes256", "aes256cisco"]: ...
    @property
    def priv_pwd(self) -> list[Any]: ...
    @property
    def queries(self) -> Literal["disable", "enable"]: ...
    @property
    def query_port(self) -> int: ...
    @property
    def security_level(self) -> Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemSnmpUserGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSnmpUserGet endpoint with autocomplete support."""

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
    def auth_proto(self) -> Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None:
        """Field: auth-proto"""
        ...

    @property
    def auth_pwd(self) -> list[Any] | None:
        """Field: auth-pwd"""
        ...

    @property
    def events(self) -> list[Any] | None:
        """Field: events"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def notify_hosts(self) -> str | None:
        """Field: notify-hosts"""
        ...

    @property
    def notify_hosts6(self) -> str | None:
        """Field: notify-hosts6"""
        ...

    @property
    def notify_port(self) -> int | None:
        """Field: notify-port"""
        ...

    @property
    def priv_proto(self) -> Literal["aes", "des", "aes256", "aes256cisco"] | None:
        """Field: priv-proto"""
        ...

    @property
    def priv_pwd(self) -> list[Any] | None:
        """Field: priv-pwd"""
        ...

    @property
    def queries(self) -> Literal["disable", "enable"] | None:
        """Field: queries"""
        ...

    @property
    def query_port(self) -> int | None:
        """Field: query-port"""
        ...

    @property
    def security_level(self) -> Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None:
        """Field: security-level"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSnmpUserGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSnmpUser:
    """FortiAnalyzer endpoint: cli.global.system.snmp.user"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        user: int | str | None = None,
        fields: list[Literal["auth-proto", "auth-pwd", "events", "name", "notify-hosts", "notify-hosts6", "notify-port", "priv-proto", "priv-pwd", "queries", "query-port", "security-level"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemSnmpUserGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        user: int | str | None = None,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = None,
        auth_pwd: list[Any] | None = None,
        events: list[Any] | None = None,
        name: str | None = None,
        notify_hosts: str | None = None,
        notify_hosts6: str | None = None,
        notify_port: int | None = None,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = None,
        priv_pwd: list[Any] | None = None,
        queries: Literal["disable", "enable"] | None = None,
        query_port: int | None = None,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        user: int | str | None = None,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = None,
        auth_pwd: list[Any] | None = None,
        events: list[Any] | None = None,
        name: str | None = None,
        notify_hosts: str | None = None,
        notify_hosts6: str | None = None,
        notify_port: int | None = None,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = None,
        priv_pwd: list[Any] | None = None,
        queries: Literal["disable", "enable"] | None = None,
        query_port: int | None = None,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        user: int | str | None = None,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = None,
        auth_pwd: list[Any] | None = None,
        events: list[Any] | None = None,
        name: str | None = None,
        notify_hosts: str | None = None,
        notify_hosts6: str | None = None,
        notify_port: int | None = None,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = None,
        priv_pwd: list[Any] | None = None,
        queries: Literal["disable", "enable"] | None = None,
        query_port: int | None = None,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        user: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemSnmpUser", "CliGlobalSystemSnmpUserGetResponse"]
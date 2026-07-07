"""Type stubs for cli.global.system.syslog"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSyslogGetItem:
    """Item yielded when iterating over CliGlobalSystemSyslogGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def ip(self) -> str: ...
    @property
    def local_cert(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def peer_cert_cn(self) -> str: ...
    @property
    def port(self) -> int: ...
    @property
    def reliable(self) -> Literal["disable", "enable"]: ...
    @property
    def secure_connection(self) -> Literal["disable", "enable"]: ...
    @property
    def ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemSyslogGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSyslogGet endpoint with autocomplete support."""

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
    def ip(self) -> str | None:
        """Field: ip"""
        ...

    @property
    def local_cert(self) -> str | None:
        """Field: local-cert"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def peer_cert_cn(self) -> str | None:
        """Field: peer-cert-cn"""
        ...

    @property
    def port(self) -> int | None:
        """Field: port"""
        ...

    @property
    def reliable(self) -> Literal["disable", "enable"] | None:
        """Field: reliable"""
        ...

    @property
    def secure_connection(self) -> Literal["disable", "enable"] | None:
        """Field: secure-connection"""
        ...

    @property
    def ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: ssl-protocol"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSyslogGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSyslog:
    """FortiAnalyzer endpoint: cli.global.system.syslog"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        syslog: int | str | None = None,
        fields: list[Literal["ip", "local-cert", "name", "peer-cert-cn", "port", "reliable", "secure-connection", "ssl-protocol"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemSyslogGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        syslog: int | str | None = None,
        ip: str | None = None,
        local_cert: str | None = None,
        name: str | None = None,
        peer_cert_cn: str | None = None,
        port: int | None = None,
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        syslog: int | str | None = None,
        ip: str | None = None,
        local_cert: str | None = None,
        name: str | None = None,
        peer_cert_cn: str | None = None,
        port: int | None = None,
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        syslog: int | str | None = None,
        ip: str | None = None,
        local_cert: str | None = None,
        name: str | None = None,
        peer_cert_cn: str | None = None,
        port: int | None = None,
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        syslog: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemSyslog", "CliGlobalSystemSyslogGetResponse"]
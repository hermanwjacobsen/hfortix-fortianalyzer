"""Type stubs for cli.global.system.global.ssl-cipher-suites"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemGlobalSslCipherSuitesGetItem:
    """Item yielded when iterating over CliGlobalSystemGlobalSslCipherSuitesGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def cipher(self) -> str: ...
    @property
    def priority(self) -> int: ...
    @property
    def version(self) -> Literal["tls1.2-or-below", "tls1.3"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemGlobalSslCipherSuitesGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemGlobalSslCipherSuitesGet endpoint with autocomplete support."""

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
    def cipher(self) -> str | None:
        """Field: cipher"""
        ...

    @property
    def priority(self) -> int | None:
        """Field: priority"""
        ...

    @property
    def version(self) -> Literal["tls1.2-or-below", "tls1.3"] | None:
        """Field: version"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemGlobalSslCipherSuitesGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemGlobalSslCipherSuites:
    """FortiAnalyzer endpoint: cli.global.system.global.ssl-cipher-suites"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        ssl_cipher_suites: int | str | None = None,
        fields: list[Literal["cipher", "priority", "version"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemGlobalSslCipherSuitesGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        ssl_cipher_suites: int | str | None = None,
        cipher: str | None = None,
        priority: int | None = None,
        version: Literal["tls1.2-or-below", "tls1.3"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        ssl_cipher_suites: int | str | None = None,
        cipher: str | None = None,
        priority: int | None = None,
        version: Literal["tls1.2-or-below", "tls1.3"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        ssl_cipher_suites: int | str | None = None,
        cipher: str | None = None,
        priority: int | None = None,
        version: Literal["tls1.2-or-below", "tls1.3"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        ssl_cipher_suites: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemGlobalSslCipherSuites", "CliGlobalSystemGlobalSslCipherSuitesGetResponse"]
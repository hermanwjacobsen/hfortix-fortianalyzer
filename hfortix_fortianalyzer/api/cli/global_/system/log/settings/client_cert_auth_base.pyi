"""Type stubs for cli.global.system.log.settings.client-cert-auth"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogSettingsClientCertAuthGetItem:
    """Item yielded when iterating over CliGlobalSystemLogSettingsClientCertAuthGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def mode(self) -> Literal["basic", "strict"]: ...
    @property
    def tls_port(self) -> Literal["both", "514", "6514"]: ...
    @property
    def trusted_client(self) -> list[TrustedClientItem]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class TrustedClientItem:
    """Nested item type for trusted-client array."""

    @property
    def certificate(self) -> list[Any]: ...
    @property
    def description(self) -> str: ...
    @property
    def domain(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def type(self) -> Literal["certificate", "domain"]: ...


class CliGlobalSystemLogSettingsClientCertAuthGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogSettingsClientCertAuthGet endpoint with autocomplete support."""

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
    def mode(self) -> Literal["basic", "strict"] | None:
        """Field: mode"""
        ...

    @property
    def tls_port(self) -> Literal["both", "514", "6514"] | None:
        """Field: tls-port"""
        ...

    @property
    def trusted_client(self) -> list[TrustedClientItem]:
        """Field: trusted-client"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogSettingsClientCertAuthGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogSettingsClientCertAuth:
    """FortiAnalyzer endpoint: cli.global.system.log.settings.client-cert-auth"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogSettingsClientCertAuthGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        mode: Literal["basic", "strict"] | None = None,
        tls_port: Literal["both", "514", "6514"] | None = None,
        trusted_client: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        mode: Literal["basic", "strict"] | None = None,
        tls_port: Literal["both", "514", "6514"] | None = None,
        trusted_client: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogSettingsClientCertAuth", "CliGlobalSystemLogSettingsClientCertAuthGetResponse"]
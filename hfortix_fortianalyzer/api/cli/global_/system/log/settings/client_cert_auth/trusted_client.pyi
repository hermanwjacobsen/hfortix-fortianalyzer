"""Type stubs for cli.global.system.log.settings.client-cert-auth.trusted-client"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogSettingsClientCertAuthTrustedClientGetItem:
    """Item yielded when iterating over CliGlobalSystemLogSettingsClientCertAuthTrustedClientGetResponse."""

    @property
    def oid(self) -> int: ...
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

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogSettingsClientCertAuthTrustedClientGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogSettingsClientCertAuthTrustedClientGet endpoint with autocomplete support."""

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
    def certificate(self) -> list[Any] | None:
        """Field: certificate"""
        ...

    @property
    def description(self) -> str | None:
        """Field: description"""
        ...

    @property
    def domain(self) -> str | None:
        """Field: domain"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def type(self) -> Literal["certificate", "domain"] | None:
        """Field: type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogSettingsClientCertAuthTrustedClientGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogSettingsClientCertAuthTrustedClient:
    """FortiAnalyzer endpoint: cli.global.system.log.settings.client-cert-auth.trusted-client"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        trusted_client: int | str | None = None,
        fields: list[Literal["certificate", "description", "domain", "id", "type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLogSettingsClientCertAuthTrustedClientGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        trusted_client: int | str | None = None,
        certificate: list[Any] | None = None,
        description: str | None = None,
        domain: str | None = None,
        id: int | None = None,
        type: Literal["certificate", "domain"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        trusted_client: int | str | None = None,
        certificate: list[Any] | None = None,
        description: str | None = None,
        domain: str | None = None,
        id: int | None = None,
        type: Literal["certificate", "domain"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        trusted_client: int | str | None = None,
        certificate: list[Any] | None = None,
        description: str | None = None,
        domain: str | None = None,
        id: int | None = None,
        type: Literal["certificate", "domain"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        trusted_client: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLogSettingsClientCertAuthTrustedClient", "CliGlobalSystemLogSettingsClientCertAuthTrustedClientGetResponse"]
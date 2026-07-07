"""Type stubs for cli.global.system.certificate.oftp"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCertificateOftpGetItem:
    """Item yielded when iterating over CliGlobalSystemCertificateOftpGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def certificate(self) -> list[Any]: ...
    @property
    def comment(self) -> str: ...
    @property
    def local(self) -> str: ...
    @property
    def mode(self) -> Literal["default", "custom", "local"]: ...
    @property
    def password(self) -> list[Any]: ...
    @property
    def private_key(self) -> list[Any]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemCertificateOftpGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCertificateOftpGet endpoint with autocomplete support."""

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
    def comment(self) -> str | None:
        """Field: comment"""
        ...

    @property
    def local(self) -> str | None:
        """Field: local"""
        ...

    @property
    def mode(self) -> Literal["default", "custom", "local"] | None:
        """Field: mode"""
        ...

    @property
    def password(self) -> list[Any] | None:
        """Field: password"""
        ...

    @property
    def private_key(self) -> list[Any] | None:
        """Field: private-key"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemCertificateOftpGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCertificateOftp:
    """FortiAnalyzer endpoint: cli.global.system.certificate.oftp"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemCertificateOftpGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        local: str | None = None,
        mode: Literal["default", "custom", "local"] | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        local: str | None = None,
        mode: Literal["default", "custom", "local"] | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemCertificateOftp", "CliGlobalSystemCertificateOftpGetResponse"]
"""Type stubs for cli.global.system.certificate.local"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCertificateLocalGetItem:
    """Item yielded when iterating over CliGlobalSystemCertificateLocalGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def certificate(self) -> list[Any]: ...
    @property
    def comment(self) -> str: ...
    @property
    def csr(self) -> list[Any]: ...
    @property
    def name(self) -> str: ...
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


class CliGlobalSystemCertificateLocalGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCertificateLocalGet endpoint with autocomplete support."""

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
    def csr(self) -> list[Any] | None:
        """Field: csr"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemCertificateLocalGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCertificateLocal:
    """FortiAnalyzer endpoint: cli.global.system.certificate.local"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        local: int | str | None = None,
        fields: list[Literal["certificate", "comment", "csr", "name", "password", "private-key"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemCertificateLocalGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        local: int | str | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        csr: list[Any] | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        local: int | str | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        csr: list[Any] | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        local: int | str | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        csr: list[Any] | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        local: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemCertificateLocal", "CliGlobalSystemCertificateLocalGetResponse"]
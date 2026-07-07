"""Type stubs for cli.global.system.certificate.ssh"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCertificateSshGetItem:
    """Item yielded when iterating over CliGlobalSystemCertificateSshGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def certificate(self) -> list[Any]: ...
    @property
    def comment(self) -> str: ...
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


class CliGlobalSystemCertificateSshGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCertificateSshGet endpoint with autocomplete support."""

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
    def __iter__(self) -> Iterator[CliGlobalSystemCertificateSshGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCertificateSsh:
    """FortiAnalyzer endpoint: cli.global.system.certificate.ssh"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        ssh: int | str | None = None,
        fields: list[Literal["certificate", "comment", "name", "password", "private-key"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemCertificateSshGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        ssh: int | str | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        ssh: int | str | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        ssh: int | str | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        ssh: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemCertificateSsh", "CliGlobalSystemCertificateSshGetResponse"]
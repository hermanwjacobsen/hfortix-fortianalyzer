"""Type stubs for cli.global.system.certificate.remote"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCertificateRemoteGetItem:
    """Item yielded when iterating over CliGlobalSystemCertificateRemoteGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def cert(self) -> list[Any]: ...
    @property
    def comment(self) -> str: ...
    @property
    def name(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemCertificateRemoteGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCertificateRemoteGet endpoint with autocomplete support."""

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
    def cert(self) -> list[Any] | None:
        """Field: cert"""
        ...

    @property
    def comment(self) -> str | None:
        """Field: comment"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemCertificateRemoteGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCertificateRemote:
    """FortiAnalyzer endpoint: cli.global.system.certificate.remote"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        remote: int | str | None = None,
        fields: list[Literal["cert", "comment", "name"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemCertificateRemoteGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        remote: int | str | None = None,
        cert: list[Any] | None = None,
        comment: str | None = None,
        name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        remote: int | str | None = None,
        cert: list[Any] | None = None,
        comment: str | None = None,
        name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        remote: int | str | None = None,
        cert: list[Any] | None = None,
        comment: str | None = None,
        name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        remote: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemCertificateRemote", "CliGlobalSystemCertificateRemoteGetResponse"]
"""Type stubs for cli.global.system.certificate.ca"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCertificateCaGetItem:
    """Item yielded when iterating over CliGlobalSystemCertificateCaGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def ca(self) -> list[Any]: ...
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


class CliGlobalSystemCertificateCaGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCertificateCaGet endpoint with autocomplete support."""

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
    def ca(self) -> list[Any] | None:
        """Field: ca"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemCertificateCaGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCertificateCa:
    """FortiAnalyzer endpoint: cli.global.system.certificate.ca"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        ca: int | str | None = None,
        fields: list[Literal["ca", "comment", "name"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemCertificateCaGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        ca: int | str | None = None,
        comment: str | None = None,
        name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        ca: int | str | None = None,
        comment: str | None = None,
        name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        ca: int | str | None = None,
        comment: str | None = None,
        name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        ca: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemCertificateCa", "CliGlobalSystemCertificateCaGetResponse"]
"""Type stubs for cli.global.system.certificate.crl"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCertificateCrlGetItem:
    """Item yielded when iterating over CliGlobalSystemCertificateCrlGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def comment(self) -> str: ...
    @property
    def crl(self) -> list[Any]: ...
    @property
    def http_url(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def update_interval(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemCertificateCrlGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCertificateCrlGet endpoint with autocomplete support."""

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
    def comment(self) -> str | None:
        """Field: comment"""
        ...

    @property
    def crl(self) -> list[Any] | None:
        """Field: crl"""
        ...

    @property
    def http_url(self) -> str | None:
        """Field: http-url"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def update_interval(self) -> int | None:
        """Field: update-interval"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemCertificateCrlGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCertificateCrl:
    """FortiAnalyzer endpoint: cli.global.system.certificate.crl"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        crl: int | str | None = None,
        fields: list[Literal["comment", "crl", "http-url", "name", "update-interval"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemCertificateCrlGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        crl: int | str | None = None,
        comment: str | None = None,
        http_url: str | None = None,
        name: str | None = None,
        update_interval: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        crl: int | str | None = None,
        comment: str | None = None,
        http_url: str | None = None,
        name: str | None = None,
        update_interval: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        crl: int | str | None = None,
        comment: str | None = None,
        http_url: str | None = None,
        name: str | None = None,
        update_interval: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        crl: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemCertificateCrl", "CliGlobalSystemCertificateCrlGetResponse"]
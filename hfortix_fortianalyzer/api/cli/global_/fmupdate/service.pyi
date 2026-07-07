"""Type stubs for cli.global.fmupdate.service"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateServiceGetItem:
    """Item yielded when iterating over CliGlobalFmupdateServiceGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def avips(self) -> Literal["disable", "enable"]: ...
    @property
    def geoip(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalFmupdateServiceGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateServiceGet endpoint with autocomplete support."""

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
    def avips(self) -> Literal["disable", "enable"] | None:
        """Field: avips"""
        ...

    @property
    def geoip(self) -> Literal["disable", "enable"] | None:
        """Field: geoip"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateServiceGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateService:
    """FortiAnalyzer endpoint: cli.global.fmupdate.service"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateServiceGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        avips: Literal["disable", "enable"] | None = None,
        geoip: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        avips: Literal["disable", "enable"] | None = None,
        geoip: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateService", "CliGlobalFmupdateServiceGetResponse"]
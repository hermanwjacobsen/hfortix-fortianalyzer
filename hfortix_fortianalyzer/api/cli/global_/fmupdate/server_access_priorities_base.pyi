"""Type stubs for cli.global.fmupdate.server-access-priorities"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateServerAccessPrioritiesGetItem:
    """Item yielded when iterating over CliGlobalFmupdateServerAccessPrioritiesGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def access_public(self) -> Literal["disable", "enable"]: ...
    @property
    def av_ips(self) -> Literal["disable", "enable"]: ...
    @property
    def private_server(self) -> list[PrivateServerItem]: ...
    @property
    def web_spam(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class PrivateServerItem:
    """Nested item type for private-server array."""

    @property
    def id(self) -> int: ...
    @property
    def ip(self) -> str: ...
    @property
    def ip6(self) -> str: ...
    @property
    def time_zone(self) -> int: ...


class CliGlobalFmupdateServerAccessPrioritiesGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateServerAccessPrioritiesGet endpoint with autocomplete support."""

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
    def access_public(self) -> Literal["disable", "enable"] | None:
        """Field: access-public"""
        ...

    @property
    def av_ips(self) -> Literal["disable", "enable"] | None:
        """Field: av-ips"""
        ...

    @property
    def private_server(self) -> list[PrivateServerItem]:
        """Field: private-server"""
        ...

    @property
    def web_spam(self) -> Literal["disable", "enable"] | None:
        """Field: web-spam"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateServerAccessPrioritiesGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateServerAccessPriorities:
    """FortiAnalyzer endpoint: cli.global.fmupdate.server-access-priorities"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateServerAccessPrioritiesGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        access_public: Literal["disable", "enable"] | None = None,
        av_ips: Literal["disable", "enable"] | None = None,
        private_server: list[dict[str, Any]] | None = None,
        web_spam: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        access_public: Literal["disable", "enable"] | None = None,
        av_ips: Literal["disable", "enable"] | None = None,
        private_server: list[dict[str, Any]] | None = None,
        web_spam: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateServerAccessPriorities", "CliGlobalFmupdateServerAccessPrioritiesGetResponse"]
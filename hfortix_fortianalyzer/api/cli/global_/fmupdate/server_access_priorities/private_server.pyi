"""Type stubs for cli.global.fmupdate.server-access-priorities.private-server"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateServerAccessPrioritiesPrivateServerGetItem:
    """Item yielded when iterating over CliGlobalFmupdateServerAccessPrioritiesPrivateServerGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def ip(self) -> str: ...
    @property
    def ip6(self) -> str: ...
    @property
    def time_zone(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalFmupdateServerAccessPrioritiesPrivateServerGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateServerAccessPrioritiesPrivateServerGet endpoint with autocomplete support."""

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
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def ip(self) -> str | None:
        """Field: ip"""
        ...

    @property
    def ip6(self) -> str | None:
        """Field: ip6"""
        ...

    @property
    def time_zone(self) -> int | None:
        """Field: time_zone"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateServerAccessPrioritiesPrivateServerGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateServerAccessPrioritiesPrivateServer:
    """FortiAnalyzer endpoint: cli.global.fmupdate.server-access-priorities.private-server"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        private_server: int | str | None = None,
        fields: list[Literal["id", "ip", "ip6", "time_zone"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalFmupdateServerAccessPrioritiesPrivateServerGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        private_server: int | str | None = None,
        id: int | None = None,
        ip: str | None = None,
        ip6: str | None = None,
        time_zone: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        private_server: int | str | None = None,
        id: int | None = None,
        ip: str | None = None,
        ip6: str | None = None,
        time_zone: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        private_server: int | str | None = None,
        id: int | None = None,
        ip: str | None = None,
        ip6: str | None = None,
        time_zone: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        private_server: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalFmupdateServerAccessPrioritiesPrivateServer", "CliGlobalFmupdateServerAccessPrioritiesPrivateServerGetResponse"]
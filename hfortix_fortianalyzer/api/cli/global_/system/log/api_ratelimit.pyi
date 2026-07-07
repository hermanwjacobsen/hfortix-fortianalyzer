"""Type stubs for cli.global.system.log.api-ratelimit"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogApiRatelimitGetItem:
    """Item yielded when iterating over CliGlobalSystemLogApiRatelimitGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def read_limit(self) -> int: ...
    @property
    def write_limit(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogApiRatelimitGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogApiRatelimitGet endpoint with autocomplete support."""

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
    def read_limit(self) -> int | None:
        """Field: read-limit"""
        ...

    @property
    def write_limit(self) -> int | None:
        """Field: write-limit"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogApiRatelimitGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogApiRatelimit:
    """FortiAnalyzer endpoint: cli.global.system.log.api-ratelimit"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogApiRatelimitGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        read_limit: int | None = None,
        write_limit: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        read_limit: int | None = None,
        write_limit: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogApiRatelimit", "CliGlobalSystemLogApiRatelimitGetResponse"]
"""Type stubs for cli.global.system.log.ratelimit.ratelimits"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogRatelimitRatelimitsGetItem:
    """Item yielded when iterating over CliGlobalSystemLogRatelimitRatelimitsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def filter(self) -> str: ...
    @property
    def filter_type(self) -> Literal["devid", "adom"]: ...
    @property
    def id(self) -> int: ...
    @property
    def ratelimit(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogRatelimitRatelimitsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogRatelimitRatelimitsGet endpoint with autocomplete support."""

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
    def filter(self) -> str | None:
        """Field: filter"""
        ...

    @property
    def filter_type(self) -> Literal["devid", "adom"] | None:
        """Field: filter-type"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def ratelimit(self) -> int | None:
        """Field: ratelimit"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogRatelimitRatelimitsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogRatelimitRatelimits:
    """FortiAnalyzer endpoint: cli.global.system.log.ratelimit.ratelimits"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        ratelimits: int | str | None = None,
        fields: list[Literal["filter", "filter-type", "id", "ratelimit"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLogRatelimitRatelimitsGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        ratelimits: int | str | None = None,
        filter: str | None = None,
        filter_type: Literal["devid", "adom"] | None = None,
        id: int | None = None,
        ratelimit: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        ratelimits: int | str | None = None,
        filter: str | None = None,
        filter_type: Literal["devid", "adom"] | None = None,
        id: int | None = None,
        ratelimit: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        ratelimits: int | str | None = None,
        filter: str | None = None,
        filter_type: Literal["devid", "adom"] | None = None,
        id: int | None = None,
        ratelimit: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        ratelimits: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLogRatelimitRatelimits", "CliGlobalSystemLogRatelimitRatelimitsGetResponse"]
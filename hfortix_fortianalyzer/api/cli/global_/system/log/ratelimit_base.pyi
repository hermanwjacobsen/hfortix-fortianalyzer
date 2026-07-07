"""Type stubs for cli.global.system.log.ratelimit"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogRatelimitGetItem:
    """Item yielded when iterating over CliGlobalSystemLogRatelimitGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def device_ratelimit_default(self) -> int: ...
    @property
    def mode(self) -> Literal["disable", "manual"]: ...
    @property
    def ratelimits(self) -> list[RatelimitsItem]: ...
    @property
    def system_ratelimit(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class RatelimitsItem:
    """Nested item type for ratelimits array."""

    @property
    def filter(self) -> str: ...
    @property
    def filter_type(self) -> Literal["devid", "adom"]: ...
    @property
    def id(self) -> int: ...
    @property
    def ratelimit(self) -> int: ...


class CliGlobalSystemLogRatelimitGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogRatelimitGet endpoint with autocomplete support."""

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
    def device_ratelimit_default(self) -> int | None:
        """Field: device-ratelimit-default"""
        ...

    @property
    def mode(self) -> Literal["disable", "manual"] | None:
        """Field: mode"""
        ...

    @property
    def ratelimits(self) -> list[RatelimitsItem]:
        """Field: ratelimits"""
        ...

    @property
    def system_ratelimit(self) -> int | None:
        """Field: system-ratelimit"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogRatelimitGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogRatelimit:
    """FortiAnalyzer endpoint: cli.global.system.log.ratelimit"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogRatelimitGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        device_ratelimit_default: int | None = None,
        mode: Literal["disable", "manual"] | None = None,
        ratelimits: list[dict[str, Any]] | None = None,
        system_ratelimit: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        device_ratelimit_default: int | None = None,
        mode: Literal["disable", "manual"] | None = None,
        ratelimits: list[dict[str, Any]] | None = None,
        system_ratelimit: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogRatelimit", "CliGlobalSystemLogRatelimitGetResponse"]
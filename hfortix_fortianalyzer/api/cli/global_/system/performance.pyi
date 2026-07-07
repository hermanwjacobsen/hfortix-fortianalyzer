"""Type stubs for cli.global.system.performance"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemPerformanceGetItem:
    """Item yielded when iterating over CliGlobalSystemPerformanceGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def CPU(self) -> dict[str, Any]: ...
    @property
    def Flash_Disk(self) -> dict[str, Any]: ...
    @property
    def Hard_Disk(self) -> dict[str, Any]: ...
    @property
    def Memory(self) -> dict[str, Any]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemPerformanceGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemPerformanceGet endpoint with autocomplete support."""

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
    def CPU(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.performance.CPU)."""
        ...

    @property
    def Flash_Disk(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.performance.Flash.Disk)."""
        ...

    @property
    def Hard_Disk(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.performance.Hard.Disk)."""
        ...

    @property
    def Memory(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.performance.Memory)."""
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
    def __iter__(self) -> Iterator[CliGlobalSystemPerformanceGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemPerformance:
    """FortiAnalyzer endpoint: cli.global.system.performance"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemPerformanceGetResponse:
        """GET operation."""
        ...


__all__ = ["CliGlobalSystemPerformance", "CliGlobalSystemPerformanceGetResponse"]
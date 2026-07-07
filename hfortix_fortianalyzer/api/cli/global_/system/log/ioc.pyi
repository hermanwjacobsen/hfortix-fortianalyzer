"""Type stubs for cli.global.system.log.ioc"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogIocGetItem:
    """Item yielded when iterating over CliGlobalSystemLogIocGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def notification(self) -> Literal["disable", "enable"]: ...
    @property
    def notification_throttle(self) -> int: ...
    @property
    def rescan_max_runner(self) -> int: ...
    @property
    def rescan_run_at(self) -> int: ...
    @property
    def rescan_status(self) -> Literal["disable", "enable"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogIocGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogIocGet endpoint with autocomplete support."""

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
    def notification(self) -> Literal["disable", "enable"] | None:
        """Field: notification"""
        ...

    @property
    def notification_throttle(self) -> int | None:
        """Field: notification-throttle"""
        ...

    @property
    def rescan_max_runner(self) -> int | None:
        """Field: rescan-max-runner"""
        ...

    @property
    def rescan_run_at(self) -> int | None:
        """Field: rescan-run-at"""
        ...

    @property
    def rescan_status(self) -> Literal["disable", "enable"] | None:
        """Field: rescan-status"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogIocGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogIoc:
    """FortiAnalyzer endpoint: cli.global.system.log.ioc"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogIocGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        notification: Literal["disable", "enable"] | None = None,
        notification_throttle: int | None = None,
        rescan_max_runner: int | None = None,
        rescan_run_at: int | None = None,
        rescan_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        notification: Literal["disable", "enable"] | None = None,
        notification_throttle: int | None = None,
        rescan_max_runner: int | None = None,
        rescan_run_at: int | None = None,
        rescan_status: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogIoc", "CliGlobalSystemLogIocGetResponse"]
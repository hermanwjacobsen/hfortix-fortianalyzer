"""Type stubs for cli.global.system.locallog.setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogSettingGetItem:
    """Item yielded when iterating over CliGlobalSystemLocallogSettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def log_daemon_crash(self) -> Literal["disable", "enable"]: ...
    @property
    def log_interval_adom_perf_stats(self) -> int: ...
    @property
    def log_interval_dev_no_logging(self) -> int: ...
    @property
    def log_interval_disk_full(self) -> int: ...
    @property
    def log_interval_gbday_exceeded(self) -> int: ...
    @property
    def no_log_detection_threshold(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocallogSettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocallogSettingGet endpoint with autocomplete support."""

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
    def log_daemon_crash(self) -> Literal["disable", "enable"] | None:
        """Field: log-daemon-crash"""
        ...

    @property
    def log_interval_adom_perf_stats(self) -> int | None:
        """Field: log-interval-adom-perf-stats"""
        ...

    @property
    def log_interval_dev_no_logging(self) -> int | None:
        """Field: log-interval-dev-no-logging"""
        ...

    @property
    def log_interval_disk_full(self) -> int | None:
        """Field: log-interval-disk-full"""
        ...

    @property
    def log_interval_gbday_exceeded(self) -> int | None:
        """Field: log-interval-gbday-exceeded"""
        ...

    @property
    def no_log_detection_threshold(self) -> int | None:
        """Field: no-log-detection-threshold"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocallogSettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocallogSetting:
    """FortiAnalyzer endpoint: cli.global.system.locallog.setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLocallogSettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        log_daemon_crash: Literal["disable", "enable"] | None = None,
        log_interval_adom_perf_stats: int | None = None,
        log_interval_dev_no_logging: int | None = None,
        log_interval_disk_full: int | None = None,
        log_interval_gbday_exceeded: int | None = None,
        no_log_detection_threshold: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        log_daemon_crash: Literal["disable", "enable"] | None = None,
        log_interval_adom_perf_stats: int | None = None,
        log_interval_dev_no_logging: int | None = None,
        log_interval_disk_full: int | None = None,
        log_interval_gbday_exceeded: int | None = None,
        no_log_detection_threshold: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLocallogSetting", "CliGlobalSystemLocallogSettingGetResponse"]
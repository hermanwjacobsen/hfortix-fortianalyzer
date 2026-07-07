"""Type stubs for cli.global.system.admin.user.dashboard"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminUserDashboardGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminUserDashboardGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def column(self) -> int: ...
    @property
    def diskio_content_type(self) -> Literal["util", "iops", "blks"]: ...
    @property
    def diskio_period(self) -> Literal["1hour", "8hour", "24hour"]: ...
    @property
    def log_rate_period(self) -> Literal["2min ", "1hour", "6hours"]: ...
    @property
    def log_rate_topn(self) -> Literal["1", "2", "3", "4", "5"]: ...
    @property
    def log_rate_type(self) -> Literal["log", "device"]: ...
    @property
    def moduleid(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def num_entries(self) -> int: ...
    @property
    def refresh_interval(self) -> int: ...
    @property
    def res_cpu_display(self) -> Literal["average ", "each"]: ...
    @property
    def res_period(self) -> Literal["10min ", "hour", "day"]: ...
    @property
    def res_view_type(self) -> Literal["real-time ", "history"]: ...
    @property
    def status(self) -> Literal["close", "open"]: ...
    @property
    def tabid(self) -> int: ...
    @property
    def time_period(self) -> Literal["1hour", "8hour", "24hour"]: ...
    @property
    def widget_type(self) -> Literal["top-lograte", "sysres", "sysinfo", "licinfo", "jsconsole", "sysop", "alert", "statistics", "rpteng", "raid", "logrecv", "devsummary", "logdb-perf", "logdb-lag", "disk-io", "log-rcvd-fwd"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAdminUserDashboardGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminUserDashboardGet endpoint with autocomplete support."""

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
    def column(self) -> int | None:
        """Field: column"""
        ...

    @property
    def diskio_content_type(self) -> Literal["util", "iops", "blks"] | None:
        """Field: diskio-content-type"""
        ...

    @property
    def diskio_period(self) -> Literal["1hour", "8hour", "24hour"] | None:
        """Field: diskio-period"""
        ...

    @property
    def log_rate_period(self) -> Literal["2min ", "1hour", "6hours"] | None:
        """Field: log-rate-period"""
        ...

    @property
    def log_rate_topn(self) -> Literal["1", "2", "3", "4", "5"] | None:
        """Field: log-rate-topn"""
        ...

    @property
    def log_rate_type(self) -> Literal["log", "device"] | None:
        """Field: log-rate-type"""
        ...

    @property
    def moduleid(self) -> int | None:
        """Field: moduleid"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def num_entries(self) -> int | None:
        """Field: num-entries"""
        ...

    @property
    def refresh_interval(self) -> int | None:
        """Field: refresh-interval"""
        ...

    @property
    def res_cpu_display(self) -> Literal["average ", "each"] | None:
        """Field: res-cpu-display"""
        ...

    @property
    def res_period(self) -> Literal["10min ", "hour", "day"] | None:
        """Field: res-period"""
        ...

    @property
    def res_view_type(self) -> Literal["real-time ", "history"] | None:
        """Field: res-view-type"""
        ...

    @property
    def status(self) -> Literal["close", "open"] | None:
        """Field: status"""
        ...

    @property
    def tabid(self) -> int | None:
        """Field: tabid"""
        ...

    @property
    def time_period(self) -> Literal["1hour", "8hour", "24hour"] | None:
        """Field: time-period"""
        ...

    @property
    def widget_type(self) -> Literal["top-lograte", "sysres", "sysinfo", "licinfo", "jsconsole", "sysop", "alert", "statistics", "rpteng", "raid", "logrecv", "devsummary", "logdb-perf", "logdb-lag", "disk-io", "log-rcvd-fwd"] | None:
        """Field: widget-type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminUserDashboardGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminUserDashboard:
    """FortiAnalyzer endpoint: cli.global.system.admin.user.dashboard"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        user: str,
        dashboard: int | str | None = None,
        fields: list[Literal["column", "diskio-content-type", "diskio-period", "log-rate-period", "log-rate-topn", "log-rate-type", "moduleid", "name", "num-entries", "refresh-interval", "res-cpu-display", "res-period", "res-view-type", "status", "tabid", "time-period", "widget-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminUserDashboardGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        user: str,
        dashboard: int | str | None = None,
        column: int | None = None,
        diskio_content_type: Literal["util", "iops", "blks"] | None = None,
        diskio_period: Literal["1hour", "8hour", "24hour"] | None = None,
        log_rate_period: Literal["2min ", "1hour", "6hours"] | None = None,
        log_rate_topn: Literal["1", "2", "3", "4", "5"] | None = None,
        log_rate_type: Literal["log", "device"] | None = None,
        moduleid: int | None = None,
        name: str | None = None,
        num_entries: int | None = None,
        refresh_interval: int | None = None,
        res_cpu_display: Literal["average ", "each"] | None = None,
        res_period: Literal["10min ", "hour", "day"] | None = None,
        res_view_type: Literal["real-time ", "history"] | None = None,
        status: Literal["close", "open"] | None = None,
        tabid: int | None = None,
        time_period: Literal["1hour", "8hour", "24hour"] | None = None,
        widget_type: Literal["top-lograte", "sysres", "sysinfo", "licinfo", "jsconsole", "sysop", "alert", "statistics", "rpteng", "raid", "logrecv", "devsummary", "logdb-perf", "logdb-lag", "disk-io", "log-rcvd-fwd"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        user: str,
        dashboard: int | str | None = None,
        column: int | None = None,
        diskio_content_type: Literal["util", "iops", "blks"] | None = None,
        diskio_period: Literal["1hour", "8hour", "24hour"] | None = None,
        log_rate_period: Literal["2min ", "1hour", "6hours"] | None = None,
        log_rate_topn: Literal["1", "2", "3", "4", "5"] | None = None,
        log_rate_type: Literal["log", "device"] | None = None,
        moduleid: int | None = None,
        name: str | None = None,
        num_entries: int | None = None,
        refresh_interval: int | None = None,
        res_cpu_display: Literal["average ", "each"] | None = None,
        res_period: Literal["10min ", "hour", "day"] | None = None,
        res_view_type: Literal["real-time ", "history"] | None = None,
        status: Literal["close", "open"] | None = None,
        tabid: int | None = None,
        time_period: Literal["1hour", "8hour", "24hour"] | None = None,
        widget_type: Literal["top-lograte", "sysres", "sysinfo", "licinfo", "jsconsole", "sysop", "alert", "statistics", "rpteng", "raid", "logrecv", "devsummary", "logdb-perf", "logdb-lag", "disk-io", "log-rcvd-fwd"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        user: str,
        dashboard: int | str | None = None,
        column: int | None = None,
        diskio_content_type: Literal["util", "iops", "blks"] | None = None,
        diskio_period: Literal["1hour", "8hour", "24hour"] | None = None,
        log_rate_period: Literal["2min ", "1hour", "6hours"] | None = None,
        log_rate_topn: Literal["1", "2", "3", "4", "5"] | None = None,
        log_rate_type: Literal["log", "device"] | None = None,
        moduleid: int | None = None,
        name: str | None = None,
        num_entries: int | None = None,
        refresh_interval: int | None = None,
        res_cpu_display: Literal["average ", "each"] | None = None,
        res_period: Literal["10min ", "hour", "day"] | None = None,
        res_view_type: Literal["real-time ", "history"] | None = None,
        status: Literal["close", "open"] | None = None,
        tabid: int | None = None,
        time_period: Literal["1hour", "8hour", "24hour"] | None = None,
        widget_type: Literal["top-lograte", "sysres", "sysinfo", "licinfo", "jsconsole", "sysop", "alert", "statistics", "rpteng", "raid", "logrecv", "devsummary", "logdb-perf", "logdb-lag", "disk-io", "log-rcvd-fwd"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        user: str,
        dashboard: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminUserDashboard", "CliGlobalSystemAdminUserDashboardGetResponse"]
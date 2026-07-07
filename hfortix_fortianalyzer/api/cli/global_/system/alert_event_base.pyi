"""Type stubs for cli.global.system.alert-event"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAlertEventGetItem:
    """Item yielded when iterating over CliGlobalSystemAlertEventGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def alert_destination(self) -> list[AlertDestinationItem]: ...
    @property
    def enable_generic_text(self) -> Literal["disable", "enable"]: ...
    @property
    def enable_severity_filter(self) -> Literal["disable", "enable"]: ...
    @property
    def event_time_period(self) -> Literal["0.5", "1", "3", "6", "12", "24", "72", "168"]: ...
    @property
    def generic_text(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def num_events(self) -> Literal["1", "5", "10", "50", "100"]: ...
    @property
    def severity_filter(self) -> Literal["high", "medium-high", "medium", "medium-low", "low"]: ...
    @property
    def severity_level_comp(self) -> Literal["=", ">=", "<="]: ...
    @property
    def severity_level_logs(self) -> list[Any]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class AlertDestinationItem:
    """Nested item type for alert-destination array."""

    @property
    def from_(self) -> str: ...
    @property
    def smtp_name(self) -> str: ...
    @property
    def snmp_name(self) -> str: ...
    @property
    def syslog_name(self) -> str: ...
    @property
    def to(self) -> str: ...
    @property
    def type(self) -> Literal["mail", "snmp", "syslog"]: ...


class CliGlobalSystemAlertEventGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAlertEventGet endpoint with autocomplete support."""

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
    def alert_destination(self) -> list[AlertDestinationItem]:
        """Field: alert-destination"""
        ...

    @property
    def enable_generic_text(self) -> Literal["disable", "enable"] | None:
        """Field: enable-generic-text"""
        ...

    @property
    def enable_severity_filter(self) -> Literal["disable", "enable"] | None:
        """Field: enable-severity-filter"""
        ...

    @property
    def event_time_period(self) -> Literal["0.5", "1", "3", "6", "12", "24", "72", "168"] | None:
        """Field: event-time-period"""
        ...

    @property
    def generic_text(self) -> str | None:
        """Field: generic-text"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def num_events(self) -> Literal["1", "5", "10", "50", "100"] | None:
        """Field: num-events"""
        ...

    @property
    def severity_filter(self) -> Literal["high", "medium-high", "medium", "medium-low", "low"] | None:
        """Field: severity-filter"""
        ...

    @property
    def severity_level_comp(self) -> Literal["=", ">=", "<="] | None:
        """Field: severity-level-comp"""
        ...

    @property
    def severity_level_logs(self) -> list[Any] | None:
        """Field: severity-level-logs"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAlertEventGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAlertEvent:
    """FortiAnalyzer endpoint: cli.global.system.alert-event"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        alert_event: int | str | None = None,
        fields: list[Literal["enable-generic-text", "enable-severity-filter", "event-time-period", "generic-text", "name", "num-events", "severity-filter", "severity-level-comp", "severity-level-logs"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAlertEventGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        alert_event: int | str | None = None,
        alert_destination: list[dict[str, Any]] | None = None,
        enable_generic_text: Literal["disable", "enable"] | None = None,
        enable_severity_filter: Literal["disable", "enable"] | None = None,
        event_time_period: Literal["0.5", "1", "3", "6", "12", "24", "72", "168"] | None = None,
        generic_text: str | None = None,
        name: str | None = None,
        num_events: Literal["1", "5", "10", "50", "100"] | None = None,
        severity_filter: Literal["high", "medium-high", "medium", "medium-low", "low"] | None = None,
        severity_level_comp: Literal["=", ">=", "<="] | None = None,
        severity_level_logs: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        alert_event: int | str | None = None,
        alert_destination: list[dict[str, Any]] | None = None,
        enable_generic_text: Literal["disable", "enable"] | None = None,
        enable_severity_filter: Literal["disable", "enable"] | None = None,
        event_time_period: Literal["0.5", "1", "3", "6", "12", "24", "72", "168"] | None = None,
        generic_text: str | None = None,
        name: str | None = None,
        num_events: Literal["1", "5", "10", "50", "100"] | None = None,
        severity_filter: Literal["high", "medium-high", "medium", "medium-low", "low"] | None = None,
        severity_level_comp: Literal["=", ">=", "<="] | None = None,
        severity_level_logs: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        alert_event: int | str | None = None,
        alert_destination: list[dict[str, Any]] | None = None,
        enable_generic_text: Literal["disable", "enable"] | None = None,
        enable_severity_filter: Literal["disable", "enable"] | None = None,
        event_time_period: Literal["0.5", "1", "3", "6", "12", "24", "72", "168"] | None = None,
        generic_text: str | None = None,
        name: str | None = None,
        num_events: Literal["1", "5", "10", "50", "100"] | None = None,
        severity_filter: Literal["high", "medium-high", "medium", "medium-low", "low"] | None = None,
        severity_level_comp: Literal["=", ">=", "<="] | None = None,
        severity_level_logs: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        alert_event: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAlertEvent", "CliGlobalSystemAlertEventGetResponse"]
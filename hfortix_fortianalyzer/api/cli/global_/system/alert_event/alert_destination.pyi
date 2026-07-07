"""Type stubs for cli.global.system.alert-event.alert-destination"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAlertEventAlertDestinationGetItem:
    """Item yielded when iterating over CliGlobalSystemAlertEventAlertDestinationGetResponse."""

    @property
    def oid(self) -> int: ...
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

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAlertEventAlertDestinationGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAlertEventAlertDestinationGet endpoint with autocomplete support."""

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
    def from_(self) -> str | None:
        """Field: from"""
        ...

    @property
    def smtp_name(self) -> str | None:
        """Field: smtp-name"""
        ...

    @property
    def snmp_name(self) -> str | None:
        """Field: snmp-name"""
        ...

    @property
    def syslog_name(self) -> str | None:
        """Field: syslog-name"""
        ...

    @property
    def to(self) -> str | None:
        """Field: to"""
        ...

    @property
    def type(self) -> Literal["mail", "snmp", "syslog"] | None:
        """Field: type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAlertEventAlertDestinationGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAlertEventAlertDestination:
    """FortiAnalyzer endpoint: cli.global.system.alert-event.alert-destination"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        alert_event: str,
        alert_destination: int | str | None = None,
        fields: list[Literal["from", "smtp-name", "snmp-name", "syslog-name", "to", "type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAlertEventAlertDestinationGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        alert_event: str,
        alert_destination: int | str | None = None,
        from_: str | None = None,
        smtp_name: str | None = None,
        snmp_name: str | None = None,
        syslog_name: str | None = None,
        to: str | None = None,
        type: Literal["mail", "snmp", "syslog"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        alert_event: str,
        alert_destination: int | str | None = None,
        from_: str | None = None,
        smtp_name: str | None = None,
        snmp_name: str | None = None,
        syslog_name: str | None = None,
        to: str | None = None,
        type: Literal["mail", "snmp", "syslog"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        alert_event: str,
        alert_destination: int | str | None = None,
        from_: str | None = None,
        smtp_name: str | None = None,
        snmp_name: str | None = None,
        syslog_name: str | None = None,
        to: str | None = None,
        type: Literal["mail", "snmp", "syslog"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        alert_event: str,
        alert_destination: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAlertEventAlertDestination", "CliGlobalSystemAlertEventAlertDestinationGetResponse"]
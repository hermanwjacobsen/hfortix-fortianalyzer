"""Type stubs for cli.global.system.locallog.syslogd2.setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogSyslogd2SettingGetItem:
    """Item yielded when iterating over CliGlobalSystemLocallogSyslogd2SettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def csv(self) -> Literal["disable", "enable"]: ...
    @property
    def facility(self) -> Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]: ...
    @property
    def severity(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def syslog_name(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocallogSyslogd2SettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocallogSyslogd2SettingGet endpoint with autocomplete support."""

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
    def csv(self) -> Literal["disable", "enable"] | None:
        """Field: csv"""
        ...

    @property
    def facility(self) -> Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None:
        """Field: facility"""
        ...

    @property
    def severity(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None:
        """Field: severity"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def syslog_name(self) -> str | None:
        """Field: syslog-name"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocallogSyslogd2SettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocallogSyslogd2Setting:
    """FortiAnalyzer endpoint: cli.global.system.locallog.syslogd2.setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLocallogSyslogd2SettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        csv: Literal["disable", "enable"] | None = None,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        syslog_name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        csv: Literal["disable", "enable"] | None = None,
        facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        syslog_name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLocallogSyslogd2Setting", "CliGlobalSystemLocallogSyslogd2SettingGetResponse"]
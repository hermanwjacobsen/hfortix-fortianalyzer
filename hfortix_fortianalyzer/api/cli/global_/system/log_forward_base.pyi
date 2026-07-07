"""Type stubs for cli.global.system.log-forward"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogForwardGetItem:
    """Item yielded when iterating over CliGlobalSystemLogForwardGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def agg_archive_types(self) -> list[Any]: ...
    @property
    def agg_data_end_time(self) -> list[Any]: ...
    @property
    def agg_data_start_time(self) -> list[Any]: ...
    @property
    def agg_logtypes(self) -> list[Any]: ...
    @property
    def agg_password(self) -> list[Any]: ...
    @property
    def agg_schedule(self) -> Literal["daily", "on-demand"]: ...
    @property
    def agg_time(self) -> int: ...
    @property
    def agg_user(self) -> str: ...
    @property
    def device_filter(self) -> list[DeviceFilterItem]: ...
    @property
    def fwd_archive_types(self) -> list[Any]: ...
    @property
    def fwd_archives(self) -> Literal["disable", "enable"]: ...
    @property
    def fwd_compression(self) -> Literal["disable", "enable"]: ...
    @property
    def fwd_facility(self) -> Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "clock", "authpriv", "ftp", "ntp", "audit", "alert", "cron", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]: ...
    @property
    def fwd_ha_bind_vip(self) -> Literal["disable", "enable"]: ...
    @property
    def fwd_log_source_ip(self) -> Literal["local_ip", "original_ip"]: ...
    @property
    def fwd_max_delay(self) -> Literal["realtime", "1min", "5min"]: ...
    @property
    def fwd_output_plugin_id(self) -> str: ...
    @property
    def fwd_reliable(self) -> Literal["disable", "enable"]: ...
    @property
    def fwd_secure(self) -> Literal["disable", "enable"]: ...
    @property
    def fwd_server_type(self) -> Literal["syslog", "fortianalyzer", "cef", "syslog-pack", "fwd-via-output-plugin", "elite-service"]: ...
    @property
    def fwd_syslog_decode_b64(self) -> Literal["disable", "enable"]: ...
    @property
    def fwd_syslog_enrich_cve(self) -> Literal["disable", "enable"]: ...
    @property
    def fwd_syslog_format(self) -> Literal["fgt", "rfc-5424"]: ...
    @property
    def fwd_syslog_transparent(self) -> Literal["disable", "enable", "faz-enrich"]: ...
    @property
    def id(self) -> int: ...
    @property
    def log_field_exclusion(self) -> list[LogFieldExclusionItem]: ...
    @property
    def log_field_exclusion_status(self) -> Literal["disable", "enable"]: ...
    @property
    def log_filter(self) -> list[LogFilterItem]: ...
    @property
    def log_filter_logic(self) -> Literal["and", "or"]: ...
    @property
    def log_filter_status(self) -> Literal["disable", "enable"]: ...
    @property
    def log_masking_custom(self) -> list[LogMaskingCustomItem]: ...
    @property
    def log_masking_custom_priority(self) -> Literal["disable", "enable"]: ...
    @property
    def log_masking_fields(self) -> list[Any]: ...
    @property
    def log_masking_key(self) -> list[Any]: ...
    @property
    def log_masking_status(self) -> Literal["disable", "enable"]: ...
    @property
    def mode(self) -> Literal["forwarding", "aggregation", "disable"]: ...
    @property
    def pcapurl_domain_ip(self) -> str: ...
    @property
    def pcapurl_enrich(self) -> Literal["disable", "enable"]: ...
    @property
    def peer_cert_cn(self) -> str: ...
    @property
    def proxy_service(self) -> Literal["disable", "enable"]: ...
    @property
    def proxy_service_priority(self) -> int: ...
    @property
    def server_addr(self) -> str: ...
    @property
    def server_device(self) -> str: ...
    @property
    def server_name(self) -> str: ...
    @property
    def server_port(self) -> int: ...
    @property
    def signature(self) -> int: ...
    @property
    def sync_metadata(self) -> list[Any]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class DeviceFilterItem:
    """Nested item type for device-filter array."""

    @property
    def action(self) -> Literal["include", "exclude", "include-like", "exclude-like"]: ...
    @property
    def adom(self) -> str: ...
    @property
    def device(self) -> str: ...
    @property
    def id(self) -> int: ...

class LogFieldExclusionItem:
    """Nested item type for log-field-exclusion array."""

    @property
    def dev_type(self) -> Literal["FortiGate", "FortiManager", "Syslog", "FortiClient", "FortiMail", "FortiWeb", "FortiCache", "FortiAnalyzer", "FortiSandbox", "FortiDDoS", "FortiAuthenticator", "FortiProxy", "FortiNAC", "FortiDeceptor", "FortiADC", "FortiFirewall", "FortiIsolator", "FortiEDR", "FortiPAM", "FortiCASB", "FortiToken"]: ...
    @property
    def field_list(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def log_type(self) -> Literal["app-ctrl", "appevent", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "Asset", "protocol", "ztna", "security", "ANY-TYPE"]: ...

class LogFilterItem:
    """Nested item type for log-filter array."""

    @property
    def field(self) -> Literal["type", "logid", "level", "devid", "vd", "srcip", "srcintf", "dstip", "dstintf", "dstport", "user", "group", "free-text"]: ...
    @property
    def id(self) -> int: ...
    @property
    def oper(self) -> Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"]: ...
    @property
    def value(self) -> str: ...

class LogMaskingCustomItem:
    """Nested item type for log-masking-custom array."""

    @property
    def field_name(self) -> str: ...
    @property
    def field_type(self) -> Literal["string", "ip", "mac", "email", "unknown"]: ...
    @property
    def id(self) -> int: ...


class CliGlobalSystemLogForwardGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogForwardGet endpoint with autocomplete support."""

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
    def agg_archive_types(self) -> list[Any] | None:
        """Field: agg-archive-types"""
        ...

    @property
    def agg_data_end_time(self) -> list[Any] | None:
        """Field: agg-data-end-time"""
        ...

    @property
    def agg_data_start_time(self) -> list[Any] | None:
        """Field: agg-data-start-time"""
        ...

    @property
    def agg_logtypes(self) -> list[Any] | None:
        """Field: agg-logtypes"""
        ...

    @property
    def agg_password(self) -> list[Any] | None:
        """Field: agg-password"""
        ...

    @property
    def agg_schedule(self) -> Literal["daily", "on-demand"] | None:
        """Field: agg-schedule"""
        ...

    @property
    def agg_time(self) -> int | None:
        """Field: agg-time"""
        ...

    @property
    def agg_user(self) -> str | None:
        """Field: agg-user"""
        ...

    @property
    def device_filter(self) -> list[DeviceFilterItem]:
        """Field: device-filter"""
        ...

    @property
    def fwd_archive_types(self) -> list[Any] | None:
        """Field: fwd-archive-types"""
        ...

    @property
    def fwd_archives(self) -> Literal["disable", "enable"] | None:
        """Field: fwd-archives"""
        ...

    @property
    def fwd_compression(self) -> Literal["disable", "enable"] | None:
        """Field: fwd-compression"""
        ...

    @property
    def fwd_facility(self) -> Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "clock", "authpriv", "ftp", "ntp", "audit", "alert", "cron", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None:
        """Field: fwd-facility"""
        ...

    @property
    def fwd_ha_bind_vip(self) -> Literal["disable", "enable"] | None:
        """Field: fwd-ha-bind-vip"""
        ...

    @property
    def fwd_log_source_ip(self) -> Literal["local_ip", "original_ip"] | None:
        """Field: fwd-log-source-ip"""
        ...

    @property
    def fwd_max_delay(self) -> Literal["realtime", "1min", "5min"] | None:
        """Field: fwd-max-delay"""
        ...

    @property
    def fwd_output_plugin_id(self) -> str | None:
        """Field: fwd-output-plugin-id"""
        ...

    @property
    def fwd_reliable(self) -> Literal["disable", "enable"] | None:
        """Field: fwd-reliable"""
        ...

    @property
    def fwd_secure(self) -> Literal["disable", "enable"] | None:
        """Field: fwd-secure"""
        ...

    @property
    def fwd_server_type(self) -> Literal["syslog", "fortianalyzer", "cef", "syslog-pack", "fwd-via-output-plugin", "elite-service"] | None:
        """Field: fwd-server-type"""
        ...

    @property
    def fwd_syslog_decode_b64(self) -> Literal["disable", "enable"] | None:
        """Field: fwd-syslog-decode-b64"""
        ...

    @property
    def fwd_syslog_enrich_cve(self) -> Literal["disable", "enable"] | None:
        """Field: fwd-syslog-enrich-cve"""
        ...

    @property
    def fwd_syslog_format(self) -> Literal["fgt", "rfc-5424"] | None:
        """Field: fwd-syslog-format"""
        ...

    @property
    def fwd_syslog_transparent(self) -> Literal["disable", "enable", "faz-enrich"] | None:
        """Field: fwd-syslog-transparent"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def log_field_exclusion(self) -> list[LogFieldExclusionItem]:
        """Field: log-field-exclusion"""
        ...

    @property
    def log_field_exclusion_status(self) -> Literal["disable", "enable"] | None:
        """Field: log-field-exclusion-status"""
        ...

    @property
    def log_filter(self) -> list[LogFilterItem]:
        """Field: log-filter"""
        ...

    @property
    def log_filter_logic(self) -> Literal["and", "or"] | None:
        """Field: log-filter-logic"""
        ...

    @property
    def log_filter_status(self) -> Literal["disable", "enable"] | None:
        """Field: log-filter-status"""
        ...

    @property
    def log_masking_custom(self) -> list[LogMaskingCustomItem]:
        """Field: log-masking-custom"""
        ...

    @property
    def log_masking_custom_priority(self) -> Literal["disable", "enable"] | None:
        """Field: log-masking-custom-priority"""
        ...

    @property
    def log_masking_fields(self) -> list[Any] | None:
        """Field: log-masking-fields"""
        ...

    @property
    def log_masking_key(self) -> list[Any] | None:
        """Field: log-masking-key"""
        ...

    @property
    def log_masking_status(self) -> Literal["disable", "enable"] | None:
        """Field: log-masking-status"""
        ...

    @property
    def mode(self) -> Literal["forwarding", "aggregation", "disable"] | None:
        """Field: mode"""
        ...

    @property
    def pcapurl_domain_ip(self) -> str | None:
        """Field: pcapurl-domain-ip"""
        ...

    @property
    def pcapurl_enrich(self) -> Literal["disable", "enable"] | None:
        """Field: pcapurl-enrich"""
        ...

    @property
    def peer_cert_cn(self) -> str | None:
        """Field: peer-cert-cn"""
        ...

    @property
    def proxy_service(self) -> Literal["disable", "enable"] | None:
        """Field: proxy-service"""
        ...

    @property
    def proxy_service_priority(self) -> int | None:
        """Field: proxy-service-priority"""
        ...

    @property
    def server_addr(self) -> str | None:
        """Field: server-addr"""
        ...

    @property
    def server_device(self) -> str | None:
        """Field: server-device"""
        ...

    @property
    def server_name(self) -> str | None:
        """Field: server-name"""
        ...

    @property
    def server_port(self) -> int | None:
        """Field: server-port"""
        ...

    @property
    def signature(self) -> int | None:
        """Field: signature"""
        ...

    @property
    def sync_metadata(self) -> list[Any] | None:
        """Field: sync-metadata"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogForwardGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogForward:
    """FortiAnalyzer endpoint: cli.global.system.log-forward"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        log_forward: int | str | None = None,
        fields: list[Literal["agg-archive-types", "agg-data-end-time", "agg-data-start-time", "agg-logtypes", "agg-password", "agg-schedule", "agg-time", "agg-user", "fwd-archive-types", "fwd-archives", "fwd-compression", "fwd-facility", "fwd-ha-bind-vip", "fwd-log-source-ip", "fwd-max-delay", "fwd-output-plugin-id", "fwd-reliable", "fwd-secure", "fwd-server-type", "fwd-syslog-decode-b64", "fwd-syslog-enrich-cve", "fwd-syslog-format", "fwd-syslog-transparent", "id", "log-field-exclusion-status", "log-filter-logic", "log-filter-status", "log-masking-custom-priority", "log-masking-fields", "log-masking-key", "log-masking-status", "mode", "pcapurl-domain-ip", "pcapurl-enrich", "peer-cert-cn", "proxy-service", "proxy-service-priority", "server-addr", "server-device", "server-name", "server-port", "signature", "sync-metadata"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLogForwardGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        log_forward: int | str | None = None,
        agg_archive_types: list[Any] | None = None,
        agg_data_end_time: list[Any] | None = None,
        agg_data_start_time: list[Any] | None = None,
        agg_logtypes: list[Any] | None = None,
        agg_password: list[Any] | None = None,
        agg_schedule: Literal["daily", "on-demand"] | None = None,
        agg_time: int | None = None,
        agg_user: str | None = None,
        device_filter: list[dict[str, Any]] | None = None,
        fwd_archive_types: list[Any] | None = None,
        fwd_archives: Literal["disable", "enable"] | None = None,
        fwd_compression: Literal["disable", "enable"] | None = None,
        fwd_facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "clock", "authpriv", "ftp", "ntp", "audit", "alert", "cron", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = None,
        fwd_ha_bind_vip: Literal["disable", "enable"] | None = None,
        fwd_log_source_ip: Literal["local_ip", "original_ip"] | None = None,
        fwd_max_delay: Literal["realtime", "1min", "5min"] | None = None,
        fwd_output_plugin_id: str | None = None,
        fwd_reliable: Literal["disable", "enable"] | None = None,
        fwd_secure: Literal["disable", "enable"] | None = None,
        fwd_server_type: Literal["syslog", "fortianalyzer", "cef", "syslog-pack", "fwd-via-output-plugin", "elite-service"] | None = None,
        fwd_syslog_decode_b64: Literal["disable", "enable"] | None = None,
        fwd_syslog_enrich_cve: Literal["disable", "enable"] | None = None,
        fwd_syslog_format: Literal["fgt", "rfc-5424"] | None = None,
        fwd_syslog_transparent: Literal["disable", "enable", "faz-enrich"] | None = None,
        id: int | None = None,
        log_field_exclusion: list[dict[str, Any]] | None = None,
        log_field_exclusion_status: Literal["disable", "enable"] | None = None,
        log_filter: list[dict[str, Any]] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        log_masking_custom: list[dict[str, Any]] | None = None,
        log_masking_custom_priority: Literal["disable", "enable"] | None = None,
        log_masking_fields: list[Any] | None = None,
        log_masking_key: list[Any] | None = None,
        log_masking_status: Literal["disable", "enable"] | None = None,
        mode: Literal["forwarding", "aggregation", "disable"] | None = None,
        pcapurl_domain_ip: str | None = None,
        pcapurl_enrich: Literal["disable", "enable"] | None = None,
        peer_cert_cn: str | None = None,
        proxy_service: Literal["disable", "enable"] | None = None,
        proxy_service_priority: int | None = None,
        server_addr: str | None = None,
        server_device: str | None = None,
        server_name: str | None = None,
        server_port: int | None = None,
        signature: int | None = None,
        sync_metadata: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        log_forward: int | str | None = None,
        agg_archive_types: list[Any] | None = None,
        agg_data_end_time: list[Any] | None = None,
        agg_data_start_time: list[Any] | None = None,
        agg_logtypes: list[Any] | None = None,
        agg_password: list[Any] | None = None,
        agg_schedule: Literal["daily", "on-demand"] | None = None,
        agg_time: int | None = None,
        agg_user: str | None = None,
        device_filter: list[dict[str, Any]] | None = None,
        fwd_archive_types: list[Any] | None = None,
        fwd_archives: Literal["disable", "enable"] | None = None,
        fwd_compression: Literal["disable", "enable"] | None = None,
        fwd_facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "clock", "authpriv", "ftp", "ntp", "audit", "alert", "cron", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = None,
        fwd_ha_bind_vip: Literal["disable", "enable"] | None = None,
        fwd_log_source_ip: Literal["local_ip", "original_ip"] | None = None,
        fwd_max_delay: Literal["realtime", "1min", "5min"] | None = None,
        fwd_output_plugin_id: str | None = None,
        fwd_reliable: Literal["disable", "enable"] | None = None,
        fwd_secure: Literal["disable", "enable"] | None = None,
        fwd_server_type: Literal["syslog", "fortianalyzer", "cef", "syslog-pack", "fwd-via-output-plugin", "elite-service"] | None = None,
        fwd_syslog_decode_b64: Literal["disable", "enable"] | None = None,
        fwd_syslog_enrich_cve: Literal["disable", "enable"] | None = None,
        fwd_syslog_format: Literal["fgt", "rfc-5424"] | None = None,
        fwd_syslog_transparent: Literal["disable", "enable", "faz-enrich"] | None = None,
        id: int | None = None,
        log_field_exclusion: list[dict[str, Any]] | None = None,
        log_field_exclusion_status: Literal["disable", "enable"] | None = None,
        log_filter: list[dict[str, Any]] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        log_masking_custom: list[dict[str, Any]] | None = None,
        log_masking_custom_priority: Literal["disable", "enable"] | None = None,
        log_masking_fields: list[Any] | None = None,
        log_masking_key: list[Any] | None = None,
        log_masking_status: Literal["disable", "enable"] | None = None,
        mode: Literal["forwarding", "aggregation", "disable"] | None = None,
        pcapurl_domain_ip: str | None = None,
        pcapurl_enrich: Literal["disable", "enable"] | None = None,
        peer_cert_cn: str | None = None,
        proxy_service: Literal["disable", "enable"] | None = None,
        proxy_service_priority: int | None = None,
        server_addr: str | None = None,
        server_device: str | None = None,
        server_name: str | None = None,
        server_port: int | None = None,
        signature: int | None = None,
        sync_metadata: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        log_forward: int | str | None = None,
        agg_archive_types: list[Any] | None = None,
        agg_data_end_time: list[Any] | None = None,
        agg_data_start_time: list[Any] | None = None,
        agg_logtypes: list[Any] | None = None,
        agg_password: list[Any] | None = None,
        agg_schedule: Literal["daily", "on-demand"] | None = None,
        agg_time: int | None = None,
        agg_user: str | None = None,
        device_filter: list[dict[str, Any]] | None = None,
        fwd_archive_types: list[Any] | None = None,
        fwd_archives: Literal["disable", "enable"] | None = None,
        fwd_compression: Literal["disable", "enable"] | None = None,
        fwd_facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "clock", "authpriv", "ftp", "ntp", "audit", "alert", "cron", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = None,
        fwd_ha_bind_vip: Literal["disable", "enable"] | None = None,
        fwd_log_source_ip: Literal["local_ip", "original_ip"] | None = None,
        fwd_max_delay: Literal["realtime", "1min", "5min"] | None = None,
        fwd_output_plugin_id: str | None = None,
        fwd_reliable: Literal["disable", "enable"] | None = None,
        fwd_secure: Literal["disable", "enable"] | None = None,
        fwd_server_type: Literal["syslog", "fortianalyzer", "cef", "syslog-pack", "fwd-via-output-plugin", "elite-service"] | None = None,
        fwd_syslog_decode_b64: Literal["disable", "enable"] | None = None,
        fwd_syslog_enrich_cve: Literal["disable", "enable"] | None = None,
        fwd_syslog_format: Literal["fgt", "rfc-5424"] | None = None,
        fwd_syslog_transparent: Literal["disable", "enable", "faz-enrich"] | None = None,
        id: int | None = None,
        log_field_exclusion: list[dict[str, Any]] | None = None,
        log_field_exclusion_status: Literal["disable", "enable"] | None = None,
        log_filter: list[dict[str, Any]] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        log_masking_custom: list[dict[str, Any]] | None = None,
        log_masking_custom_priority: Literal["disable", "enable"] | None = None,
        log_masking_fields: list[Any] | None = None,
        log_masking_key: list[Any] | None = None,
        log_masking_status: Literal["disable", "enable"] | None = None,
        mode: Literal["forwarding", "aggregation", "disable"] | None = None,
        pcapurl_domain_ip: str | None = None,
        pcapurl_enrich: Literal["disable", "enable"] | None = None,
        peer_cert_cn: str | None = None,
        proxy_service: Literal["disable", "enable"] | None = None,
        proxy_service_priority: int | None = None,
        server_addr: str | None = None,
        server_device: str | None = None,
        server_name: str | None = None,
        server_port: int | None = None,
        signature: int | None = None,
        sync_metadata: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        log_forward: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLogForward", "CliGlobalSystemLogForwardGetResponse"]
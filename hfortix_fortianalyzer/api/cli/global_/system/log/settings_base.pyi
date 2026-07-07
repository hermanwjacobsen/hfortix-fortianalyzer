"""Type stubs for cli.global.system.log.settings"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogSettingsGetItem:
    """Item yielded when iterating over CliGlobalSystemLogSettingsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def FAC_custom_field1(self) -> str: ...
    @property
    def FCH_custom_field1(self) -> str: ...
    @property
    def FCT_custom_field1(self) -> str: ...
    @property
    def FDD_custom_field1(self) -> str: ...
    @property
    def FFW_custom_field1(self) -> str: ...
    @property
    def FGT_custom_field1(self) -> str: ...
    @property
    def FML_custom_field1(self) -> str: ...
    @property
    def FPX_custom_field1(self) -> str: ...
    @property
    def FSA_custom_field1(self) -> str: ...
    @property
    def FWB_custom_field1(self) -> str: ...
    @property
    def browse_max_logfiles(self) -> int: ...
    @property
    def client_cert_auth(self) -> dict[str, Any]: ...
    @property
    def device_auto_detect(self) -> Literal["disable", "enable"]: ...
    @property
    def dns_resolve_dstip(self) -> Literal["disable", "enable"]: ...
    @property
    def download_max_logs(self) -> int: ...
    @property
    def ha_auto_migrate(self) -> Literal["disable", "enable"]: ...
    @property
    def import_max_logfiles(self) -> int: ...
    @property
    def keep_dev_logs(self) -> Literal["disable", "enable"]: ...
    @property
    def legacy_auth_mode(self) -> Literal["disable", "enable"]: ...
    @property
    def log_file_archive_name(self) -> Literal["basic", "extended"]: ...
    @property
    def log_interval_dev_no_logging(self) -> int: ...
    @property
    def log_process_fast_mode(self) -> Literal["disable", "enable"]: ...
    @property
    def log_upload_interval_dev_no_logging(self) -> int: ...
    @property
    def rolling_analyzer(self) -> dict[str, Any]: ...
    @property
    def rolling_local(self) -> dict[str, Any]: ...
    @property
    def rolling_regular(self) -> dict[str, Any]: ...
    @property
    def sync_search_timeout(self) -> int: ...
    @property
    def syslog_over_tls_port(self) -> Literal["514", "6514"]: ...
    @property
    def unencrypted_logging_tcp(self) -> Literal["disable", "enable"]: ...
    @property
    def unencrypted_logging_udp(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogSettingsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogSettingsGet endpoint with autocomplete support."""

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
    def FAC_custom_field1(self) -> str | None:
        """Field: FAC-custom-field1"""
        ...

    @property
    def FCH_custom_field1(self) -> str | None:
        """Field: FCH-custom-field1"""
        ...

    @property
    def FCT_custom_field1(self) -> str | None:
        """Field: FCT-custom-field1"""
        ...

    @property
    def FDD_custom_field1(self) -> str | None:
        """Field: FDD-custom-field1"""
        ...

    @property
    def FFW_custom_field1(self) -> str | None:
        """Field: FFW-custom-field1"""
        ...

    @property
    def FGT_custom_field1(self) -> str | None:
        """Field: FGT-custom-field1"""
        ...

    @property
    def FML_custom_field1(self) -> str | None:
        """Field: FML-custom-field1"""
        ...

    @property
    def FPX_custom_field1(self) -> str | None:
        """Field: FPX-custom-field1"""
        ...

    @property
    def FSA_custom_field1(self) -> str | None:
        """Field: FSA-custom-field1"""
        ...

    @property
    def FWB_custom_field1(self) -> str | None:
        """Field: FWB-custom-field1"""
        ...

    @property
    def browse_max_logfiles(self) -> int | None:
        """Field: browse-max-logfiles"""
        ...

    @property
    def client_cert_auth(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.log.settings.client-cert-auth)."""
        ...

    @property
    def device_auto_detect(self) -> Literal["disable", "enable"] | None:
        """Field: device-auto-detect"""
        ...

    @property
    def dns_resolve_dstip(self) -> Literal["disable", "enable"] | None:
        """Field: dns-resolve-dstip"""
        ...

    @property
    def download_max_logs(self) -> int | None:
        """Field: download-max-logs"""
        ...

    @property
    def ha_auto_migrate(self) -> Literal["disable", "enable"] | None:
        """Field: ha-auto-migrate"""
        ...

    @property
    def import_max_logfiles(self) -> int | None:
        """Field: import-max-logfiles"""
        ...

    @property
    def keep_dev_logs(self) -> Literal["disable", "enable"] | None:
        """Field: keep-dev-logs"""
        ...

    @property
    def legacy_auth_mode(self) -> Literal["disable", "enable"] | None:
        """Field: legacy-auth-mode"""
        ...

    @property
    def log_file_archive_name(self) -> Literal["basic", "extended"] | None:
        """Field: log-file-archive-name"""
        ...

    @property
    def log_interval_dev_no_logging(self) -> int | None:
        """Field: log-interval-dev-no-logging"""
        ...

    @property
    def log_process_fast_mode(self) -> Literal["disable", "enable"] | None:
        """Field: log-process-fast-mode"""
        ...

    @property
    def log_upload_interval_dev_no_logging(self) -> int | None:
        """Field: log-upload-interval-dev-no-logging"""
        ...

    @property
    def rolling_analyzer(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.log.settings.rolling-analyzer)."""
        ...

    @property
    def rolling_local(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.log.settings.rolling-local)."""
        ...

    @property
    def rolling_regular(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.log.settings.rolling-regular)."""
        ...

    @property
    def sync_search_timeout(self) -> int | None:
        """Field: sync-search-timeout"""
        ...

    @property
    def syslog_over_tls_port(self) -> Literal["514", "6514"] | None:
        """Field: syslog-over-tls-port"""
        ...

    @property
    def unencrypted_logging_tcp(self) -> Literal["disable", "enable"] | None:
        """Field: unencrypted-logging-tcp"""
        ...

    @property
    def unencrypted_logging_udp(self) -> Literal["disable", "enable"] | None:
        """Field: unencrypted-logging-udp"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogSettingsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogSettings:
    """FortiAnalyzer endpoint: cli.global.system.log.settings"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogSettingsGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        FAC_custom_field1: str | None = None,
        FCH_custom_field1: str | None = None,
        FCT_custom_field1: str | None = None,
        FDD_custom_field1: str | None = None,
        FFW_custom_field1: str | None = None,
        FGT_custom_field1: str | None = None,
        FML_custom_field1: str | None = None,
        FPX_custom_field1: str | None = None,
        FSA_custom_field1: str | None = None,
        FWB_custom_field1: str | None = None,
        browse_max_logfiles: int | None = None,
        client_cert_auth: dict[str, Any] | None = None,
        device_auto_detect: Literal["disable", "enable"] | None = None,
        dns_resolve_dstip: Literal["disable", "enable"] | None = None,
        download_max_logs: int | None = None,
        ha_auto_migrate: Literal["disable", "enable"] | None = None,
        import_max_logfiles: int | None = None,
        keep_dev_logs: Literal["disable", "enable"] | None = None,
        legacy_auth_mode: Literal["disable", "enable"] | None = None,
        log_file_archive_name: Literal["basic", "extended"] | None = None,
        log_interval_dev_no_logging: int | None = None,
        log_process_fast_mode: Literal["disable", "enable"] | None = None,
        log_upload_interval_dev_no_logging: int | None = None,
        rolling_analyzer: dict[str, Any] | None = None,
        rolling_local: dict[str, Any] | None = None,
        rolling_regular: dict[str, Any] | None = None,
        sync_search_timeout: int | None = None,
        syslog_over_tls_port: Literal["514", "6514"] | None = None,
        unencrypted_logging_tcp: Literal["disable", "enable"] | None = None,
        unencrypted_logging_udp: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        FAC_custom_field1: str | None = None,
        FCH_custom_field1: str | None = None,
        FCT_custom_field1: str | None = None,
        FDD_custom_field1: str | None = None,
        FFW_custom_field1: str | None = None,
        FGT_custom_field1: str | None = None,
        FML_custom_field1: str | None = None,
        FPX_custom_field1: str | None = None,
        FSA_custom_field1: str | None = None,
        FWB_custom_field1: str | None = None,
        browse_max_logfiles: int | None = None,
        client_cert_auth: dict[str, Any] | None = None,
        device_auto_detect: Literal["disable", "enable"] | None = None,
        dns_resolve_dstip: Literal["disable", "enable"] | None = None,
        download_max_logs: int | None = None,
        ha_auto_migrate: Literal["disable", "enable"] | None = None,
        import_max_logfiles: int | None = None,
        keep_dev_logs: Literal["disable", "enable"] | None = None,
        legacy_auth_mode: Literal["disable", "enable"] | None = None,
        log_file_archive_name: Literal["basic", "extended"] | None = None,
        log_interval_dev_no_logging: int | None = None,
        log_process_fast_mode: Literal["disable", "enable"] | None = None,
        log_upload_interval_dev_no_logging: int | None = None,
        rolling_analyzer: dict[str, Any] | None = None,
        rolling_local: dict[str, Any] | None = None,
        rolling_regular: dict[str, Any] | None = None,
        sync_search_timeout: int | None = None,
        syslog_over_tls_port: Literal["514", "6514"] | None = None,
        unencrypted_logging_tcp: Literal["disable", "enable"] | None = None,
        unencrypted_logging_udp: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogSettings", "CliGlobalSystemLogSettingsGetResponse"]
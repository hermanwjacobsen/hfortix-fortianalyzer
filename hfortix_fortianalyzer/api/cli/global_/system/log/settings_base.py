"""
FortiAnalyzer API endpoint: cli.global.system.log.settings

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogSettings:
    """
    FortiAnalyzer endpoint: cli.global.system.log.settings
    
    
    Available methods: get, set, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/settings"
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        browse_max_logfiles: int | None = None,
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
        sync_search_timeout: int | None = None,
        syslog_over_tls_port: Literal["514", "6514"] | None = None,
        unencrypted_logging_tcp: Literal["disable", "enable"] | None = None,
        unencrypted_logging_udp: Literal["disable", "enable"] | None = None,
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
        client_cert_auth: dict[str, Any] | None = None,
        rolling_analyzer: dict[str, Any] | None = None,
        rolling_local: dict[str, Any] | None = None,
        rolling_regular: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            FAC_custom_field1: FAC-custom-field1 parameter
            FCH_custom_field1: FCH-custom-field1 parameter
            FCT_custom_field1: FCT-custom-field1 parameter
            FDD_custom_field1: FDD-custom-field1 parameter
            FFW_custom_field1: FFW-custom-field1 parameter
            FGT_custom_field1: FGT-custom-field1 parameter
            FML_custom_field1: FML-custom-field1 parameter
            FPX_custom_field1: FPX-custom-field1 parameter
            FSA_custom_field1: FSA-custom-field1 parameter
            FWB_custom_field1: FWB-custom-field1 parameter
            ... (20 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/settings"
        
        # Build data payload
        data = {}
        if FAC_custom_field1 is not None:
            data["FAC-custom-field1"] = FAC_custom_field1
        if FCH_custom_field1 is not None:
            data["FCH-custom-field1"] = FCH_custom_field1
        if FCT_custom_field1 is not None:
            data["FCT-custom-field1"] = FCT_custom_field1
        if FDD_custom_field1 is not None:
            data["FDD-custom-field1"] = FDD_custom_field1
        if FFW_custom_field1 is not None:
            data["FFW-custom-field1"] = FFW_custom_field1
        if FGT_custom_field1 is not None:
            data["FGT-custom-field1"] = FGT_custom_field1
        if FML_custom_field1 is not None:
            data["FML-custom-field1"] = FML_custom_field1
        if FPX_custom_field1 is not None:
            data["FPX-custom-field1"] = FPX_custom_field1
        if FSA_custom_field1 is not None:
            data["FSA-custom-field1"] = FSA_custom_field1
        if FWB_custom_field1 is not None:
            data["FWB-custom-field1"] = FWB_custom_field1
        if browse_max_logfiles is not None:
            data["browse-max-logfiles"] = browse_max_logfiles
        if client_cert_auth is not None:
            data["client-cert-auth"] = client_cert_auth
        if device_auto_detect is not None:
            data["device-auto-detect"] = device_auto_detect
        if dns_resolve_dstip is not None:
            data["dns-resolve-dstip"] = dns_resolve_dstip
        if download_max_logs is not None:
            data["download-max-logs"] = download_max_logs
        if ha_auto_migrate is not None:
            data["ha-auto-migrate"] = ha_auto_migrate
        if import_max_logfiles is not None:
            data["import-max-logfiles"] = import_max_logfiles
        if keep_dev_logs is not None:
            data["keep-dev-logs"] = keep_dev_logs
        if legacy_auth_mode is not None:
            data["legacy-auth-mode"] = legacy_auth_mode
        if log_file_archive_name is not None:
            data["log-file-archive-name"] = log_file_archive_name
        if log_interval_dev_no_logging is not None:
            data["log-interval-dev-no-logging"] = log_interval_dev_no_logging
        if log_process_fast_mode is not None:
            data["log-process-fast-mode"] = log_process_fast_mode
        if log_upload_interval_dev_no_logging is not None:
            data["log-upload-interval-dev-no-logging"] = log_upload_interval_dev_no_logging
        if rolling_analyzer is not None:
            data["rolling-analyzer"] = rolling_analyzer
        if rolling_local is not None:
            data["rolling-local"] = rolling_local
        if rolling_regular is not None:
            data["rolling-regular"] = rolling_regular
        if sync_search_timeout is not None:
            data["sync-search-timeout"] = sync_search_timeout
        if syslog_over_tls_port is not None:
            data["syslog-over-tls-port"] = syslog_over_tls_port
        if unencrypted_logging_tcp is not None:
            data["unencrypted-logging-tcp"] = unencrypted_logging_tcp
        if unencrypted_logging_udp is not None:
            data["unencrypted-logging-udp"] = unencrypted_logging_udp
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def update(
        self,
        browse_max_logfiles: int | None = None,
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
        sync_search_timeout: int | None = None,
        syslog_over_tls_port: Literal["514", "6514"] | None = None,
        unencrypted_logging_tcp: Literal["disable", "enable"] | None = None,
        unencrypted_logging_udp: Literal["disable", "enable"] | None = None,
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
        client_cert_auth: dict[str, Any] | None = None,
        rolling_analyzer: dict[str, Any] | None = None,
        rolling_local: dict[str, Any] | None = None,
        rolling_regular: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            FAC_custom_field1: FAC-custom-field1 parameter
            FCH_custom_field1: FCH-custom-field1 parameter
            FCT_custom_field1: FCT-custom-field1 parameter
            FDD_custom_field1: FDD-custom-field1 parameter
            FFW_custom_field1: FFW-custom-field1 parameter
            FGT_custom_field1: FGT-custom-field1 parameter
            FML_custom_field1: FML-custom-field1 parameter
            FPX_custom_field1: FPX-custom-field1 parameter
            FSA_custom_field1: FSA-custom-field1 parameter
            FWB_custom_field1: FWB-custom-field1 parameter
            ... (20 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/settings"
        
        # Build data payload
        data = {}
        if FAC_custom_field1 is not None:
            data["FAC-custom-field1"] = FAC_custom_field1
        if FCH_custom_field1 is not None:
            data["FCH-custom-field1"] = FCH_custom_field1
        if FCT_custom_field1 is not None:
            data["FCT-custom-field1"] = FCT_custom_field1
        if FDD_custom_field1 is not None:
            data["FDD-custom-field1"] = FDD_custom_field1
        if FFW_custom_field1 is not None:
            data["FFW-custom-field1"] = FFW_custom_field1
        if FGT_custom_field1 is not None:
            data["FGT-custom-field1"] = FGT_custom_field1
        if FML_custom_field1 is not None:
            data["FML-custom-field1"] = FML_custom_field1
        if FPX_custom_field1 is not None:
            data["FPX-custom-field1"] = FPX_custom_field1
        if FSA_custom_field1 is not None:
            data["FSA-custom-field1"] = FSA_custom_field1
        if FWB_custom_field1 is not None:
            data["FWB-custom-field1"] = FWB_custom_field1
        if browse_max_logfiles is not None:
            data["browse-max-logfiles"] = browse_max_logfiles
        if client_cert_auth is not None:
            data["client-cert-auth"] = client_cert_auth
        if device_auto_detect is not None:
            data["device-auto-detect"] = device_auto_detect
        if dns_resolve_dstip is not None:
            data["dns-resolve-dstip"] = dns_resolve_dstip
        if download_max_logs is not None:
            data["download-max-logs"] = download_max_logs
        if ha_auto_migrate is not None:
            data["ha-auto-migrate"] = ha_auto_migrate
        if import_max_logfiles is not None:
            data["import-max-logfiles"] = import_max_logfiles
        if keep_dev_logs is not None:
            data["keep-dev-logs"] = keep_dev_logs
        if legacy_auth_mode is not None:
            data["legacy-auth-mode"] = legacy_auth_mode
        if log_file_archive_name is not None:
            data["log-file-archive-name"] = log_file_archive_name
        if log_interval_dev_no_logging is not None:
            data["log-interval-dev-no-logging"] = log_interval_dev_no_logging
        if log_process_fast_mode is not None:
            data["log-process-fast-mode"] = log_process_fast_mode
        if log_upload_interval_dev_no_logging is not None:
            data["log-upload-interval-dev-no-logging"] = log_upload_interval_dev_no_logging
        if rolling_analyzer is not None:
            data["rolling-analyzer"] = rolling_analyzer
        if rolling_local is not None:
            data["rolling-local"] = rolling_local
        if rolling_regular is not None:
            data["rolling-regular"] = rolling_regular
        if sync_search_timeout is not None:
            data["sync-search-timeout"] = sync_search_timeout
        if syslog_over_tls_port is not None:
            data["syslog-over-tls-port"] = syslog_over_tls_port
        if unencrypted_logging_tcp is not None:
            data["unencrypted-logging-tcp"] = unencrypted_logging_tcp
        if unencrypted_logging_udp is not None:
            data["unencrypted-logging-udp"] = unencrypted_logging_udp
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

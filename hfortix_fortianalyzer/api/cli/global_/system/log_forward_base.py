"""
FortiAnalyzer API endpoint: cli.global.system.log-forward

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogForward:
    """
    FortiAnalyzer endpoint: cli.global.system.log-forward
    
    
    Available methods: get, add, set, update, delete
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(
        self,
        log_forward: int | str | None = None,
        fields: list[Literal["agg-archive-types", "agg-data-end-time", "agg-data-start-time", "agg-logtypes", "agg-password", "agg-schedule", "agg-time", "agg-user", "fwd-archive-types", "fwd-archives", "fwd-compression", "fwd-facility", "fwd-ha-bind-vip", "fwd-log-source-ip", "fwd-max-delay", "fwd-output-plugin-id", "fwd-reliable", "fwd-secure", "fwd-server-type", "fwd-syslog-decode-b64", "fwd-syslog-enrich-cve", "fwd-syslog-format", "fwd-syslog-transparent", "id", "log-field-exclusion-status", "log-filter-logic", "log-filter-status", "log-masking-custom-priority", "log-masking-fields", "log-masking-key", "log-masking-status", "mode", "pcapurl-domain-ip", "pcapurl-enrich", "peer-cert-cn", "proxy-service", "proxy-service-priority", "server-addr", "server-device", "server-name", "server-port", "signature", "sync-metadata"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            log_forward: log-forward parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if log_forward is not None:
            url = "/cli/global/system/log-forward/{log-forward}"
            url = url.replace("{log-forward}", str(log_forward))
        else:
            url = "/cli/global/system/log-forward"
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        if fields is not None and fields and not isinstance(fields[0], list):
            fields = [fields]
        
        request_params = {}
        if fields is not None:
            request_params["fields"] = fields
        if filter is not None:
            request_params["filter"] = filter
        if loadsub is not None:
            request_params["loadsub"] = loadsub
        if option is not None:
            request_params["option"] = option
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            **request_params
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def add(
        self,
        log_forward: int | str | None = None,
        agg_schedule: Literal["daily", "on-demand"] | None = None,
        agg_time: int | None = None,
        fwd_archives: Literal["disable", "enable"] | None = None,
        fwd_compression: Literal["disable", "enable"] | None = None,
        fwd_facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "clock", "authpriv", "ftp", "ntp", "audit", "alert", "cron", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = None,
        fwd_ha_bind_vip: Literal["disable", "enable"] | None = None,
        fwd_log_source_ip: Literal["local_ip", "original_ip"] | None = None,
        fwd_max_delay: Literal["realtime", "1min", "5min"] | None = None,
        fwd_reliable: Literal["disable", "enable"] | None = None,
        fwd_secure: Literal["disable", "enable"] | None = None,
        fwd_server_type: Literal["syslog", "fortianalyzer", "cef", "syslog-pack", "fwd-via-output-plugin", "elite-service"] | None = None,
        fwd_syslog_decode_b64: Literal["disable", "enable"] | None = None,
        fwd_syslog_enrich_cve: Literal["disable", "enable"] | None = None,
        fwd_syslog_format: Literal["fgt", "rfc-5424"] | None = None,
        fwd_syslog_transparent: Literal["disable", "enable", "faz-enrich"] | None = None,
        id: int | None = None,
        log_field_exclusion_status: Literal["disable", "enable"] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        log_masking_custom_priority: Literal["disable", "enable"] | None = None,
        log_masking_status: Literal["disable", "enable"] | None = None,
        mode: Literal["forwarding", "aggregation", "disable"] | None = None,
        pcapurl_enrich: Literal["disable", "enable"] | None = None,
        proxy_service: Literal["disable", "enable"] | None = None,
        proxy_service_priority: int | None = None,
        server_port: int | None = None,
        signature: int | None = None,
        agg_archive_types: list[Any] | None = None,
        agg_data_end_time: list[Any] | None = None,
        agg_data_start_time: list[Any] | None = None,
        agg_logtypes: list[Any] | None = None,
        agg_password: list[Any] | None = None,
        agg_user: str | None = None,
        device_filter: list[Any] | None = None,
        fwd_archive_types: list[Any] | None = None,
        fwd_output_plugin_id: str | None = None,
        log_field_exclusion: list[Any] | None = None,
        log_filter: list[Any] | None = None,
        log_masking_custom: list[Any] | None = None,
        log_masking_fields: list[Any] | None = None,
        log_masking_key: list[Any] | None = None,
        pcapurl_domain_ip: str | None = None,
        peer_cert_cn: str | None = None,
        server_addr: str | None = None,
        server_device: str | None = None,
        server_name: str | None = None,
        sync_metadata: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            log_forward: log-forward parameter
            agg_archive_types: agg-archive-types parameter
            agg_data_end_time: agg-data-end-time parameter
            agg_data_start_time: agg-data-start-time parameter
            agg_logtypes: agg-logtypes parameter
            agg_password: agg-password parameter
            agg_schedule: agg-schedule parameter
            agg_time: agg-time parameter
            agg_user: agg-user parameter
            device_filter: device-filter parameter
            fwd_archive_types: fwd-archive-types parameter
            ... (37 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log-forward"
        
        # Build data payload
        data = {}
        if agg_archive_types is not None:
            data["agg-archive-types"] = agg_archive_types
        if agg_data_end_time is not None:
            data["agg-data-end-time"] = agg_data_end_time
        if agg_data_start_time is not None:
            data["agg-data-start-time"] = agg_data_start_time
        if agg_logtypes is not None:
            data["agg-logtypes"] = agg_logtypes
        if agg_password is not None:
            data["agg-password"] = agg_password
        if agg_schedule is not None:
            data["agg-schedule"] = agg_schedule
        if agg_time is not None:
            data["agg-time"] = agg_time
        if agg_user is not None:
            data["agg-user"] = agg_user
        if device_filter is not None:
            data["device-filter"] = device_filter
        if fwd_archive_types is not None:
            data["fwd-archive-types"] = fwd_archive_types
        if fwd_archives is not None:
            data["fwd-archives"] = fwd_archives
        if fwd_compression is not None:
            data["fwd-compression"] = fwd_compression
        if fwd_facility is not None:
            data["fwd-facility"] = fwd_facility
        if fwd_ha_bind_vip is not None:
            data["fwd-ha-bind-vip"] = fwd_ha_bind_vip
        if fwd_log_source_ip is not None:
            data["fwd-log-source-ip"] = fwd_log_source_ip
        if fwd_max_delay is not None:
            data["fwd-max-delay"] = fwd_max_delay
        if fwd_output_plugin_id is not None:
            data["fwd-output-plugin-id"] = fwd_output_plugin_id
        if fwd_reliable is not None:
            data["fwd-reliable"] = fwd_reliable
        if fwd_secure is not None:
            data["fwd-secure"] = fwd_secure
        if fwd_server_type is not None:
            data["fwd-server-type"] = fwd_server_type
        if fwd_syslog_decode_b64 is not None:
            data["fwd-syslog-decode-b64"] = fwd_syslog_decode_b64
        if fwd_syslog_enrich_cve is not None:
            data["fwd-syslog-enrich-cve"] = fwd_syslog_enrich_cve
        if fwd_syslog_format is not None:
            data["fwd-syslog-format"] = fwd_syslog_format
        if fwd_syslog_transparent is not None:
            data["fwd-syslog-transparent"] = fwd_syslog_transparent
        if id is not None:
            data["id"] = id
        if log_field_exclusion is not None:
            data["log-field-exclusion"] = log_field_exclusion
        if log_field_exclusion_status is not None:
            data["log-field-exclusion-status"] = log_field_exclusion_status
        if log_filter is not None:
            data["log-filter"] = log_filter
        if log_filter_logic is not None:
            data["log-filter-logic"] = log_filter_logic
        if log_filter_status is not None:
            data["log-filter-status"] = log_filter_status
        if log_masking_custom is not None:
            data["log-masking-custom"] = log_masking_custom
        if log_masking_custom_priority is not None:
            data["log-masking-custom-priority"] = log_masking_custom_priority
        if log_masking_fields is not None:
            data["log-masking-fields"] = log_masking_fields
        if log_masking_key is not None:
            data["log-masking-key"] = log_masking_key
        if log_masking_status is not None:
            data["log-masking-status"] = log_masking_status
        if mode is not None:
            data["mode"] = mode
        if pcapurl_domain_ip is not None:
            data["pcapurl-domain-ip"] = pcapurl_domain_ip
        if pcapurl_enrich is not None:
            data["pcapurl-enrich"] = pcapurl_enrich
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if proxy_service is not None:
            data["proxy-service"] = proxy_service
        if proxy_service_priority is not None:
            data["proxy-service-priority"] = proxy_service_priority
        if server_addr is not None:
            data["server-addr"] = server_addr
        if server_device is not None:
            data["server-device"] = server_device
        if server_name is not None:
            data["server-name"] = server_name
        if server_port is not None:
            data["server-port"] = server_port
        if signature is not None:
            data["signature"] = signature
        if sync_metadata is not None:
            data["sync-metadata"] = sync_metadata
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        log_forward: int | str | None = None,
        agg_schedule: Literal["daily", "on-demand"] | None = None,
        agg_time: int | None = None,
        fwd_archives: Literal["disable", "enable"] | None = None,
        fwd_compression: Literal["disable", "enable"] | None = None,
        fwd_facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "clock", "authpriv", "ftp", "ntp", "audit", "alert", "cron", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = None,
        fwd_ha_bind_vip: Literal["disable", "enable"] | None = None,
        fwd_log_source_ip: Literal["local_ip", "original_ip"] | None = None,
        fwd_max_delay: Literal["realtime", "1min", "5min"] | None = None,
        fwd_reliable: Literal["disable", "enable"] | None = None,
        fwd_secure: Literal["disable", "enable"] | None = None,
        fwd_server_type: Literal["syslog", "fortianalyzer", "cef", "syslog-pack", "fwd-via-output-plugin", "elite-service"] | None = None,
        fwd_syslog_decode_b64: Literal["disable", "enable"] | None = None,
        fwd_syslog_enrich_cve: Literal["disable", "enable"] | None = None,
        fwd_syslog_format: Literal["fgt", "rfc-5424"] | None = None,
        fwd_syslog_transparent: Literal["disable", "enable", "faz-enrich"] | None = None,
        id: int | None = None,
        log_field_exclusion_status: Literal["disable", "enable"] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        log_masking_custom_priority: Literal["disable", "enable"] | None = None,
        log_masking_status: Literal["disable", "enable"] | None = None,
        mode: Literal["forwarding", "aggregation", "disable"] | None = None,
        pcapurl_enrich: Literal["disable", "enable"] | None = None,
        proxy_service: Literal["disable", "enable"] | None = None,
        proxy_service_priority: int | None = None,
        server_port: int | None = None,
        signature: int | None = None,
        agg_archive_types: list[Any] | None = None,
        agg_data_end_time: list[Any] | None = None,
        agg_data_start_time: list[Any] | None = None,
        agg_logtypes: list[Any] | None = None,
        agg_password: list[Any] | None = None,
        agg_user: str | None = None,
        device_filter: list[Any] | None = None,
        fwd_archive_types: list[Any] | None = None,
        fwd_output_plugin_id: str | None = None,
        log_field_exclusion: list[Any] | None = None,
        log_filter: list[Any] | None = None,
        log_masking_custom: list[Any] | None = None,
        log_masking_fields: list[Any] | None = None,
        log_masking_key: list[Any] | None = None,
        pcapurl_domain_ip: str | None = None,
        peer_cert_cn: str | None = None,
        server_addr: str | None = None,
        server_device: str | None = None,
        server_name: str | None = None,
        sync_metadata: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            log_forward: log-forward parameter
            agg_archive_types: agg-archive-types parameter
            agg_data_end_time: agg-data-end-time parameter
            agg_data_start_time: agg-data-start-time parameter
            agg_logtypes: agg-logtypes parameter
            agg_password: agg-password parameter
            agg_schedule: agg-schedule parameter
            agg_time: agg-time parameter
            agg_user: agg-user parameter
            device_filter: device-filter parameter
            fwd_archive_types: fwd-archive-types parameter
            ... (37 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if log_forward is not None:
            url = "/cli/global/system/log-forward/{log-forward}"
            url = url.replace("{log-forward}", str(log_forward))
        else:
            url = "/cli/global/system/log-forward"
        
        # Build data payload
        data = {}
        if agg_archive_types is not None:
            data["agg-archive-types"] = agg_archive_types
        if agg_data_end_time is not None:
            data["agg-data-end-time"] = agg_data_end_time
        if agg_data_start_time is not None:
            data["agg-data-start-time"] = agg_data_start_time
        if agg_logtypes is not None:
            data["agg-logtypes"] = agg_logtypes
        if agg_password is not None:
            data["agg-password"] = agg_password
        if agg_schedule is not None:
            data["agg-schedule"] = agg_schedule
        if agg_time is not None:
            data["agg-time"] = agg_time
        if agg_user is not None:
            data["agg-user"] = agg_user
        if device_filter is not None:
            data["device-filter"] = device_filter
        if fwd_archive_types is not None:
            data["fwd-archive-types"] = fwd_archive_types
        if fwd_archives is not None:
            data["fwd-archives"] = fwd_archives
        if fwd_compression is not None:
            data["fwd-compression"] = fwd_compression
        if fwd_facility is not None:
            data["fwd-facility"] = fwd_facility
        if fwd_ha_bind_vip is not None:
            data["fwd-ha-bind-vip"] = fwd_ha_bind_vip
        if fwd_log_source_ip is not None:
            data["fwd-log-source-ip"] = fwd_log_source_ip
        if fwd_max_delay is not None:
            data["fwd-max-delay"] = fwd_max_delay
        if fwd_output_plugin_id is not None:
            data["fwd-output-plugin-id"] = fwd_output_plugin_id
        if fwd_reliable is not None:
            data["fwd-reliable"] = fwd_reliable
        if fwd_secure is not None:
            data["fwd-secure"] = fwd_secure
        if fwd_server_type is not None:
            data["fwd-server-type"] = fwd_server_type
        if fwd_syslog_decode_b64 is not None:
            data["fwd-syslog-decode-b64"] = fwd_syslog_decode_b64
        if fwd_syslog_enrich_cve is not None:
            data["fwd-syslog-enrich-cve"] = fwd_syslog_enrich_cve
        if fwd_syslog_format is not None:
            data["fwd-syslog-format"] = fwd_syslog_format
        if fwd_syslog_transparent is not None:
            data["fwd-syslog-transparent"] = fwd_syslog_transparent
        if id is not None:
            data["id"] = id
        if log_field_exclusion is not None:
            data["log-field-exclusion"] = log_field_exclusion
        if log_field_exclusion_status is not None:
            data["log-field-exclusion-status"] = log_field_exclusion_status
        if log_filter is not None:
            data["log-filter"] = log_filter
        if log_filter_logic is not None:
            data["log-filter-logic"] = log_filter_logic
        if log_filter_status is not None:
            data["log-filter-status"] = log_filter_status
        if log_masking_custom is not None:
            data["log-masking-custom"] = log_masking_custom
        if log_masking_custom_priority is not None:
            data["log-masking-custom-priority"] = log_masking_custom_priority
        if log_masking_fields is not None:
            data["log-masking-fields"] = log_masking_fields
        if log_masking_key is not None:
            data["log-masking-key"] = log_masking_key
        if log_masking_status is not None:
            data["log-masking-status"] = log_masking_status
        if mode is not None:
            data["mode"] = mode
        if pcapurl_domain_ip is not None:
            data["pcapurl-domain-ip"] = pcapurl_domain_ip
        if pcapurl_enrich is not None:
            data["pcapurl-enrich"] = pcapurl_enrich
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if proxy_service is not None:
            data["proxy-service"] = proxy_service
        if proxy_service_priority is not None:
            data["proxy-service-priority"] = proxy_service_priority
        if server_addr is not None:
            data["server-addr"] = server_addr
        if server_device is not None:
            data["server-device"] = server_device
        if server_name is not None:
            data["server-name"] = server_name
        if server_port is not None:
            data["server-port"] = server_port
        if signature is not None:
            data["signature"] = signature
        if sync_metadata is not None:
            data["sync-metadata"] = sync_metadata
        
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
        log_forward: int | str | None = None,
        agg_schedule: Literal["daily", "on-demand"] | None = None,
        agg_time: int | None = None,
        fwd_archives: Literal["disable", "enable"] | None = None,
        fwd_compression: Literal["disable", "enable"] | None = None,
        fwd_facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "clock", "authpriv", "ftp", "ntp", "audit", "alert", "cron", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"] | None = None,
        fwd_ha_bind_vip: Literal["disable", "enable"] | None = None,
        fwd_log_source_ip: Literal["local_ip", "original_ip"] | None = None,
        fwd_max_delay: Literal["realtime", "1min", "5min"] | None = None,
        fwd_reliable: Literal["disable", "enable"] | None = None,
        fwd_secure: Literal["disable", "enable"] | None = None,
        fwd_server_type: Literal["syslog", "fortianalyzer", "cef", "syslog-pack", "fwd-via-output-plugin", "elite-service"] | None = None,
        fwd_syslog_decode_b64: Literal["disable", "enable"] | None = None,
        fwd_syslog_enrich_cve: Literal["disable", "enable"] | None = None,
        fwd_syslog_format: Literal["fgt", "rfc-5424"] | None = None,
        fwd_syslog_transparent: Literal["disable", "enable", "faz-enrich"] | None = None,
        id: int | None = None,
        log_field_exclusion_status: Literal["disable", "enable"] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        log_masking_custom_priority: Literal["disable", "enable"] | None = None,
        log_masking_status: Literal["disable", "enable"] | None = None,
        mode: Literal["forwarding", "aggregation", "disable"] | None = None,
        pcapurl_enrich: Literal["disable", "enable"] | None = None,
        proxy_service: Literal["disable", "enable"] | None = None,
        proxy_service_priority: int | None = None,
        server_port: int | None = None,
        signature: int | None = None,
        agg_archive_types: list[Any] | None = None,
        agg_data_end_time: list[Any] | None = None,
        agg_data_start_time: list[Any] | None = None,
        agg_logtypes: list[Any] | None = None,
        agg_password: list[Any] | None = None,
        agg_user: str | None = None,
        device_filter: list[Any] | None = None,
        fwd_archive_types: list[Any] | None = None,
        fwd_output_plugin_id: str | None = None,
        log_field_exclusion: list[Any] | None = None,
        log_filter: list[Any] | None = None,
        log_masking_custom: list[Any] | None = None,
        log_masking_fields: list[Any] | None = None,
        log_masking_key: list[Any] | None = None,
        pcapurl_domain_ip: str | None = None,
        peer_cert_cn: str | None = None,
        server_addr: str | None = None,
        server_device: str | None = None,
        server_name: str | None = None,
        sync_metadata: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            log_forward: log-forward parameter
            agg_archive_types: agg-archive-types parameter
            agg_data_end_time: agg-data-end-time parameter
            agg_data_start_time: agg-data-start-time parameter
            agg_logtypes: agg-logtypes parameter
            agg_password: agg-password parameter
            agg_schedule: agg-schedule parameter
            agg_time: agg-time parameter
            agg_user: agg-user parameter
            device_filter: device-filter parameter
            fwd_archive_types: fwd-archive-types parameter
            ... (37 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if log_forward is not None:
            url = "/cli/global/system/log-forward/{log-forward}"
            url = url.replace("{log-forward}", str(log_forward))
        else:
            url = "/cli/global/system/log-forward"
        
        # Build data payload
        data = {}
        if agg_archive_types is not None:
            data["agg-archive-types"] = agg_archive_types
        if agg_data_end_time is not None:
            data["agg-data-end-time"] = agg_data_end_time
        if agg_data_start_time is not None:
            data["agg-data-start-time"] = agg_data_start_time
        if agg_logtypes is not None:
            data["agg-logtypes"] = agg_logtypes
        if agg_password is not None:
            data["agg-password"] = agg_password
        if agg_schedule is not None:
            data["agg-schedule"] = agg_schedule
        if agg_time is not None:
            data["agg-time"] = agg_time
        if agg_user is not None:
            data["agg-user"] = agg_user
        if device_filter is not None:
            data["device-filter"] = device_filter
        if fwd_archive_types is not None:
            data["fwd-archive-types"] = fwd_archive_types
        if fwd_archives is not None:
            data["fwd-archives"] = fwd_archives
        if fwd_compression is not None:
            data["fwd-compression"] = fwd_compression
        if fwd_facility is not None:
            data["fwd-facility"] = fwd_facility
        if fwd_ha_bind_vip is not None:
            data["fwd-ha-bind-vip"] = fwd_ha_bind_vip
        if fwd_log_source_ip is not None:
            data["fwd-log-source-ip"] = fwd_log_source_ip
        if fwd_max_delay is not None:
            data["fwd-max-delay"] = fwd_max_delay
        if fwd_output_plugin_id is not None:
            data["fwd-output-plugin-id"] = fwd_output_plugin_id
        if fwd_reliable is not None:
            data["fwd-reliable"] = fwd_reliable
        if fwd_secure is not None:
            data["fwd-secure"] = fwd_secure
        if fwd_server_type is not None:
            data["fwd-server-type"] = fwd_server_type
        if fwd_syslog_decode_b64 is not None:
            data["fwd-syslog-decode-b64"] = fwd_syslog_decode_b64
        if fwd_syslog_enrich_cve is not None:
            data["fwd-syslog-enrich-cve"] = fwd_syslog_enrich_cve
        if fwd_syslog_format is not None:
            data["fwd-syslog-format"] = fwd_syslog_format
        if fwd_syslog_transparent is not None:
            data["fwd-syslog-transparent"] = fwd_syslog_transparent
        if id is not None:
            data["id"] = id
        if log_field_exclusion is not None:
            data["log-field-exclusion"] = log_field_exclusion
        if log_field_exclusion_status is not None:
            data["log-field-exclusion-status"] = log_field_exclusion_status
        if log_filter is not None:
            data["log-filter"] = log_filter
        if log_filter_logic is not None:
            data["log-filter-logic"] = log_filter_logic
        if log_filter_status is not None:
            data["log-filter-status"] = log_filter_status
        if log_masking_custom is not None:
            data["log-masking-custom"] = log_masking_custom
        if log_masking_custom_priority is not None:
            data["log-masking-custom-priority"] = log_masking_custom_priority
        if log_masking_fields is not None:
            data["log-masking-fields"] = log_masking_fields
        if log_masking_key is not None:
            data["log-masking-key"] = log_masking_key
        if log_masking_status is not None:
            data["log-masking-status"] = log_masking_status
        if mode is not None:
            data["mode"] = mode
        if pcapurl_domain_ip is not None:
            data["pcapurl-domain-ip"] = pcapurl_domain_ip
        if pcapurl_enrich is not None:
            data["pcapurl-enrich"] = pcapurl_enrich
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if proxy_service is not None:
            data["proxy-service"] = proxy_service
        if proxy_service_priority is not None:
            data["proxy-service-priority"] = proxy_service_priority
        if server_addr is not None:
            data["server-addr"] = server_addr
        if server_device is not None:
            data["server-device"] = server_device
        if server_name is not None:
            data["server-name"] = server_name
        if server_port is not None:
            data["server-port"] = server_port
        if signature is not None:
            data["signature"] = signature
        if sync_metadata is not None:
            data["sync-metadata"] = sync_metadata
        
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

    def delete(self, log_forward: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            log_forward: log-forward parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if log_forward is not None:
            url = "/cli/global/system/log-forward/{log-forward}"
            url = url.replace("{log-forward}", str(log_forward))
        else:
            url = "/cli/global/system/log-forward"
        
        data = {}
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

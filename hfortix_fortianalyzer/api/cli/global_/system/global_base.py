"""
FortiAnalyzer API endpoint: cli.global.system.global

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemGlobal:
    """
    FortiAnalyzer endpoint: cli.global.system.global
    
    
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
        url = "/cli/global/system/global"
        
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
        admin_lockout_duration: int | None = None,
        admin_lockout_method: Literal["ip", "user"] | None = None,
        admin_lockout_threshold: int | None = None,
        admin_ssh_grace_time: int | None = None,
        adom_mode: Literal["normal", "advanced"] | None = None,
        adom_select: Literal["disable", "enable"] | None = None,
        adom_status: Literal["disable", "enable"] | None = None,
        ai_mode: Literal["disable", "enable"] | None = None,
        apache_mode: Literal["event", "prefork"] | None = None,
        apache_wsgi_processes: int | None = None,
        api_ip_binding: Literal["disable", "enable"] | None = None,
        auth_dev_restapi_allowlist: Literal["disable", "enable"] | None = None,
        backup_compression: Literal["none", "low", "normal", "high"] | None = None,
        backup_to_subfolders: Literal["disable", "enable"] | None = None,
        cli_auth: Literal["disable", "enable"] | None = None,
        clone_name_option: Literal["default", "keep"] | None = None,
        clt_cert_req: Literal["disable", "enable", "optional"] | None = None,
        console_output: Literal["standard", "more"] | None = None,
        contentpack_fgt_install: Literal["disable", "enable"] | None = None,
        country_flag: Literal["disable", "enable"] | None = None,
        create_revision: Literal["disable", "enable"] | None = None,
        daylightsavetime: Literal["disable", "enable"] | None = None,
        debug_tool: Literal["disable", "enable"] | None = None,
        default_logview_auto_completion: Literal["disable", "enable"] | None = None,
        default_search_mode: Literal["filter-based", "advanced"] | None = None,
        detect_unregistered_log_device: Literal["disable", "enable"] | None = None,
        device_view_mode: Literal["regular", "tree"] | None = None,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = None,
        enc_algorithm: Literal["low", "medium", "high", "custom"] | None = None,
        event_correlation_cache_size: int | None = None,
        fabric_storage_pool_quota: int | None = None,
        fabric_storage_pool_size: int | None = None,
        fcp_cfg_service: Literal["disable", "enable"] | None = None,
        fgfm_cert_exclusive: Literal["disable", "enable"] | None = None,
        fgfm_ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        fortiservice_port: int | None = None,
        global_ssl_protocol: Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        gui_curl_timeout: int | None = None,
        gui_feature_visibility_mode: Literal["per-adom", "per-admin"] | None = None,
        gui_install_preview_concurrency: int | None = None,
        gui_max_objects_per_row: int | None = None,
        gui_polling_interval: int | None = None,
        ha_member_auto_grouping: Literal["disable", "enable"] | None = None,
        hostname: str | None = None,
        jsonapi_log: Literal["disable", "request", "response", "all"] | None = None,
        language: Literal["english", "simch", "japanese", "korean", "spanish", "trach"] | None = None,
        ldap_cache_timeout: int | None = None,
        ldapconntimeout: int | None = None,
        lock_preempt: Literal["disable", "enable"] | None = None,
        log_checksum: Literal["none", "md5", "md5-auth"] | None = None,
        log_checksum_upload: Literal["disable", "enable"] | None = None,
        log_forward_cache_size: int | None = None,
        log_forward_plugin_workers: int | None = None,
        log_mode: Literal["analyzer", "collector"] | None = None,
        management_port: int | None = None,
        mapclient_ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        max_aggregation_tasks: int | None = None,
        max_log_forward: int | None = None,
        max_running_reports: int | None = None,
        multiple_steps_upgrade_in_autolink: Literal["disable", "enable"] | None = None,
        no_copy_permission_check: Literal["disable", "enable"] | None = None,
        no_vip_value_check: Literal["disable", "enable"] | None = None,
        normalized_intf_zone_only: Literal["disable", "enable"] | None = None,
        object_revision_db_max: int | None = None,
        object_revision_mandatory_note: Literal["disable", "enable"] | None = None,
        object_revision_object_max: int | None = None,
        object_revision_status: Literal["disable", "enable"] | None = None,
        oftp_ssl_protocol: Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        policy_object_icon: Literal["disable", "enable"] | None = None,
        policy_object_in_dual_pane: Literal["disable", "enable"] | None = None,
        pre_login_banner: Literal["disable", "enable"] | None = None,
        private_data_encryption: Literal["disable", "enable"] | None = None,
        remoteauthtimeout: int | None = None,
        rpc_log: Literal["disable", "enable"] | None = None,
        search_all_adoms: Literal["disable", "enable"] | None = None,
        skip_ip_check_in_session: Literal["disable", "enable"] | None = None,
        ssl_low_encryption: Literal["disable", "enable"] | None = None,
        ssl_static_key_ciphers: Literal["disable", "enable"] | None = None,
        storage_age_limit: int | None = None,
        table_entry_blink: Literal["disable", "enable"] | None = None,
        task_list_size: int | None = None,
        tftp: Literal["disable", "enable"] | None = None,
        timezone: Literal["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92"] | None = None,
        tunnel_mtu: int | None = None,
        usg: Literal["disable", "enable"] | None = None,
        vm_swappiness: int | None = None,
        workflow_max_sessions: int | None = None,
        admin_host: str | None = None,
        disable_module: list[Any] | None = None,
        fgfm_ca_cert: str | None = None,
        fgfm_local_cert: str | None = None,
        httpd_ssl_protocol: list[Any] | None = None,
        latitude: str | None = None,
        longitude: str | None = None,
        management_ip: str | None = None,
        pre_login_banner_message: str | None = None,
        ssh_enc_algo: list[Any] | None = None,
        ssh_hostkey_algo: list[Any] | None = None,
        ssh_kex_algo: list[Any] | None = None,
        ssh_mac_algo: list[Any] | None = None,
        ssl_cipher_suites: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            admin_host: admin-host parameter
            admin_lockout_duration: admin-lockout-duration parameter
            admin_lockout_method: admin-lockout-method parameter
            admin_lockout_threshold: admin-lockout-threshold parameter
            admin_ssh_grace_time: admin-ssh-grace-time parameter
            adom_mode: adom-mode parameter
            adom_select: adom-select parameter
            adom_status: adom-status parameter
            ai_mode: ai-mode parameter
            apache_mode: apache-mode parameter
            ... (91 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/global"
        
        # Build data payload
        data = {}
        if admin_host is not None:
            data["admin-host"] = admin_host
        if admin_lockout_duration is not None:
            data["admin-lockout-duration"] = admin_lockout_duration
        if admin_lockout_method is not None:
            data["admin-lockout-method"] = admin_lockout_method
        if admin_lockout_threshold is not None:
            data["admin-lockout-threshold"] = admin_lockout_threshold
        if admin_ssh_grace_time is not None:
            data["admin-ssh-grace-time"] = admin_ssh_grace_time
        if adom_mode is not None:
            data["adom-mode"] = adom_mode
        if adom_select is not None:
            data["adom-select"] = adom_select
        if adom_status is not None:
            data["adom-status"] = adom_status
        if ai_mode is not None:
            data["ai-mode"] = ai_mode
        if apache_mode is not None:
            data["apache-mode"] = apache_mode
        if apache_wsgi_processes is not None:
            data["apache-wsgi-processes"] = apache_wsgi_processes
        if api_ip_binding is not None:
            data["api-ip-binding"] = api_ip_binding
        if auth_dev_restapi_allowlist is not None:
            data["auth-dev-restapi-allowlist"] = auth_dev_restapi_allowlist
        if backup_compression is not None:
            data["backup-compression"] = backup_compression
        if backup_to_subfolders is not None:
            data["backup-to-subfolders"] = backup_to_subfolders
        if cli_auth is not None:
            data["cli-auth"] = cli_auth
        if clone_name_option is not None:
            data["clone-name-option"] = clone_name_option
        if clt_cert_req is not None:
            data["clt-cert-req"] = clt_cert_req
        if console_output is not None:
            data["console-output"] = console_output
        if contentpack_fgt_install is not None:
            data["contentpack-fgt-install"] = contentpack_fgt_install
        if country_flag is not None:
            data["country-flag"] = country_flag
        if create_revision is not None:
            data["create-revision"] = create_revision
        if daylightsavetime is not None:
            data["daylightsavetime"] = daylightsavetime
        if debug_tool is not None:
            data["debug-tool"] = debug_tool
        if default_logview_auto_completion is not None:
            data["default-logview-auto-completion"] = default_logview_auto_completion
        if default_search_mode is not None:
            data["default-search-mode"] = default_search_mode
        if detect_unregistered_log_device is not None:
            data["detect-unregistered-log-device"] = detect_unregistered_log_device
        if device_view_mode is not None:
            data["device-view-mode"] = device_view_mode
        if dh_params is not None:
            data["dh-params"] = dh_params
        if disable_module is not None:
            data["disable-module"] = disable_module
        if enc_algorithm is not None:
            data["enc-algorithm"] = enc_algorithm
        if event_correlation_cache_size is not None:
            data["event-correlation-cache-size"] = event_correlation_cache_size
        if fabric_storage_pool_quota is not None:
            data["fabric-storage-pool-quota"] = fabric_storage_pool_quota
        if fabric_storage_pool_size is not None:
            data["fabric-storage-pool-size"] = fabric_storage_pool_size
        if fcp_cfg_service is not None:
            data["fcp-cfg-service"] = fcp_cfg_service
        if fgfm_ca_cert is not None:
            data["fgfm-ca-cert"] = fgfm_ca_cert
        if fgfm_cert_exclusive is not None:
            data["fgfm-cert-exclusive"] = fgfm_cert_exclusive
        if fgfm_local_cert is not None:
            data["fgfm-local-cert"] = fgfm_local_cert
        if fgfm_ssl_protocol is not None:
            data["fgfm-ssl-protocol"] = fgfm_ssl_protocol
        if fortiservice_port is not None:
            data["fortiservice-port"] = fortiservice_port
        if global_ssl_protocol is not None:
            data["global-ssl-protocol"] = global_ssl_protocol
        if gui_curl_timeout is not None:
            data["gui-curl-timeout"] = gui_curl_timeout
        if gui_feature_visibility_mode is not None:
            data["gui-feature-visibility-mode"] = gui_feature_visibility_mode
        if gui_install_preview_concurrency is not None:
            data["gui-install-preview-concurrency"] = gui_install_preview_concurrency
        if gui_max_objects_per_row is not None:
            data["gui-max-objects-per-row"] = gui_max_objects_per_row
        if gui_polling_interval is not None:
            data["gui-polling-interval"] = gui_polling_interval
        if ha_member_auto_grouping is not None:
            data["ha-member-auto-grouping"] = ha_member_auto_grouping
        if hostname is not None:
            data["hostname"] = hostname
        if httpd_ssl_protocol is not None:
            data["httpd-ssl-protocol"] = httpd_ssl_protocol
        if jsonapi_log is not None:
            data["jsonapi-log"] = jsonapi_log
        if language is not None:
            data["language"] = language
        if latitude is not None:
            data["latitude"] = latitude
        if ldap_cache_timeout is not None:
            data["ldap-cache-timeout"] = ldap_cache_timeout
        if ldapconntimeout is not None:
            data["ldapconntimeout"] = ldapconntimeout
        if lock_preempt is not None:
            data["lock-preempt"] = lock_preempt
        if log_checksum is not None:
            data["log-checksum"] = log_checksum
        if log_checksum_upload is not None:
            data["log-checksum-upload"] = log_checksum_upload
        if log_forward_cache_size is not None:
            data["log-forward-cache-size"] = log_forward_cache_size
        if log_forward_plugin_workers is not None:
            data["log-forward-plugin-workers"] = log_forward_plugin_workers
        if log_mode is not None:
            data["log-mode"] = log_mode
        if longitude is not None:
            data["longitude"] = longitude
        if management_ip is not None:
            data["management-ip"] = management_ip
        if management_port is not None:
            data["management-port"] = management_port
        if mapclient_ssl_protocol is not None:
            data["mapclient-ssl-protocol"] = mapclient_ssl_protocol
        if max_aggregation_tasks is not None:
            data["max-aggregation-tasks"] = max_aggregation_tasks
        if max_log_forward is not None:
            data["max-log-forward"] = max_log_forward
        if max_running_reports is not None:
            data["max-running-reports"] = max_running_reports
        if multiple_steps_upgrade_in_autolink is not None:
            data["multiple-steps-upgrade-in-autolink"] = multiple_steps_upgrade_in_autolink
        if no_copy_permission_check is not None:
            data["no-copy-permission-check"] = no_copy_permission_check
        if no_vip_value_check is not None:
            data["no-vip-value-check"] = no_vip_value_check
        if normalized_intf_zone_only is not None:
            data["normalized-intf-zone-only"] = normalized_intf_zone_only
        if object_revision_db_max is not None:
            data["object-revision-db-max"] = object_revision_db_max
        if object_revision_mandatory_note is not None:
            data["object-revision-mandatory-note"] = object_revision_mandatory_note
        if object_revision_object_max is not None:
            data["object-revision-object-max"] = object_revision_object_max
        if object_revision_status is not None:
            data["object-revision-status"] = object_revision_status
        if oftp_ssl_protocol is not None:
            data["oftp-ssl-protocol"] = oftp_ssl_protocol
        if policy_object_icon is not None:
            data["policy-object-icon"] = policy_object_icon
        if policy_object_in_dual_pane is not None:
            data["policy-object-in-dual-pane"] = policy_object_in_dual_pane
        if pre_login_banner is not None:
            data["pre-login-banner"] = pre_login_banner
        if pre_login_banner_message is not None:
            data["pre-login-banner-message"] = pre_login_banner_message
        if private_data_encryption is not None:
            data["private-data-encryption"] = private_data_encryption
        if remoteauthtimeout is not None:
            data["remoteauthtimeout"] = remoteauthtimeout
        if rpc_log is not None:
            data["rpc-log"] = rpc_log
        if search_all_adoms is not None:
            data["search-all-adoms"] = search_all_adoms
        if skip_ip_check_in_session is not None:
            data["skip-ip-check-in-session"] = skip_ip_check_in_session
        if ssh_enc_algo is not None:
            data["ssh-enc-algo"] = ssh_enc_algo
        if ssh_hostkey_algo is not None:
            data["ssh-hostkey-algo"] = ssh_hostkey_algo
        if ssh_kex_algo is not None:
            data["ssh-kex-algo"] = ssh_kex_algo
        if ssh_mac_algo is not None:
            data["ssh-mac-algo"] = ssh_mac_algo
        if ssl_cipher_suites is not None:
            data["ssl-cipher-suites"] = ssl_cipher_suites
        if ssl_low_encryption is not None:
            data["ssl-low-encryption"] = ssl_low_encryption
        if ssl_static_key_ciphers is not None:
            data["ssl-static-key-ciphers"] = ssl_static_key_ciphers
        if storage_age_limit is not None:
            data["storage-age-limit"] = storage_age_limit
        if table_entry_blink is not None:
            data["table-entry-blink"] = table_entry_blink
        if task_list_size is not None:
            data["task-list-size"] = task_list_size
        if tftp is not None:
            data["tftp"] = tftp
        if timezone is not None:
            data["timezone"] = timezone
        if tunnel_mtu is not None:
            data["tunnel-mtu"] = tunnel_mtu
        if usg is not None:
            data["usg"] = usg
        if vm_swappiness is not None:
            data["vm-swappiness"] = vm_swappiness
        if workflow_max_sessions is not None:
            data["workflow-max-sessions"] = workflow_max_sessions
        
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
        admin_lockout_duration: int | None = None,
        admin_lockout_method: Literal["ip", "user"] | None = None,
        admin_lockout_threshold: int | None = None,
        admin_ssh_grace_time: int | None = None,
        adom_mode: Literal["normal", "advanced"] | None = None,
        adom_select: Literal["disable", "enable"] | None = None,
        adom_status: Literal["disable", "enable"] | None = None,
        ai_mode: Literal["disable", "enable"] | None = None,
        apache_mode: Literal["event", "prefork"] | None = None,
        apache_wsgi_processes: int | None = None,
        api_ip_binding: Literal["disable", "enable"] | None = None,
        auth_dev_restapi_allowlist: Literal["disable", "enable"] | None = None,
        backup_compression: Literal["none", "low", "normal", "high"] | None = None,
        backup_to_subfolders: Literal["disable", "enable"] | None = None,
        cli_auth: Literal["disable", "enable"] | None = None,
        clone_name_option: Literal["default", "keep"] | None = None,
        clt_cert_req: Literal["disable", "enable", "optional"] | None = None,
        console_output: Literal["standard", "more"] | None = None,
        contentpack_fgt_install: Literal["disable", "enable"] | None = None,
        country_flag: Literal["disable", "enable"] | None = None,
        create_revision: Literal["disable", "enable"] | None = None,
        daylightsavetime: Literal["disable", "enable"] | None = None,
        debug_tool: Literal["disable", "enable"] | None = None,
        default_logview_auto_completion: Literal["disable", "enable"] | None = None,
        default_search_mode: Literal["filter-based", "advanced"] | None = None,
        detect_unregistered_log_device: Literal["disable", "enable"] | None = None,
        device_view_mode: Literal["regular", "tree"] | None = None,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = None,
        enc_algorithm: Literal["low", "medium", "high", "custom"] | None = None,
        event_correlation_cache_size: int | None = None,
        fabric_storage_pool_quota: int | None = None,
        fabric_storage_pool_size: int | None = None,
        fcp_cfg_service: Literal["disable", "enable"] | None = None,
        fgfm_cert_exclusive: Literal["disable", "enable"] | None = None,
        fgfm_ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        fortiservice_port: int | None = None,
        global_ssl_protocol: Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        gui_curl_timeout: int | None = None,
        gui_feature_visibility_mode: Literal["per-adom", "per-admin"] | None = None,
        gui_install_preview_concurrency: int | None = None,
        gui_max_objects_per_row: int | None = None,
        gui_polling_interval: int | None = None,
        ha_member_auto_grouping: Literal["disable", "enable"] | None = None,
        hostname: str | None = None,
        jsonapi_log: Literal["disable", "request", "response", "all"] | None = None,
        language: Literal["english", "simch", "japanese", "korean", "spanish", "trach"] | None = None,
        ldap_cache_timeout: int | None = None,
        ldapconntimeout: int | None = None,
        lock_preempt: Literal["disable", "enable"] | None = None,
        log_checksum: Literal["none", "md5", "md5-auth"] | None = None,
        log_checksum_upload: Literal["disable", "enable"] | None = None,
        log_forward_cache_size: int | None = None,
        log_forward_plugin_workers: int | None = None,
        log_mode: Literal["analyzer", "collector"] | None = None,
        management_port: int | None = None,
        mapclient_ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        max_aggregation_tasks: int | None = None,
        max_log_forward: int | None = None,
        max_running_reports: int | None = None,
        multiple_steps_upgrade_in_autolink: Literal["disable", "enable"] | None = None,
        no_copy_permission_check: Literal["disable", "enable"] | None = None,
        no_vip_value_check: Literal["disable", "enable"] | None = None,
        normalized_intf_zone_only: Literal["disable", "enable"] | None = None,
        object_revision_db_max: int | None = None,
        object_revision_mandatory_note: Literal["disable", "enable"] | None = None,
        object_revision_object_max: int | None = None,
        object_revision_status: Literal["disable", "enable"] | None = None,
        oftp_ssl_protocol: Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        policy_object_icon: Literal["disable", "enable"] | None = None,
        policy_object_in_dual_pane: Literal["disable", "enable"] | None = None,
        pre_login_banner: Literal["disable", "enable"] | None = None,
        private_data_encryption: Literal["disable", "enable"] | None = None,
        remoteauthtimeout: int | None = None,
        rpc_log: Literal["disable", "enable"] | None = None,
        search_all_adoms: Literal["disable", "enable"] | None = None,
        skip_ip_check_in_session: Literal["disable", "enable"] | None = None,
        ssl_low_encryption: Literal["disable", "enable"] | None = None,
        ssl_static_key_ciphers: Literal["disable", "enable"] | None = None,
        storage_age_limit: int | None = None,
        table_entry_blink: Literal["disable", "enable"] | None = None,
        task_list_size: int | None = None,
        tftp: Literal["disable", "enable"] | None = None,
        timezone: Literal["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92"] | None = None,
        tunnel_mtu: int | None = None,
        usg: Literal["disable", "enable"] | None = None,
        vm_swappiness: int | None = None,
        workflow_max_sessions: int | None = None,
        admin_host: str | None = None,
        disable_module: list[Any] | None = None,
        fgfm_ca_cert: str | None = None,
        fgfm_local_cert: str | None = None,
        httpd_ssl_protocol: list[Any] | None = None,
        latitude: str | None = None,
        longitude: str | None = None,
        management_ip: str | None = None,
        pre_login_banner_message: str | None = None,
        ssh_enc_algo: list[Any] | None = None,
        ssh_hostkey_algo: list[Any] | None = None,
        ssh_kex_algo: list[Any] | None = None,
        ssh_mac_algo: list[Any] | None = None,
        ssl_cipher_suites: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            admin_host: admin-host parameter
            admin_lockout_duration: admin-lockout-duration parameter
            admin_lockout_method: admin-lockout-method parameter
            admin_lockout_threshold: admin-lockout-threshold parameter
            admin_ssh_grace_time: admin-ssh-grace-time parameter
            adom_mode: adom-mode parameter
            adom_select: adom-select parameter
            adom_status: adom-status parameter
            ai_mode: ai-mode parameter
            apache_mode: apache-mode parameter
            ... (91 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/global"
        
        # Build data payload
        data = {}
        if admin_host is not None:
            data["admin-host"] = admin_host
        if admin_lockout_duration is not None:
            data["admin-lockout-duration"] = admin_lockout_duration
        if admin_lockout_method is not None:
            data["admin-lockout-method"] = admin_lockout_method
        if admin_lockout_threshold is not None:
            data["admin-lockout-threshold"] = admin_lockout_threshold
        if admin_ssh_grace_time is not None:
            data["admin-ssh-grace-time"] = admin_ssh_grace_time
        if adom_mode is not None:
            data["adom-mode"] = adom_mode
        if adom_select is not None:
            data["adom-select"] = adom_select
        if adom_status is not None:
            data["adom-status"] = adom_status
        if ai_mode is not None:
            data["ai-mode"] = ai_mode
        if apache_mode is not None:
            data["apache-mode"] = apache_mode
        if apache_wsgi_processes is not None:
            data["apache-wsgi-processes"] = apache_wsgi_processes
        if api_ip_binding is not None:
            data["api-ip-binding"] = api_ip_binding
        if auth_dev_restapi_allowlist is not None:
            data["auth-dev-restapi-allowlist"] = auth_dev_restapi_allowlist
        if backup_compression is not None:
            data["backup-compression"] = backup_compression
        if backup_to_subfolders is not None:
            data["backup-to-subfolders"] = backup_to_subfolders
        if cli_auth is not None:
            data["cli-auth"] = cli_auth
        if clone_name_option is not None:
            data["clone-name-option"] = clone_name_option
        if clt_cert_req is not None:
            data["clt-cert-req"] = clt_cert_req
        if console_output is not None:
            data["console-output"] = console_output
        if contentpack_fgt_install is not None:
            data["contentpack-fgt-install"] = contentpack_fgt_install
        if country_flag is not None:
            data["country-flag"] = country_flag
        if create_revision is not None:
            data["create-revision"] = create_revision
        if daylightsavetime is not None:
            data["daylightsavetime"] = daylightsavetime
        if debug_tool is not None:
            data["debug-tool"] = debug_tool
        if default_logview_auto_completion is not None:
            data["default-logview-auto-completion"] = default_logview_auto_completion
        if default_search_mode is not None:
            data["default-search-mode"] = default_search_mode
        if detect_unregistered_log_device is not None:
            data["detect-unregistered-log-device"] = detect_unregistered_log_device
        if device_view_mode is not None:
            data["device-view-mode"] = device_view_mode
        if dh_params is not None:
            data["dh-params"] = dh_params
        if disable_module is not None:
            data["disable-module"] = disable_module
        if enc_algorithm is not None:
            data["enc-algorithm"] = enc_algorithm
        if event_correlation_cache_size is not None:
            data["event-correlation-cache-size"] = event_correlation_cache_size
        if fabric_storage_pool_quota is not None:
            data["fabric-storage-pool-quota"] = fabric_storage_pool_quota
        if fabric_storage_pool_size is not None:
            data["fabric-storage-pool-size"] = fabric_storage_pool_size
        if fcp_cfg_service is not None:
            data["fcp-cfg-service"] = fcp_cfg_service
        if fgfm_ca_cert is not None:
            data["fgfm-ca-cert"] = fgfm_ca_cert
        if fgfm_cert_exclusive is not None:
            data["fgfm-cert-exclusive"] = fgfm_cert_exclusive
        if fgfm_local_cert is not None:
            data["fgfm-local-cert"] = fgfm_local_cert
        if fgfm_ssl_protocol is not None:
            data["fgfm-ssl-protocol"] = fgfm_ssl_protocol
        if fortiservice_port is not None:
            data["fortiservice-port"] = fortiservice_port
        if global_ssl_protocol is not None:
            data["global-ssl-protocol"] = global_ssl_protocol
        if gui_curl_timeout is not None:
            data["gui-curl-timeout"] = gui_curl_timeout
        if gui_feature_visibility_mode is not None:
            data["gui-feature-visibility-mode"] = gui_feature_visibility_mode
        if gui_install_preview_concurrency is not None:
            data["gui-install-preview-concurrency"] = gui_install_preview_concurrency
        if gui_max_objects_per_row is not None:
            data["gui-max-objects-per-row"] = gui_max_objects_per_row
        if gui_polling_interval is not None:
            data["gui-polling-interval"] = gui_polling_interval
        if ha_member_auto_grouping is not None:
            data["ha-member-auto-grouping"] = ha_member_auto_grouping
        if hostname is not None:
            data["hostname"] = hostname
        if httpd_ssl_protocol is not None:
            data["httpd-ssl-protocol"] = httpd_ssl_protocol
        if jsonapi_log is not None:
            data["jsonapi-log"] = jsonapi_log
        if language is not None:
            data["language"] = language
        if latitude is not None:
            data["latitude"] = latitude
        if ldap_cache_timeout is not None:
            data["ldap-cache-timeout"] = ldap_cache_timeout
        if ldapconntimeout is not None:
            data["ldapconntimeout"] = ldapconntimeout
        if lock_preempt is not None:
            data["lock-preempt"] = lock_preempt
        if log_checksum is not None:
            data["log-checksum"] = log_checksum
        if log_checksum_upload is not None:
            data["log-checksum-upload"] = log_checksum_upload
        if log_forward_cache_size is not None:
            data["log-forward-cache-size"] = log_forward_cache_size
        if log_forward_plugin_workers is not None:
            data["log-forward-plugin-workers"] = log_forward_plugin_workers
        if log_mode is not None:
            data["log-mode"] = log_mode
        if longitude is not None:
            data["longitude"] = longitude
        if management_ip is not None:
            data["management-ip"] = management_ip
        if management_port is not None:
            data["management-port"] = management_port
        if mapclient_ssl_protocol is not None:
            data["mapclient-ssl-protocol"] = mapclient_ssl_protocol
        if max_aggregation_tasks is not None:
            data["max-aggregation-tasks"] = max_aggregation_tasks
        if max_log_forward is not None:
            data["max-log-forward"] = max_log_forward
        if max_running_reports is not None:
            data["max-running-reports"] = max_running_reports
        if multiple_steps_upgrade_in_autolink is not None:
            data["multiple-steps-upgrade-in-autolink"] = multiple_steps_upgrade_in_autolink
        if no_copy_permission_check is not None:
            data["no-copy-permission-check"] = no_copy_permission_check
        if no_vip_value_check is not None:
            data["no-vip-value-check"] = no_vip_value_check
        if normalized_intf_zone_only is not None:
            data["normalized-intf-zone-only"] = normalized_intf_zone_only
        if object_revision_db_max is not None:
            data["object-revision-db-max"] = object_revision_db_max
        if object_revision_mandatory_note is not None:
            data["object-revision-mandatory-note"] = object_revision_mandatory_note
        if object_revision_object_max is not None:
            data["object-revision-object-max"] = object_revision_object_max
        if object_revision_status is not None:
            data["object-revision-status"] = object_revision_status
        if oftp_ssl_protocol is not None:
            data["oftp-ssl-protocol"] = oftp_ssl_protocol
        if policy_object_icon is not None:
            data["policy-object-icon"] = policy_object_icon
        if policy_object_in_dual_pane is not None:
            data["policy-object-in-dual-pane"] = policy_object_in_dual_pane
        if pre_login_banner is not None:
            data["pre-login-banner"] = pre_login_banner
        if pre_login_banner_message is not None:
            data["pre-login-banner-message"] = pre_login_banner_message
        if private_data_encryption is not None:
            data["private-data-encryption"] = private_data_encryption
        if remoteauthtimeout is not None:
            data["remoteauthtimeout"] = remoteauthtimeout
        if rpc_log is not None:
            data["rpc-log"] = rpc_log
        if search_all_adoms is not None:
            data["search-all-adoms"] = search_all_adoms
        if skip_ip_check_in_session is not None:
            data["skip-ip-check-in-session"] = skip_ip_check_in_session
        if ssh_enc_algo is not None:
            data["ssh-enc-algo"] = ssh_enc_algo
        if ssh_hostkey_algo is not None:
            data["ssh-hostkey-algo"] = ssh_hostkey_algo
        if ssh_kex_algo is not None:
            data["ssh-kex-algo"] = ssh_kex_algo
        if ssh_mac_algo is not None:
            data["ssh-mac-algo"] = ssh_mac_algo
        if ssl_cipher_suites is not None:
            data["ssl-cipher-suites"] = ssl_cipher_suites
        if ssl_low_encryption is not None:
            data["ssl-low-encryption"] = ssl_low_encryption
        if ssl_static_key_ciphers is not None:
            data["ssl-static-key-ciphers"] = ssl_static_key_ciphers
        if storage_age_limit is not None:
            data["storage-age-limit"] = storage_age_limit
        if table_entry_blink is not None:
            data["table-entry-blink"] = table_entry_blink
        if task_list_size is not None:
            data["task-list-size"] = task_list_size
        if tftp is not None:
            data["tftp"] = tftp
        if timezone is not None:
            data["timezone"] = timezone
        if tunnel_mtu is not None:
            data["tunnel-mtu"] = tunnel_mtu
        if usg is not None:
            data["usg"] = usg
        if vm_swappiness is not None:
            data["vm-swappiness"] = vm_swappiness
        if workflow_max_sessions is not None:
            data["workflow-max-sessions"] = workflow_max_sessions
        
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

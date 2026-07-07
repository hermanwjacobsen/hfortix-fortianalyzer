"""Type stubs for cli.global.system.global"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemGlobalGetItem:
    """Item yielded when iterating over CliGlobalSystemGlobalGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def admin_host(self) -> str: ...
    @property
    def admin_lockout_duration(self) -> int: ...
    @property
    def admin_lockout_method(self) -> Literal["ip", "user"]: ...
    @property
    def admin_lockout_threshold(self) -> int: ...
    @property
    def admin_ssh_grace_time(self) -> int: ...
    @property
    def adom_mode(self) -> Literal["normal", "advanced"]: ...
    @property
    def adom_select(self) -> Literal["disable", "enable"]: ...
    @property
    def adom_status(self) -> Literal["disable", "enable"]: ...
    @property
    def ai_mode(self) -> Literal["disable", "enable"]: ...
    @property
    def apache_mode(self) -> Literal["event", "prefork"]: ...
    @property
    def apache_wsgi_processes(self) -> int: ...
    @property
    def api_ip_binding(self) -> Literal["disable", "enable"]: ...
    @property
    def auth_dev_restapi_allowlist(self) -> Literal["disable", "enable"]: ...
    @property
    def backup_compression(self) -> Literal["none", "low", "normal", "high"]: ...
    @property
    def backup_to_subfolders(self) -> Literal["disable", "enable"]: ...
    @property
    def cli_auth(self) -> Literal["disable", "enable"]: ...
    @property
    def clone_name_option(self) -> Literal["default", "keep"]: ...
    @property
    def clt_cert_req(self) -> Literal["disable", "enable", "optional"]: ...
    @property
    def console_output(self) -> Literal["standard", "more"]: ...
    @property
    def contentpack_fgt_install(self) -> Literal["disable", "enable"]: ...
    @property
    def country_flag(self) -> Literal["disable", "enable"]: ...
    @property
    def create_revision(self) -> Literal["disable", "enable"]: ...
    @property
    def daylightsavetime(self) -> Literal["disable", "enable"]: ...
    @property
    def debug_tool(self) -> Literal["disable", "enable"]: ...
    @property
    def default_logview_auto_completion(self) -> Literal["disable", "enable"]: ...
    @property
    def default_search_mode(self) -> Literal["filter-based", "advanced"]: ...
    @property
    def detect_unregistered_log_device(self) -> Literal["disable", "enable"]: ...
    @property
    def device_view_mode(self) -> Literal["regular", "tree"]: ...
    @property
    def dh_params(self) -> Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"]: ...
    @property
    def disable_module(self) -> list[Any]: ...
    @property
    def enc_algorithm(self) -> Literal["low", "medium", "high", "custom"]: ...
    @property
    def event_correlation_cache_size(self) -> int: ...
    @property
    def fabric_storage_pool_quota(self) -> int: ...
    @property
    def fabric_storage_pool_size(self) -> int: ...
    @property
    def fcp_cfg_service(self) -> Literal["disable", "enable"]: ...
    @property
    def fgfm_ca_cert(self) -> str: ...
    @property
    def fgfm_cert_exclusive(self) -> Literal["disable", "enable"]: ...
    @property
    def fgfm_local_cert(self) -> str: ...
    @property
    def fgfm_ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def fortiservice_port(self) -> int: ...
    @property
    def global_ssl_protocol(self) -> Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def gui_curl_timeout(self) -> int: ...
    @property
    def gui_feature_visibility_mode(self) -> Literal["per-adom", "per-admin"]: ...
    @property
    def gui_install_preview_concurrency(self) -> int: ...
    @property
    def gui_max_objects_per_row(self) -> int: ...
    @property
    def gui_polling_interval(self) -> int: ...
    @property
    def ha_member_auto_grouping(self) -> Literal["disable", "enable"]: ...
    @property
    def hostname(self) -> str: ...
    @property
    def httpd_ssl_protocol(self) -> list[Any]: ...
    @property
    def jsonapi_log(self) -> Literal["disable", "request", "response", "all"]: ...
    @property
    def language(self) -> Literal["english", "simch", "japanese", "korean", "spanish", "trach"]: ...
    @property
    def latitude(self) -> str: ...
    @property
    def ldap_cache_timeout(self) -> int: ...
    @property
    def ldapconntimeout(self) -> int: ...
    @property
    def lock_preempt(self) -> Literal["disable", "enable"]: ...
    @property
    def log_checksum(self) -> Literal["none", "md5", "md5-auth"]: ...
    @property
    def log_checksum_upload(self) -> Literal["disable", "enable"]: ...
    @property
    def log_forward_cache_size(self) -> int: ...
    @property
    def log_forward_plugin_workers(self) -> int: ...
    @property
    def log_mode(self) -> Literal["analyzer", "collector"]: ...
    @property
    def longitude(self) -> str: ...
    @property
    def management_ip(self) -> str: ...
    @property
    def management_port(self) -> int: ...
    @property
    def mapclient_ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def max_aggregation_tasks(self) -> int: ...
    @property
    def max_log_forward(self) -> int: ...
    @property
    def max_running_reports(self) -> int: ...
    @property
    def multiple_steps_upgrade_in_autolink(self) -> Literal["disable", "enable"]: ...
    @property
    def no_copy_permission_check(self) -> Literal["disable", "enable"]: ...
    @property
    def no_vip_value_check(self) -> Literal["disable", "enable"]: ...
    @property
    def normalized_intf_zone_only(self) -> Literal["disable", "enable"]: ...
    @property
    def object_revision_db_max(self) -> int: ...
    @property
    def object_revision_mandatory_note(self) -> Literal["disable", "enable"]: ...
    @property
    def object_revision_object_max(self) -> int: ...
    @property
    def object_revision_status(self) -> Literal["disable", "enable"]: ...
    @property
    def oftp_ssl_protocol(self) -> Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def policy_object_icon(self) -> Literal["disable", "enable"]: ...
    @property
    def policy_object_in_dual_pane(self) -> Literal["disable", "enable"]: ...
    @property
    def pre_login_banner(self) -> Literal["disable", "enable"]: ...
    @property
    def pre_login_banner_message(self) -> str: ...
    @property
    def private_data_encryption(self) -> Literal["disable", "enable"]: ...
    @property
    def remoteauthtimeout(self) -> int: ...
    @property
    def rpc_log(self) -> Literal["disable", "enable"]: ...
    @property
    def search_all_adoms(self) -> Literal["disable", "enable"]: ...
    @property
    def skip_ip_check_in_session(self) -> Literal["disable", "enable"]: ...
    @property
    def ssh_enc_algo(self) -> list[Any]: ...
    @property
    def ssh_hostkey_algo(self) -> list[Any]: ...
    @property
    def ssh_kex_algo(self) -> list[Any]: ...
    @property
    def ssh_mac_algo(self) -> list[Any]: ...
    @property
    def ssl_cipher_suites(self) -> list[SslCipherSuitesItem]: ...
    @property
    def ssl_low_encryption(self) -> Literal["disable", "enable"]: ...
    @property
    def ssl_static_key_ciphers(self) -> Literal["disable", "enable"]: ...
    @property
    def storage_age_limit(self) -> int: ...
    @property
    def table_entry_blink(self) -> Literal["disable", "enable"]: ...
    @property
    def task_list_size(self) -> int: ...
    @property
    def tftp(self) -> Literal["disable", "enable"]: ...
    @property
    def timezone(self) -> Literal["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92"]: ...
    @property
    def tunnel_mtu(self) -> int: ...
    @property
    def usg(self) -> Literal["disable", "enable"]: ...
    @property
    def vm_swappiness(self) -> int: ...
    @property
    def workflow_max_sessions(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class SslCipherSuitesItem:
    """Nested item type for ssl-cipher-suites array."""

    @property
    def cipher(self) -> str: ...
    @property
    def priority(self) -> int: ...
    @property
    def version(self) -> Literal["tls1.2-or-below", "tls1.3"]: ...


class CliGlobalSystemGlobalGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemGlobalGet endpoint with autocomplete support."""

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
    def admin_host(self) -> str | None:
        """Field: admin-host"""
        ...

    @property
    def admin_lockout_duration(self) -> int | None:
        """Field: admin-lockout-duration"""
        ...

    @property
    def admin_lockout_method(self) -> Literal["ip", "user"] | None:
        """Field: admin-lockout-method"""
        ...

    @property
    def admin_lockout_threshold(self) -> int | None:
        """Field: admin-lockout-threshold"""
        ...

    @property
    def admin_ssh_grace_time(self) -> int | None:
        """Field: admin-ssh-grace-time"""
        ...

    @property
    def adom_mode(self) -> Literal["normal", "advanced"] | None:
        """Field: adom-mode"""
        ...

    @property
    def adom_select(self) -> Literal["disable", "enable"] | None:
        """Field: adom-select"""
        ...

    @property
    def adom_status(self) -> Literal["disable", "enable"] | None:
        """Field: adom-status"""
        ...

    @property
    def ai_mode(self) -> Literal["disable", "enable"] | None:
        """Field: ai-mode"""
        ...

    @property
    def apache_mode(self) -> Literal["event", "prefork"] | None:
        """Field: apache-mode"""
        ...

    @property
    def apache_wsgi_processes(self) -> int | None:
        """Field: apache-wsgi-processes"""
        ...

    @property
    def api_ip_binding(self) -> Literal["disable", "enable"] | None:
        """Field: api-ip-binding"""
        ...

    @property
    def auth_dev_restapi_allowlist(self) -> Literal["disable", "enable"] | None:
        """Field: auth-dev-restapi-allowlist"""
        ...

    @property
    def backup_compression(self) -> Literal["none", "low", "normal", "high"] | None:
        """Field: backup-compression"""
        ...

    @property
    def backup_to_subfolders(self) -> Literal["disable", "enable"] | None:
        """Field: backup-to-subfolders"""
        ...

    @property
    def cli_auth(self) -> Literal["disable", "enable"] | None:
        """Field: cli-auth"""
        ...

    @property
    def clone_name_option(self) -> Literal["default", "keep"] | None:
        """Field: clone-name-option"""
        ...

    @property
    def clt_cert_req(self) -> Literal["disable", "enable", "optional"] | None:
        """Field: clt-cert-req"""
        ...

    @property
    def console_output(self) -> Literal["standard", "more"] | None:
        """Field: console-output"""
        ...

    @property
    def contentpack_fgt_install(self) -> Literal["disable", "enable"] | None:
        """Field: contentpack-fgt-install"""
        ...

    @property
    def country_flag(self) -> Literal["disable", "enable"] | None:
        """Field: country-flag"""
        ...

    @property
    def create_revision(self) -> Literal["disable", "enable"] | None:
        """Field: create-revision"""
        ...

    @property
    def daylightsavetime(self) -> Literal["disable", "enable"] | None:
        """Field: daylightsavetime"""
        ...

    @property
    def debug_tool(self) -> Literal["disable", "enable"] | None:
        """Field: debug-tool"""
        ...

    @property
    def default_logview_auto_completion(self) -> Literal["disable", "enable"] | None:
        """Field: default-logview-auto-completion"""
        ...

    @property
    def default_search_mode(self) -> Literal["filter-based", "advanced"] | None:
        """Field: default-search-mode"""
        ...

    @property
    def detect_unregistered_log_device(self) -> Literal["disable", "enable"] | None:
        """Field: detect-unregistered-log-device"""
        ...

    @property
    def device_view_mode(self) -> Literal["regular", "tree"] | None:
        """Field: device-view-mode"""
        ...

    @property
    def dh_params(self) -> Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None:
        """Field: dh-params"""
        ...

    @property
    def disable_module(self) -> list[Any] | None:
        """Field: disable-module"""
        ...

    @property
    def enc_algorithm(self) -> Literal["low", "medium", "high", "custom"] | None:
        """Field: enc-algorithm"""
        ...

    @property
    def event_correlation_cache_size(self) -> int | None:
        """Field: event-correlation-cache-size"""
        ...

    @property
    def fabric_storage_pool_quota(self) -> int | None:
        """Field: fabric-storage-pool-quota"""
        ...

    @property
    def fabric_storage_pool_size(self) -> int | None:
        """Field: fabric-storage-pool-size"""
        ...

    @property
    def fcp_cfg_service(self) -> Literal["disable", "enable"] | None:
        """Field: fcp-cfg-service"""
        ...

    @property
    def fgfm_ca_cert(self) -> str | None:
        """Field: fgfm-ca-cert"""
        ...

    @property
    def fgfm_cert_exclusive(self) -> Literal["disable", "enable"] | None:
        """Field: fgfm-cert-exclusive"""
        ...

    @property
    def fgfm_local_cert(self) -> str | None:
        """Field: fgfm-local-cert"""
        ...

    @property
    def fgfm_ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: fgfm-ssl-protocol"""
        ...

    @property
    def fortiservice_port(self) -> int | None:
        """Field: fortiservice-port"""
        ...

    @property
    def global_ssl_protocol(self) -> Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: global-ssl-protocol"""
        ...

    @property
    def gui_curl_timeout(self) -> int | None:
        """Field: gui-curl-timeout"""
        ...

    @property
    def gui_feature_visibility_mode(self) -> Literal["per-adom", "per-admin"] | None:
        """Field: gui-feature-visibility-mode"""
        ...

    @property
    def gui_install_preview_concurrency(self) -> int | None:
        """Field: gui-install-preview-concurrency"""
        ...

    @property
    def gui_max_objects_per_row(self) -> int | None:
        """Field: gui-max-objects-per-row"""
        ...

    @property
    def gui_polling_interval(self) -> int | None:
        """Field: gui-polling-interval"""
        ...

    @property
    def ha_member_auto_grouping(self) -> Literal["disable", "enable"] | None:
        """Field: ha-member-auto-grouping"""
        ...

    @property
    def hostname(self) -> str | None:
        """Field: hostname"""
        ...

    @property
    def httpd_ssl_protocol(self) -> list[Any] | None:
        """Field: httpd-ssl-protocol"""
        ...

    @property
    def jsonapi_log(self) -> Literal["disable", "request", "response", "all"] | None:
        """Field: jsonapi-log"""
        ...

    @property
    def language(self) -> Literal["english", "simch", "japanese", "korean", "spanish", "trach"] | None:
        """Field: language"""
        ...

    @property
    def latitude(self) -> str | None:
        """Field: latitude"""
        ...

    @property
    def ldap_cache_timeout(self) -> int | None:
        """Field: ldap-cache-timeout"""
        ...

    @property
    def ldapconntimeout(self) -> int | None:
        """Field: ldapconntimeout"""
        ...

    @property
    def lock_preempt(self) -> Literal["disable", "enable"] | None:
        """Field: lock-preempt"""
        ...

    @property
    def log_checksum(self) -> Literal["none", "md5", "md5-auth"] | None:
        """Field: log-checksum"""
        ...

    @property
    def log_checksum_upload(self) -> Literal["disable", "enable"] | None:
        """Field: log-checksum-upload"""
        ...

    @property
    def log_forward_cache_size(self) -> int | None:
        """Field: log-forward-cache-size"""
        ...

    @property
    def log_forward_plugin_workers(self) -> int | None:
        """Field: log-forward-plugin-workers"""
        ...

    @property
    def log_mode(self) -> Literal["analyzer", "collector"] | None:
        """Field: log-mode"""
        ...

    @property
    def longitude(self) -> str | None:
        """Field: longitude"""
        ...

    @property
    def management_ip(self) -> str | None:
        """Field: management-ip"""
        ...

    @property
    def management_port(self) -> int | None:
        """Field: management-port"""
        ...

    @property
    def mapclient_ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: mapclient-ssl-protocol"""
        ...

    @property
    def max_aggregation_tasks(self) -> int | None:
        """Field: max-aggregation-tasks"""
        ...

    @property
    def max_log_forward(self) -> int | None:
        """Field: max-log-forward"""
        ...

    @property
    def max_running_reports(self) -> int | None:
        """Field: max-running-reports"""
        ...

    @property
    def multiple_steps_upgrade_in_autolink(self) -> Literal["disable", "enable"] | None:
        """Field: multiple-steps-upgrade-in-autolink"""
        ...

    @property
    def no_copy_permission_check(self) -> Literal["disable", "enable"] | None:
        """Field: no-copy-permission-check"""
        ...

    @property
    def no_vip_value_check(self) -> Literal["disable", "enable"] | None:
        """Field: no-vip-value-check"""
        ...

    @property
    def normalized_intf_zone_only(self) -> Literal["disable", "enable"] | None:
        """Field: normalized-intf-zone-only"""
        ...

    @property
    def object_revision_db_max(self) -> int | None:
        """Field: object-revision-db-max"""
        ...

    @property
    def object_revision_mandatory_note(self) -> Literal["disable", "enable"] | None:
        """Field: object-revision-mandatory-note"""
        ...

    @property
    def object_revision_object_max(self) -> int | None:
        """Field: object-revision-object-max"""
        ...

    @property
    def object_revision_status(self) -> Literal["disable", "enable"] | None:
        """Field: object-revision-status"""
        ...

    @property
    def oftp_ssl_protocol(self) -> Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: oftp-ssl-protocol"""
        ...

    @property
    def policy_object_icon(self) -> Literal["disable", "enable"] | None:
        """Field: policy-object-icon"""
        ...

    @property
    def policy_object_in_dual_pane(self) -> Literal["disable", "enable"] | None:
        """Field: policy-object-in-dual-pane"""
        ...

    @property
    def pre_login_banner(self) -> Literal["disable", "enable"] | None:
        """Field: pre-login-banner"""
        ...

    @property
    def pre_login_banner_message(self) -> str | None:
        """Field: pre-login-banner-message"""
        ...

    @property
    def private_data_encryption(self) -> Literal["disable", "enable"] | None:
        """Field: private-data-encryption"""
        ...

    @property
    def remoteauthtimeout(self) -> int | None:
        """Field: remoteauthtimeout"""
        ...

    @property
    def rpc_log(self) -> Literal["disable", "enable"] | None:
        """Field: rpc-log"""
        ...

    @property
    def search_all_adoms(self) -> Literal["disable", "enable"] | None:
        """Field: search-all-adoms"""
        ...

    @property
    def skip_ip_check_in_session(self) -> Literal["disable", "enable"] | None:
        """Field: skip-ip-check-in-session"""
        ...

    @property
    def ssh_enc_algo(self) -> list[Any] | None:
        """Field: ssh-enc-algo"""
        ...

    @property
    def ssh_hostkey_algo(self) -> list[Any] | None:
        """Field: ssh-hostkey-algo"""
        ...

    @property
    def ssh_kex_algo(self) -> list[Any] | None:
        """Field: ssh-kex-algo"""
        ...

    @property
    def ssh_mac_algo(self) -> list[Any] | None:
        """Field: ssh-mac-algo"""
        ...

    @property
    def ssl_cipher_suites(self) -> list[SslCipherSuitesItem]:
        """Field: ssl-cipher-suites"""
        ...

    @property
    def ssl_low_encryption(self) -> Literal["disable", "enable"] | None:
        """Field: ssl-low-encryption"""
        ...

    @property
    def ssl_static_key_ciphers(self) -> Literal["disable", "enable"] | None:
        """Field: ssl-static-key-ciphers"""
        ...

    @property
    def storage_age_limit(self) -> int | None:
        """Field: storage-age-limit"""
        ...

    @property
    def table_entry_blink(self) -> Literal["disable", "enable"] | None:
        """Field: table-entry-blink"""
        ...

    @property
    def task_list_size(self) -> int | None:
        """Field: task-list-size"""
        ...

    @property
    def tftp(self) -> Literal["disable", "enable"] | None:
        """Field: tftp"""
        ...

    @property
    def timezone(self) -> Literal["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92"] | None:
        """Field: timezone"""
        ...

    @property
    def tunnel_mtu(self) -> int | None:
        """Field: tunnel-mtu"""
        ...

    @property
    def usg(self) -> Literal["disable", "enable"] | None:
        """Field: usg"""
        ...

    @property
    def vm_swappiness(self) -> int | None:
        """Field: vm-swappiness"""
        ...

    @property
    def workflow_max_sessions(self) -> int | None:
        """Field: workflow-max-sessions"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemGlobalGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemGlobal:
    """FortiAnalyzer endpoint: cli.global.system.global"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemGlobalGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        admin_host: str | None = None,
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
        disable_module: list[Any] | None = None,
        enc_algorithm: Literal["low", "medium", "high", "custom"] | None = None,
        event_correlation_cache_size: int | None = None,
        fabric_storage_pool_quota: int | None = None,
        fabric_storage_pool_size: int | None = None,
        fcp_cfg_service: Literal["disable", "enable"] | None = None,
        fgfm_ca_cert: str | None = None,
        fgfm_cert_exclusive: Literal["disable", "enable"] | None = None,
        fgfm_local_cert: str | None = None,
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
        httpd_ssl_protocol: list[Any] | None = None,
        jsonapi_log: Literal["disable", "request", "response", "all"] | None = None,
        language: Literal["english", "simch", "japanese", "korean", "spanish", "trach"] | None = None,
        latitude: str | None = None,
        ldap_cache_timeout: int | None = None,
        ldapconntimeout: int | None = None,
        lock_preempt: Literal["disable", "enable"] | None = None,
        log_checksum: Literal["none", "md5", "md5-auth"] | None = None,
        log_checksum_upload: Literal["disable", "enable"] | None = None,
        log_forward_cache_size: int | None = None,
        log_forward_plugin_workers: int | None = None,
        log_mode: Literal["analyzer", "collector"] | None = None,
        longitude: str | None = None,
        management_ip: str | None = None,
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
        pre_login_banner_message: str | None = None,
        private_data_encryption: Literal["disable", "enable"] | None = None,
        remoteauthtimeout: int | None = None,
        rpc_log: Literal["disable", "enable"] | None = None,
        search_all_adoms: Literal["disable", "enable"] | None = None,
        skip_ip_check_in_session: Literal["disable", "enable"] | None = None,
        ssh_enc_algo: list[Any] | None = None,
        ssh_hostkey_algo: list[Any] | None = None,
        ssh_kex_algo: list[Any] | None = None,
        ssh_mac_algo: list[Any] | None = None,
        ssl_cipher_suites: list[dict[str, Any]] | None = None,
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
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        admin_host: str | None = None,
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
        disable_module: list[Any] | None = None,
        enc_algorithm: Literal["low", "medium", "high", "custom"] | None = None,
        event_correlation_cache_size: int | None = None,
        fabric_storage_pool_quota: int | None = None,
        fabric_storage_pool_size: int | None = None,
        fcp_cfg_service: Literal["disable", "enable"] | None = None,
        fgfm_ca_cert: str | None = None,
        fgfm_cert_exclusive: Literal["disable", "enable"] | None = None,
        fgfm_local_cert: str | None = None,
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
        httpd_ssl_protocol: list[Any] | None = None,
        jsonapi_log: Literal["disable", "request", "response", "all"] | None = None,
        language: Literal["english", "simch", "japanese", "korean", "spanish", "trach"] | None = None,
        latitude: str | None = None,
        ldap_cache_timeout: int | None = None,
        ldapconntimeout: int | None = None,
        lock_preempt: Literal["disable", "enable"] | None = None,
        log_checksum: Literal["none", "md5", "md5-auth"] | None = None,
        log_checksum_upload: Literal["disable", "enable"] | None = None,
        log_forward_cache_size: int | None = None,
        log_forward_plugin_workers: int | None = None,
        log_mode: Literal["analyzer", "collector"] | None = None,
        longitude: str | None = None,
        management_ip: str | None = None,
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
        pre_login_banner_message: str | None = None,
        private_data_encryption: Literal["disable", "enable"] | None = None,
        remoteauthtimeout: int | None = None,
        rpc_log: Literal["disable", "enable"] | None = None,
        search_all_adoms: Literal["disable", "enable"] | None = None,
        skip_ip_check_in_session: Literal["disable", "enable"] | None = None,
        ssh_enc_algo: list[Any] | None = None,
        ssh_hostkey_algo: list[Any] | None = None,
        ssh_kex_algo: list[Any] | None = None,
        ssh_mac_algo: list[Any] | None = None,
        ssl_cipher_suites: list[dict[str, Any]] | None = None,
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
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemGlobal", "CliGlobalSystemGlobalGetResponse"]
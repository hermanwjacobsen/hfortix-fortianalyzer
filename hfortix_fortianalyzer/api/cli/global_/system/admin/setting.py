"""
FortiAnalyzer API endpoint: cli.global.system.admin.setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminSetting:
    """
    FortiAnalyzer endpoint: cli.global.system.admin.setting
    
    
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
        url = "/cli/global/system/admin/setting"
        
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
        access_banner: Literal["disable", "enable"] | None = None,
        admin_httpd_keep_alive_timeout: int | None = None,
        admin_https_redirect: Literal["disable", "enable"] | None = None,
        admin_login_max: int | None = None,
        admin_scp: Literal["disable", "enable"] | None = None,
        admin_server_cert: str | None = None,
        auth_port: int | None = None,
        fgt_gui_proxy: Literal["disable", "enable"] | None = None,
        fgt_gui_proxy_port: int | None = None,
        firmware_upgrade_check: Literal["disable", "enable"] | None = None,
        fsw_ignore_platform_check: Literal["disable", "enable"] | None = None,
        gui_theme: Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None = None,
        http_port: int | None = None,
        https_port: int | None = None,
        idle_timeout: int | None = None,
        idle_timeout_api: int | None = None,
        idle_timeout_gui: int | None = None,
        idle_timeout_sso: int | None = None,
        object_threshold_limit: Literal["disable", "enable"] | None = None,
        object_threshold_limit_value: int | None = None,
        objects_force_deletion: Literal["disable", "enable"] | None = None,
        show_add_multiple: Literal["disable", "enable"] | None = None,
        show_checkbox_in_table: Literal["disable", "enable"] | None = None,
        show_device_import_export: Literal["disable", "enable"] | None = None,
        show_fct_manager: Literal["disable", "enable"] | None = None,
        show_hostname: Literal["disable", "enable"] | None = None,
        show_log_forwarding: Literal["disable", "enable"] | None = None,
        show_sdwan_manager: Literal["disable", "enable"] | None = None,
        unreg_dev_opt: Literal["ignore", "add_no_service", "add_allow_service"] | None = None,
        webadmin_language: Literal["auto_detect", "english", "simplified_chinese", "traditional_chinese", "japanese", "korean", "spanish", "french"] | None = None,
        auth_addr: str | None = None,
        banner_message: str | None = None,
        preferred_fgfm_intf: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            access_banner: access-banner parameter
            admin_httpd_keep_alive_timeout: admin-httpd-keep-alive-timeout parameter
            admin_https_redirect: admin-https-redirect parameter
            admin_login_max: admin-login-max parameter
            admin_scp: admin-scp parameter
            admin_server_cert: admin_server_cert parameter
            auth_addr: auth-addr parameter
            auth_port: auth-port parameter
            banner_message: banner-message parameter
            fgt_gui_proxy: fgt-gui-proxy parameter
            ... (23 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/admin/setting"
        
        # Build data payload
        data = {}
        if access_banner is not None:
            data["access-banner"] = access_banner
        if admin_httpd_keep_alive_timeout is not None:
            data["admin-httpd-keep-alive-timeout"] = admin_httpd_keep_alive_timeout
        if admin_https_redirect is not None:
            data["admin-https-redirect"] = admin_https_redirect
        if admin_login_max is not None:
            data["admin-login-max"] = admin_login_max
        if admin_scp is not None:
            data["admin-scp"] = admin_scp
        if admin_server_cert is not None:
            data["admin_server_cert"] = admin_server_cert
        if auth_addr is not None:
            data["auth-addr"] = auth_addr
        if auth_port is not None:
            data["auth-port"] = auth_port
        if banner_message is not None:
            data["banner-message"] = banner_message
        if fgt_gui_proxy is not None:
            data["fgt-gui-proxy"] = fgt_gui_proxy
        if fgt_gui_proxy_port is not None:
            data["fgt-gui-proxy-port"] = fgt_gui_proxy_port
        if firmware_upgrade_check is not None:
            data["firmware-upgrade-check"] = firmware_upgrade_check
        if fsw_ignore_platform_check is not None:
            data["fsw-ignore-platform-check"] = fsw_ignore_platform_check
        if gui_theme is not None:
            data["gui-theme"] = gui_theme
        if http_port is not None:
            data["http_port"] = http_port
        if https_port is not None:
            data["https_port"] = https_port
        if idle_timeout is not None:
            data["idle_timeout"] = idle_timeout
        if idle_timeout_api is not None:
            data["idle_timeout_api"] = idle_timeout_api
        if idle_timeout_gui is not None:
            data["idle_timeout_gui"] = idle_timeout_gui
        if idle_timeout_sso is not None:
            data["idle_timeout_sso"] = idle_timeout_sso
        if object_threshold_limit is not None:
            data["object-threshold-limit"] = object_threshold_limit
        if object_threshold_limit_value is not None:
            data["object-threshold-limit-value"] = object_threshold_limit_value
        if objects_force_deletion is not None:
            data["objects-force-deletion"] = objects_force_deletion
        if preferred_fgfm_intf is not None:
            data["preferred-fgfm-intf"] = preferred_fgfm_intf
        if show_add_multiple is not None:
            data["show-add-multiple"] = show_add_multiple
        if show_checkbox_in_table is not None:
            data["show-checkbox-in-table"] = show_checkbox_in_table
        if show_device_import_export is not None:
            data["show-device-import-export"] = show_device_import_export
        if show_fct_manager is not None:
            data["show-fct-manager"] = show_fct_manager
        if show_hostname is not None:
            data["show-hostname"] = show_hostname
        if show_log_forwarding is not None:
            data["show-log-forwarding"] = show_log_forwarding
        if show_sdwan_manager is not None:
            data["show-sdwan-manager"] = show_sdwan_manager
        if unreg_dev_opt is not None:
            data["unreg_dev_opt"] = unreg_dev_opt
        if webadmin_language is not None:
            data["webadmin_language"] = webadmin_language
        
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
        access_banner: Literal["disable", "enable"] | None = None,
        admin_httpd_keep_alive_timeout: int | None = None,
        admin_https_redirect: Literal["disable", "enable"] | None = None,
        admin_login_max: int | None = None,
        admin_scp: Literal["disable", "enable"] | None = None,
        admin_server_cert: str | None = None,
        auth_port: int | None = None,
        fgt_gui_proxy: Literal["disable", "enable"] | None = None,
        fgt_gui_proxy_port: int | None = None,
        firmware_upgrade_check: Literal["disable", "enable"] | None = None,
        fsw_ignore_platform_check: Literal["disable", "enable"] | None = None,
        gui_theme: Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None = None,
        http_port: int | None = None,
        https_port: int | None = None,
        idle_timeout: int | None = None,
        idle_timeout_api: int | None = None,
        idle_timeout_gui: int | None = None,
        idle_timeout_sso: int | None = None,
        object_threshold_limit: Literal["disable", "enable"] | None = None,
        object_threshold_limit_value: int | None = None,
        objects_force_deletion: Literal["disable", "enable"] | None = None,
        show_add_multiple: Literal["disable", "enable"] | None = None,
        show_checkbox_in_table: Literal["disable", "enable"] | None = None,
        show_device_import_export: Literal["disable", "enable"] | None = None,
        show_fct_manager: Literal["disable", "enable"] | None = None,
        show_hostname: Literal["disable", "enable"] | None = None,
        show_log_forwarding: Literal["disable", "enable"] | None = None,
        show_sdwan_manager: Literal["disable", "enable"] | None = None,
        unreg_dev_opt: Literal["ignore", "add_no_service", "add_allow_service"] | None = None,
        webadmin_language: Literal["auto_detect", "english", "simplified_chinese", "traditional_chinese", "japanese", "korean", "spanish", "french"] | None = None,
        auth_addr: str | None = None,
        banner_message: str | None = None,
        preferred_fgfm_intf: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            access_banner: access-banner parameter
            admin_httpd_keep_alive_timeout: admin-httpd-keep-alive-timeout parameter
            admin_https_redirect: admin-https-redirect parameter
            admin_login_max: admin-login-max parameter
            admin_scp: admin-scp parameter
            admin_server_cert: admin_server_cert parameter
            auth_addr: auth-addr parameter
            auth_port: auth-port parameter
            banner_message: banner-message parameter
            fgt_gui_proxy: fgt-gui-proxy parameter
            ... (23 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/admin/setting"
        
        # Build data payload
        data = {}
        if access_banner is not None:
            data["access-banner"] = access_banner
        if admin_httpd_keep_alive_timeout is not None:
            data["admin-httpd-keep-alive-timeout"] = admin_httpd_keep_alive_timeout
        if admin_https_redirect is not None:
            data["admin-https-redirect"] = admin_https_redirect
        if admin_login_max is not None:
            data["admin-login-max"] = admin_login_max
        if admin_scp is not None:
            data["admin-scp"] = admin_scp
        if admin_server_cert is not None:
            data["admin_server_cert"] = admin_server_cert
        if auth_addr is not None:
            data["auth-addr"] = auth_addr
        if auth_port is not None:
            data["auth-port"] = auth_port
        if banner_message is not None:
            data["banner-message"] = banner_message
        if fgt_gui_proxy is not None:
            data["fgt-gui-proxy"] = fgt_gui_proxy
        if fgt_gui_proxy_port is not None:
            data["fgt-gui-proxy-port"] = fgt_gui_proxy_port
        if firmware_upgrade_check is not None:
            data["firmware-upgrade-check"] = firmware_upgrade_check
        if fsw_ignore_platform_check is not None:
            data["fsw-ignore-platform-check"] = fsw_ignore_platform_check
        if gui_theme is not None:
            data["gui-theme"] = gui_theme
        if http_port is not None:
            data["http_port"] = http_port
        if https_port is not None:
            data["https_port"] = https_port
        if idle_timeout is not None:
            data["idle_timeout"] = idle_timeout
        if idle_timeout_api is not None:
            data["idle_timeout_api"] = idle_timeout_api
        if idle_timeout_gui is not None:
            data["idle_timeout_gui"] = idle_timeout_gui
        if idle_timeout_sso is not None:
            data["idle_timeout_sso"] = idle_timeout_sso
        if object_threshold_limit is not None:
            data["object-threshold-limit"] = object_threshold_limit
        if object_threshold_limit_value is not None:
            data["object-threshold-limit-value"] = object_threshold_limit_value
        if objects_force_deletion is not None:
            data["objects-force-deletion"] = objects_force_deletion
        if preferred_fgfm_intf is not None:
            data["preferred-fgfm-intf"] = preferred_fgfm_intf
        if show_add_multiple is not None:
            data["show-add-multiple"] = show_add_multiple
        if show_checkbox_in_table is not None:
            data["show-checkbox-in-table"] = show_checkbox_in_table
        if show_device_import_export is not None:
            data["show-device-import-export"] = show_device_import_export
        if show_fct_manager is not None:
            data["show-fct-manager"] = show_fct_manager
        if show_hostname is not None:
            data["show-hostname"] = show_hostname
        if show_log_forwarding is not None:
            data["show-log-forwarding"] = show_log_forwarding
        if show_sdwan_manager is not None:
            data["show-sdwan-manager"] = show_sdwan_manager
        if unreg_dev_opt is not None:
            data["unreg_dev_opt"] = unreg_dev_opt
        if webadmin_language is not None:
            data["webadmin_language"] = webadmin_language
        
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

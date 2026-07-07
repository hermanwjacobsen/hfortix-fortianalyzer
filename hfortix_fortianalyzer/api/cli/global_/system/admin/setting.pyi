"""Type stubs for cli.global.system.admin.setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminSettingGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminSettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def access_banner(self) -> Literal["disable", "enable"]: ...
    @property
    def admin_httpd_keep_alive_timeout(self) -> int: ...
    @property
    def admin_https_redirect(self) -> Literal["disable", "enable"]: ...
    @property
    def admin_login_max(self) -> int: ...
    @property
    def admin_scp(self) -> Literal["disable", "enable"]: ...
    @property
    def admin_server_cert(self) -> str: ...
    @property
    def auth_addr(self) -> str: ...
    @property
    def auth_port(self) -> int: ...
    @property
    def banner_message(self) -> str: ...
    @property
    def fgt_gui_proxy(self) -> Literal["disable", "enable"]: ...
    @property
    def fgt_gui_proxy_port(self) -> int: ...
    @property
    def firmware_upgrade_check(self) -> Literal["disable", "enable"]: ...
    @property
    def fsw_ignore_platform_check(self) -> Literal["disable", "enable"]: ...
    @property
    def gui_theme(self) -> Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"]: ...
    @property
    def http_port(self) -> int: ...
    @property
    def https_port(self) -> int: ...
    @property
    def idle_timeout(self) -> int: ...
    @property
    def idle_timeout_api(self) -> int: ...
    @property
    def idle_timeout_gui(self) -> int: ...
    @property
    def idle_timeout_sso(self) -> int: ...
    @property
    def object_threshold_limit(self) -> Literal["disable", "enable"]: ...
    @property
    def object_threshold_limit_value(self) -> int: ...
    @property
    def objects_force_deletion(self) -> Literal["disable", "enable"]: ...
    @property
    def preferred_fgfm_intf(self) -> str: ...
    @property
    def show_add_multiple(self) -> Literal["disable", "enable"]: ...
    @property
    def show_checkbox_in_table(self) -> Literal["disable", "enable"]: ...
    @property
    def show_device_import_export(self) -> Literal["disable", "enable"]: ...
    @property
    def show_fct_manager(self) -> Literal["disable", "enable"]: ...
    @property
    def show_hostname(self) -> Literal["disable", "enable"]: ...
    @property
    def show_log_forwarding(self) -> Literal["disable", "enable"]: ...
    @property
    def show_sdwan_manager(self) -> Literal["disable", "enable"]: ...
    @property
    def unreg_dev_opt(self) -> Literal["ignore", "add_no_service", "add_allow_service"]: ...
    @property
    def webadmin_language(self) -> Literal["auto_detect", "english", "simplified_chinese", "traditional_chinese", "japanese", "korean", "spanish", "french"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAdminSettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminSettingGet endpoint with autocomplete support."""

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
    def access_banner(self) -> Literal["disable", "enable"] | None:
        """Field: access-banner"""
        ...

    @property
    def admin_httpd_keep_alive_timeout(self) -> int | None:
        """Field: admin-httpd-keep-alive-timeout"""
        ...

    @property
    def admin_https_redirect(self) -> Literal["disable", "enable"] | None:
        """Field: admin-https-redirect"""
        ...

    @property
    def admin_login_max(self) -> int | None:
        """Field: admin-login-max"""
        ...

    @property
    def admin_scp(self) -> Literal["disable", "enable"] | None:
        """Field: admin-scp"""
        ...

    @property
    def admin_server_cert(self) -> str | None:
        """Field: admin_server_cert"""
        ...

    @property
    def auth_addr(self) -> str | None:
        """Field: auth-addr"""
        ...

    @property
    def auth_port(self) -> int | None:
        """Field: auth-port"""
        ...

    @property
    def banner_message(self) -> str | None:
        """Field: banner-message"""
        ...

    @property
    def fgt_gui_proxy(self) -> Literal["disable", "enable"] | None:
        """Field: fgt-gui-proxy"""
        ...

    @property
    def fgt_gui_proxy_port(self) -> int | None:
        """Field: fgt-gui-proxy-port"""
        ...

    @property
    def firmware_upgrade_check(self) -> Literal["disable", "enable"] | None:
        """Field: firmware-upgrade-check"""
        ...

    @property
    def fsw_ignore_platform_check(self) -> Literal["disable", "enable"] | None:
        """Field: fsw-ignore-platform-check"""
        ...

    @property
    def gui_theme(self) -> Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None:
        """Field: gui-theme"""
        ...

    @property
    def http_port(self) -> int | None:
        """Field: http_port"""
        ...

    @property
    def https_port(self) -> int | None:
        """Field: https_port"""
        ...

    @property
    def idle_timeout(self) -> int | None:
        """Field: idle_timeout"""
        ...

    @property
    def idle_timeout_api(self) -> int | None:
        """Field: idle_timeout_api"""
        ...

    @property
    def idle_timeout_gui(self) -> int | None:
        """Field: idle_timeout_gui"""
        ...

    @property
    def idle_timeout_sso(self) -> int | None:
        """Field: idle_timeout_sso"""
        ...

    @property
    def object_threshold_limit(self) -> Literal["disable", "enable"] | None:
        """Field: object-threshold-limit"""
        ...

    @property
    def object_threshold_limit_value(self) -> int | None:
        """Field: object-threshold-limit-value"""
        ...

    @property
    def objects_force_deletion(self) -> Literal["disable", "enable"] | None:
        """Field: objects-force-deletion"""
        ...

    @property
    def preferred_fgfm_intf(self) -> str | None:
        """Field: preferred-fgfm-intf"""
        ...

    @property
    def show_add_multiple(self) -> Literal["disable", "enable"] | None:
        """Field: show-add-multiple"""
        ...

    @property
    def show_checkbox_in_table(self) -> Literal["disable", "enable"] | None:
        """Field: show-checkbox-in-table"""
        ...

    @property
    def show_device_import_export(self) -> Literal["disable", "enable"] | None:
        """Field: show-device-import-export"""
        ...

    @property
    def show_fct_manager(self) -> Literal["disable", "enable"] | None:
        """Field: show-fct-manager"""
        ...

    @property
    def show_hostname(self) -> Literal["disable", "enable"] | None:
        """Field: show-hostname"""
        ...

    @property
    def show_log_forwarding(self) -> Literal["disable", "enable"] | None:
        """Field: show-log-forwarding"""
        ...

    @property
    def show_sdwan_manager(self) -> Literal["disable", "enable"] | None:
        """Field: show-sdwan-manager"""
        ...

    @property
    def unreg_dev_opt(self) -> Literal["ignore", "add_no_service", "add_allow_service"] | None:
        """Field: unreg_dev_opt"""
        ...

    @property
    def webadmin_language(self) -> Literal["auto_detect", "english", "simplified_chinese", "traditional_chinese", "japanese", "korean", "spanish", "french"] | None:
        """Field: webadmin_language"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminSettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminSetting:
    """FortiAnalyzer endpoint: cli.global.system.admin.setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemAdminSettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        access_banner: Literal["disable", "enable"] | None = None,
        admin_httpd_keep_alive_timeout: int | None = None,
        admin_https_redirect: Literal["disable", "enable"] | None = None,
        admin_login_max: int | None = None,
        admin_scp: Literal["disable", "enable"] | None = None,
        admin_server_cert: str | None = None,
        auth_addr: str | None = None,
        auth_port: int | None = None,
        banner_message: str | None = None,
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
        preferred_fgfm_intf: str | None = None,
        show_add_multiple: Literal["disable", "enable"] | None = None,
        show_checkbox_in_table: Literal["disable", "enable"] | None = None,
        show_device_import_export: Literal["disable", "enable"] | None = None,
        show_fct_manager: Literal["disable", "enable"] | None = None,
        show_hostname: Literal["disable", "enable"] | None = None,
        show_log_forwarding: Literal["disable", "enable"] | None = None,
        show_sdwan_manager: Literal["disable", "enable"] | None = None,
        unreg_dev_opt: Literal["ignore", "add_no_service", "add_allow_service"] | None = None,
        webadmin_language: Literal["auto_detect", "english", "simplified_chinese", "traditional_chinese", "japanese", "korean", "spanish", "french"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        access_banner: Literal["disable", "enable"] | None = None,
        admin_httpd_keep_alive_timeout: int | None = None,
        admin_https_redirect: Literal["disable", "enable"] | None = None,
        admin_login_max: int | None = None,
        admin_scp: Literal["disable", "enable"] | None = None,
        admin_server_cert: str | None = None,
        auth_addr: str | None = None,
        auth_port: int | None = None,
        banner_message: str | None = None,
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
        preferred_fgfm_intf: str | None = None,
        show_add_multiple: Literal["disable", "enable"] | None = None,
        show_checkbox_in_table: Literal["disable", "enable"] | None = None,
        show_device_import_export: Literal["disable", "enable"] | None = None,
        show_fct_manager: Literal["disable", "enable"] | None = None,
        show_hostname: Literal["disable", "enable"] | None = None,
        show_log_forwarding: Literal["disable", "enable"] | None = None,
        show_sdwan_manager: Literal["disable", "enable"] | None = None,
        unreg_dev_opt: Literal["ignore", "add_no_service", "add_allow_service"] | None = None,
        webadmin_language: Literal["auto_detect", "english", "simplified_chinese", "traditional_chinese", "japanese", "korean", "spanish", "french"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemAdminSetting", "CliGlobalSystemAdminSettingGetResponse"]
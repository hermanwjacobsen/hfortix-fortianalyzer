"""Type stubs for cli.global.system.admin.profile"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminProfileGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminProfileGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def adom_admin(self) -> Literal["disable", "enable"]: ...
    @property
    def adom_lock(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def adom_switch(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def allow_to_install(self) -> Literal["disable", "enable"]: ...
    @property
    def change_password(self) -> Literal["disable", "enable"]: ...
    @property
    def datamask(self) -> Literal["disable", "enable"]: ...
    @property
    def datamask_custom_fields(self) -> list[DatamaskCustomFieldsItem]: ...
    @property
    def datamask_custom_priority(self) -> Literal["disable", "enable"]: ...
    @property
    def datamask_fields(self) -> list[Any]: ...
    @property
    def datamask_key(self) -> list[Any]: ...
    @property
    def datamask_unmasked_time(self) -> int: ...
    @property
    def description(self) -> str: ...
    @property
    def device_ap(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def device_fortiextender(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def device_fortiswitch(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def device_manager(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def device_op(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def device_policy_package_lock(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def device_wan_link_load_balance(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def event_management(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def execute_playbook(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def fabric_viewer(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def fgt_gui_proxy(self) -> Literal["disable", "enable"]: ...
    @property
    def ips_lock(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def ipv6_trusthost1(self) -> str: ...
    @property
    def ipv6_trusthost10(self) -> str: ...
    @property
    def ipv6_trusthost2(self) -> str: ...
    @property
    def ipv6_trusthost3(self) -> str: ...
    @property
    def ipv6_trusthost4(self) -> str: ...
    @property
    def ipv6_trusthost5(self) -> str: ...
    @property
    def ipv6_trusthost6(self) -> str: ...
    @property
    def ipv6_trusthost7(self) -> str: ...
    @property
    def ipv6_trusthost8(self) -> str: ...
    @property
    def ipv6_trusthost9(self) -> str: ...
    @property
    def log_viewer(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def profileid(self) -> str: ...
    @property
    def report_viewer(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def rpc_permit(self) -> Literal["read-write", "none", "read"]: ...
    @property
    def run_report(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def scope(self) -> Literal["global", "adom"]: ...
    @property
    def script_access(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def script_run(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def super_user_profile(self) -> Literal["disable", "enable"]: ...
    @property
    def system_setting(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def triage_events(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def trusthost1(self) -> list[Any]: ...
    @property
    def trusthost10(self) -> list[Any]: ...
    @property
    def trusthost2(self) -> list[Any]: ...
    @property
    def trusthost3(self) -> list[Any]: ...
    @property
    def trusthost4(self) -> list[Any]: ...
    @property
    def trusthost5(self) -> list[Any]: ...
    @property
    def trusthost6(self) -> list[Any]: ...
    @property
    def trusthost7(self) -> list[Any]: ...
    @property
    def trusthost8(self) -> list[Any]: ...
    @property
    def trusthost9(self) -> list[Any]: ...
    @property
    def update_incidents(self) -> Literal["none", "read", "read-write"]: ...
    @property
    def write_passwd_access(self) -> Literal["all", "specify-by-user", "specify-by-profile"]: ...
    @property
    def write_passwd_profiles(self) -> list[WritePasswdProfilesItem]: ...
    @property
    def write_passwd_user_list(self) -> list[WritePasswdUserListItem]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class DatamaskCustomFieldsItem:
    """Nested item type for datamask-custom-fields array."""

    @property
    def field_category(self) -> list[Any]: ...
    @property
    def field_name(self) -> str: ...
    @property
    def field_status(self) -> Literal["disable", "enable"]: ...
    @property
    def field_type(self) -> Literal["string", "ip", "mac", "email", "unknown"]: ...

class WritePasswdProfilesItem:
    """Nested item type for write-passwd-profiles array."""

    @property
    def profileid(self) -> str: ...

class WritePasswdUserListItem:
    """Nested item type for write-passwd-user-list array."""

    @property
    def userid(self) -> str: ...


class CliGlobalSystemAdminProfileGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminProfileGet endpoint with autocomplete support."""

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
    def adom_admin(self) -> Literal["disable", "enable"] | None:
        """Field: adom-admin"""
        ...

    @property
    def adom_lock(self) -> Literal["none", "read", "read-write"] | None:
        """Field: adom-lock"""
        ...

    @property
    def adom_switch(self) -> Literal["none", "read", "read-write"] | None:
        """Field: adom-switch"""
        ...

    @property
    def allow_to_install(self) -> Literal["disable", "enable"] | None:
        """Field: allow-to-install"""
        ...

    @property
    def change_password(self) -> Literal["disable", "enable"] | None:
        """Field: change-password"""
        ...

    @property
    def datamask(self) -> Literal["disable", "enable"] | None:
        """Field: datamask"""
        ...

    @property
    def datamask_custom_fields(self) -> list[DatamaskCustomFieldsItem]:
        """Field: datamask-custom-fields"""
        ...

    @property
    def datamask_custom_priority(self) -> Literal["disable", "enable"] | None:
        """Field: datamask-custom-priority"""
        ...

    @property
    def datamask_fields(self) -> list[Any] | None:
        """Field: datamask-fields"""
        ...

    @property
    def datamask_key(self) -> list[Any] | None:
        """Field: datamask-key"""
        ...

    @property
    def datamask_unmasked_time(self) -> int | None:
        """Field: datamask-unmasked-time"""
        ...

    @property
    def description(self) -> str | None:
        """Field: description"""
        ...

    @property
    def device_ap(self) -> Literal["none", "read", "read-write"] | None:
        """Field: device-ap"""
        ...

    @property
    def device_fortiextender(self) -> Literal["none", "read", "read-write"] | None:
        """Field: device-fortiextender"""
        ...

    @property
    def device_fortiswitch(self) -> Literal["none", "read", "read-write"] | None:
        """Field: device-fortiswitch"""
        ...

    @property
    def device_manager(self) -> Literal["none", "read", "read-write"] | None:
        """Field: device-manager"""
        ...

    @property
    def device_op(self) -> Literal["none", "read", "read-write"] | None:
        """Field: device-op"""
        ...

    @property
    def device_policy_package_lock(self) -> Literal["none", "read", "read-write"] | None:
        """Field: device-policy-package-lock"""
        ...

    @property
    def device_wan_link_load_balance(self) -> Literal["none", "read", "read-write"] | None:
        """Field: device-wan-link-load-balance"""
        ...

    @property
    def event_management(self) -> Literal["none", "read", "read-write"] | None:
        """Field: event-management"""
        ...

    @property
    def execute_playbook(self) -> Literal["none", "read", "read-write"] | None:
        """Field: execute-playbook"""
        ...

    @property
    def fabric_viewer(self) -> Literal["none", "read", "read-write"] | None:
        """Field: fabric-viewer"""
        ...

    @property
    def fgt_gui_proxy(self) -> Literal["disable", "enable"] | None:
        """Field: fgt-gui-proxy"""
        ...

    @property
    def ips_lock(self) -> Literal["none", "read", "read-write"] | None:
        """Field: ips-lock"""
        ...

    @property
    def ipv6_trusthost1(self) -> str | None:
        """Field: ipv6_trusthost1"""
        ...

    @property
    def ipv6_trusthost10(self) -> str | None:
        """Field: ipv6_trusthost10"""
        ...

    @property
    def ipv6_trusthost2(self) -> str | None:
        """Field: ipv6_trusthost2"""
        ...

    @property
    def ipv6_trusthost3(self) -> str | None:
        """Field: ipv6_trusthost3"""
        ...

    @property
    def ipv6_trusthost4(self) -> str | None:
        """Field: ipv6_trusthost4"""
        ...

    @property
    def ipv6_trusthost5(self) -> str | None:
        """Field: ipv6_trusthost5"""
        ...

    @property
    def ipv6_trusthost6(self) -> str | None:
        """Field: ipv6_trusthost6"""
        ...

    @property
    def ipv6_trusthost7(self) -> str | None:
        """Field: ipv6_trusthost7"""
        ...

    @property
    def ipv6_trusthost8(self) -> str | None:
        """Field: ipv6_trusthost8"""
        ...

    @property
    def ipv6_trusthost9(self) -> str | None:
        """Field: ipv6_trusthost9"""
        ...

    @property
    def log_viewer(self) -> Literal["none", "read", "read-write"] | None:
        """Field: log-viewer"""
        ...

    @property
    def profileid(self) -> str | None:
        """Field: profileid"""
        ...

    @property
    def report_viewer(self) -> Literal["none", "read", "read-write"] | None:
        """Field: report-viewer"""
        ...

    @property
    def rpc_permit(self) -> Literal["read-write", "none", "read"] | None:
        """Field: rpc-permit"""
        ...

    @property
    def run_report(self) -> Literal["none", "read", "read-write"] | None:
        """Field: run-report"""
        ...

    @property
    def scope(self) -> Literal["global", "adom"] | None:
        """Field: scope"""
        ...

    @property
    def script_access(self) -> Literal["none", "read", "read-write"] | None:
        """Field: script-access"""
        ...

    @property
    def script_run(self) -> Literal["none", "read", "read-write"] | None:
        """Field: script-run"""
        ...

    @property
    def super_user_profile(self) -> Literal["disable", "enable"] | None:
        """Field: super-user-profile"""
        ...

    @property
    def system_setting(self) -> Literal["none", "read", "read-write"] | None:
        """Field: system-setting"""
        ...

    @property
    def triage_events(self) -> Literal["none", "read", "read-write"] | None:
        """Field: triage-events"""
        ...

    @property
    def trusthost1(self) -> list[Any] | None:
        """Field: trusthost1"""
        ...

    @property
    def trusthost10(self) -> list[Any] | None:
        """Field: trusthost10"""
        ...

    @property
    def trusthost2(self) -> list[Any] | None:
        """Field: trusthost2"""
        ...

    @property
    def trusthost3(self) -> list[Any] | None:
        """Field: trusthost3"""
        ...

    @property
    def trusthost4(self) -> list[Any] | None:
        """Field: trusthost4"""
        ...

    @property
    def trusthost5(self) -> list[Any] | None:
        """Field: trusthost5"""
        ...

    @property
    def trusthost6(self) -> list[Any] | None:
        """Field: trusthost6"""
        ...

    @property
    def trusthost7(self) -> list[Any] | None:
        """Field: trusthost7"""
        ...

    @property
    def trusthost8(self) -> list[Any] | None:
        """Field: trusthost8"""
        ...

    @property
    def trusthost9(self) -> list[Any] | None:
        """Field: trusthost9"""
        ...

    @property
    def update_incidents(self) -> Literal["none", "read", "read-write"] | None:
        """Field: update-incidents"""
        ...

    @property
    def write_passwd_access(self) -> Literal["all", "specify-by-user", "specify-by-profile"] | None:
        """Field: write-passwd-access"""
        ...

    @property
    def write_passwd_profiles(self) -> list[WritePasswdProfilesItem]:
        """Field: write-passwd-profiles"""
        ...

    @property
    def write_passwd_user_list(self) -> list[WritePasswdUserListItem]:
        """Field: write-passwd-user-list"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminProfileGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminProfile:
    """FortiAnalyzer endpoint: cli.global.system.admin.profile"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        profile: int | str | None = None,
        fields: list[Literal["adom-admin", "adom-lock", "adom-switch", "allow-to-install", "change-password", "datamask", "datamask-custom-priority", "datamask-fields", "datamask-key", "datamask-unmasked-time", "description", "device-ap", "device-fortiextender", "device-fortiswitch", "device-manager", "device-op", "device-policy-package-lock", "device-wan-link-load-balance", "event-management", "execute-playbook", "fabric-viewer", "fgt-gui-proxy", "ips-lock", "ipv6_trusthost1", "ipv6_trusthost10", "ipv6_trusthost2", "ipv6_trusthost3", "ipv6_trusthost4", "ipv6_trusthost5", "ipv6_trusthost6", "ipv6_trusthost7", "ipv6_trusthost8", "ipv6_trusthost9", "log-viewer", "profileid", "report-viewer", "rpc-permit", "run-report", "scope", "script-access", "script-run", "super-user-profile", "system-setting", "triage-events", "trusthost1", "trusthost10", "trusthost2", "trusthost3", "trusthost4", "trusthost5", "trusthost6", "trusthost7", "trusthost8", "trusthost9", "update-incidents", "write-passwd-access"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminProfileGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        profile: int | str | None = None,
        adom_admin: Literal["disable", "enable"] | None = None,
        adom_lock: Literal["none", "read", "read-write"] | None = None,
        adom_switch: Literal["none", "read", "read-write"] | None = None,
        allow_to_install: Literal["disable", "enable"] | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        datamask: Literal["disable", "enable"] | None = None,
        datamask_custom_fields: list[dict[str, Any]] | None = None,
        datamask_custom_priority: Literal["disable", "enable"] | None = None,
        datamask_fields: list[Any] | None = None,
        datamask_key: list[Any] | None = None,
        datamask_unmasked_time: int | None = None,
        description: str | None = None,
        device_ap: Literal["none", "read", "read-write"] | None = None,
        device_fortiextender: Literal["none", "read", "read-write"] | None = None,
        device_fortiswitch: Literal["none", "read", "read-write"] | None = None,
        device_manager: Literal["none", "read", "read-write"] | None = None,
        device_op: Literal["none", "read", "read-write"] | None = None,
        device_policy_package_lock: Literal["none", "read", "read-write"] | None = None,
        device_wan_link_load_balance: Literal["none", "read", "read-write"] | None = None,
        event_management: Literal["none", "read", "read-write"] | None = None,
        execute_playbook: Literal["none", "read", "read-write"] | None = None,
        fabric_viewer: Literal["none", "read", "read-write"] | None = None,
        fgt_gui_proxy: Literal["disable", "enable"] | None = None,
        ips_lock: Literal["none", "read", "read-write"] | None = None,
        ipv6_trusthost1: str | None = None,
        ipv6_trusthost10: str | None = None,
        ipv6_trusthost2: str | None = None,
        ipv6_trusthost3: str | None = None,
        ipv6_trusthost4: str | None = None,
        ipv6_trusthost5: str | None = None,
        ipv6_trusthost6: str | None = None,
        ipv6_trusthost7: str | None = None,
        ipv6_trusthost8: str | None = None,
        ipv6_trusthost9: str | None = None,
        log_viewer: Literal["none", "read", "read-write"] | None = None,
        profileid: str | None = None,
        report_viewer: Literal["none", "read", "read-write"] | None = None,
        rpc_permit: Literal["read-write", "none", "read"] | None = None,
        run_report: Literal["none", "read", "read-write"] | None = None,
        scope: Literal["global", "adom"] | None = None,
        script_access: Literal["none", "read", "read-write"] | None = None,
        script_run: Literal["none", "read", "read-write"] | None = None,
        super_user_profile: Literal["disable", "enable"] | None = None,
        system_setting: Literal["none", "read", "read-write"] | None = None,
        triage_events: Literal["none", "read", "read-write"] | None = None,
        trusthost1: list[Any] | None = None,
        trusthost10: list[Any] | None = None,
        trusthost2: list[Any] | None = None,
        trusthost3: list[Any] | None = None,
        trusthost4: list[Any] | None = None,
        trusthost5: list[Any] | None = None,
        trusthost6: list[Any] | None = None,
        trusthost7: list[Any] | None = None,
        trusthost8: list[Any] | None = None,
        trusthost9: list[Any] | None = None,
        update_incidents: Literal["none", "read", "read-write"] | None = None,
        write_passwd_access: Literal["all", "specify-by-user", "specify-by-profile"] | None = None,
        write_passwd_profiles: list[dict[str, Any]] | None = None,
        write_passwd_user_list: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        profile: int | str | None = None,
        adom_admin: Literal["disable", "enable"] | None = None,
        adom_lock: Literal["none", "read", "read-write"] | None = None,
        adom_switch: Literal["none", "read", "read-write"] | None = None,
        allow_to_install: Literal["disable", "enable"] | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        datamask: Literal["disable", "enable"] | None = None,
        datamask_custom_fields: list[dict[str, Any]] | None = None,
        datamask_custom_priority: Literal["disable", "enable"] | None = None,
        datamask_fields: list[Any] | None = None,
        datamask_key: list[Any] | None = None,
        datamask_unmasked_time: int | None = None,
        description: str | None = None,
        device_ap: Literal["none", "read", "read-write"] | None = None,
        device_fortiextender: Literal["none", "read", "read-write"] | None = None,
        device_fortiswitch: Literal["none", "read", "read-write"] | None = None,
        device_manager: Literal["none", "read", "read-write"] | None = None,
        device_op: Literal["none", "read", "read-write"] | None = None,
        device_policy_package_lock: Literal["none", "read", "read-write"] | None = None,
        device_wan_link_load_balance: Literal["none", "read", "read-write"] | None = None,
        event_management: Literal["none", "read", "read-write"] | None = None,
        execute_playbook: Literal["none", "read", "read-write"] | None = None,
        fabric_viewer: Literal["none", "read", "read-write"] | None = None,
        fgt_gui_proxy: Literal["disable", "enable"] | None = None,
        ips_lock: Literal["none", "read", "read-write"] | None = None,
        ipv6_trusthost1: str | None = None,
        ipv6_trusthost10: str | None = None,
        ipv6_trusthost2: str | None = None,
        ipv6_trusthost3: str | None = None,
        ipv6_trusthost4: str | None = None,
        ipv6_trusthost5: str | None = None,
        ipv6_trusthost6: str | None = None,
        ipv6_trusthost7: str | None = None,
        ipv6_trusthost8: str | None = None,
        ipv6_trusthost9: str | None = None,
        log_viewer: Literal["none", "read", "read-write"] | None = None,
        profileid: str | None = None,
        report_viewer: Literal["none", "read", "read-write"] | None = None,
        rpc_permit: Literal["read-write", "none", "read"] | None = None,
        run_report: Literal["none", "read", "read-write"] | None = None,
        scope: Literal["global", "adom"] | None = None,
        script_access: Literal["none", "read", "read-write"] | None = None,
        script_run: Literal["none", "read", "read-write"] | None = None,
        super_user_profile: Literal["disable", "enable"] | None = None,
        system_setting: Literal["none", "read", "read-write"] | None = None,
        triage_events: Literal["none", "read", "read-write"] | None = None,
        trusthost1: list[Any] | None = None,
        trusthost10: list[Any] | None = None,
        trusthost2: list[Any] | None = None,
        trusthost3: list[Any] | None = None,
        trusthost4: list[Any] | None = None,
        trusthost5: list[Any] | None = None,
        trusthost6: list[Any] | None = None,
        trusthost7: list[Any] | None = None,
        trusthost8: list[Any] | None = None,
        trusthost9: list[Any] | None = None,
        update_incidents: Literal["none", "read", "read-write"] | None = None,
        write_passwd_access: Literal["all", "specify-by-user", "specify-by-profile"] | None = None,
        write_passwd_profiles: list[dict[str, Any]] | None = None,
        write_passwd_user_list: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        profile: int | str | None = None,
        adom_admin: Literal["disable", "enable"] | None = None,
        adom_lock: Literal["none", "read", "read-write"] | None = None,
        adom_switch: Literal["none", "read", "read-write"] | None = None,
        allow_to_install: Literal["disable", "enable"] | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        datamask: Literal["disable", "enable"] | None = None,
        datamask_custom_fields: list[dict[str, Any]] | None = None,
        datamask_custom_priority: Literal["disable", "enable"] | None = None,
        datamask_fields: list[Any] | None = None,
        datamask_key: list[Any] | None = None,
        datamask_unmasked_time: int | None = None,
        description: str | None = None,
        device_ap: Literal["none", "read", "read-write"] | None = None,
        device_fortiextender: Literal["none", "read", "read-write"] | None = None,
        device_fortiswitch: Literal["none", "read", "read-write"] | None = None,
        device_manager: Literal["none", "read", "read-write"] | None = None,
        device_op: Literal["none", "read", "read-write"] | None = None,
        device_policy_package_lock: Literal["none", "read", "read-write"] | None = None,
        device_wan_link_load_balance: Literal["none", "read", "read-write"] | None = None,
        event_management: Literal["none", "read", "read-write"] | None = None,
        execute_playbook: Literal["none", "read", "read-write"] | None = None,
        fabric_viewer: Literal["none", "read", "read-write"] | None = None,
        fgt_gui_proxy: Literal["disable", "enable"] | None = None,
        ips_lock: Literal["none", "read", "read-write"] | None = None,
        ipv6_trusthost1: str | None = None,
        ipv6_trusthost10: str | None = None,
        ipv6_trusthost2: str | None = None,
        ipv6_trusthost3: str | None = None,
        ipv6_trusthost4: str | None = None,
        ipv6_trusthost5: str | None = None,
        ipv6_trusthost6: str | None = None,
        ipv6_trusthost7: str | None = None,
        ipv6_trusthost8: str | None = None,
        ipv6_trusthost9: str | None = None,
        log_viewer: Literal["none", "read", "read-write"] | None = None,
        profileid: str | None = None,
        report_viewer: Literal["none", "read", "read-write"] | None = None,
        rpc_permit: Literal["read-write", "none", "read"] | None = None,
        run_report: Literal["none", "read", "read-write"] | None = None,
        scope: Literal["global", "adom"] | None = None,
        script_access: Literal["none", "read", "read-write"] | None = None,
        script_run: Literal["none", "read", "read-write"] | None = None,
        super_user_profile: Literal["disable", "enable"] | None = None,
        system_setting: Literal["none", "read", "read-write"] | None = None,
        triage_events: Literal["none", "read", "read-write"] | None = None,
        trusthost1: list[Any] | None = None,
        trusthost10: list[Any] | None = None,
        trusthost2: list[Any] | None = None,
        trusthost3: list[Any] | None = None,
        trusthost4: list[Any] | None = None,
        trusthost5: list[Any] | None = None,
        trusthost6: list[Any] | None = None,
        trusthost7: list[Any] | None = None,
        trusthost8: list[Any] | None = None,
        trusthost9: list[Any] | None = None,
        update_incidents: Literal["none", "read", "read-write"] | None = None,
        write_passwd_access: Literal["all", "specify-by-user", "specify-by-profile"] | None = None,
        write_passwd_profiles: list[dict[str, Any]] | None = None,
        write_passwd_user_list: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        profile: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminProfile", "CliGlobalSystemAdminProfileGetResponse"]
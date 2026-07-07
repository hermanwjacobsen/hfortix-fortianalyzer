"""
FortiAnalyzer API endpoint: cli.global.system.admin.profile

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminProfile:
    """
    FortiAnalyzer endpoint: cli.global.system.admin.profile
    
    
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
        profile: int | str | None = None,
        fields: list[Literal["adom-admin", "adom-lock", "adom-switch", "allow-to-install", "change-password", "datamask", "datamask-custom-priority", "datamask-fields", "datamask-key", "datamask-unmasked-time", "description", "device-ap", "device-fortiextender", "device-fortiswitch", "device-manager", "device-op", "device-policy-package-lock", "device-wan-link-load-balance", "event-management", "execute-playbook", "fabric-viewer", "fgt-gui-proxy", "ips-lock", "ipv6_trusthost1", "ipv6_trusthost10", "ipv6_trusthost2", "ipv6_trusthost3", "ipv6_trusthost4", "ipv6_trusthost5", "ipv6_trusthost6", "ipv6_trusthost7", "ipv6_trusthost8", "ipv6_trusthost9", "log-viewer", "profileid", "report-viewer", "rpc-permit", "run-report", "scope", "script-access", "script-run", "super-user-profile", "system-setting", "triage-events", "trusthost1", "trusthost10", "trusthost2", "trusthost3", "trusthost4", "trusthost5", "trusthost6", "trusthost7", "trusthost8", "trusthost9", "update-incidents", "write-passwd-access"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            profile: profile parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if profile is not None:
            url = "/cli/global/system/admin/profile/{profile}"
            url = url.replace("{profile}", str(profile))
        else:
            url = "/cli/global/system/admin/profile"
        
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
        profile: int | str | None = None,
        adom_admin: Literal["disable", "enable"] | None = None,
        adom_lock: Literal["none", "read", "read-write"] | None = None,
        adom_switch: Literal["none", "read", "read-write"] | None = None,
        allow_to_install: Literal["disable", "enable"] | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        datamask: Literal["disable", "enable"] | None = None,
        datamask_custom_priority: Literal["disable", "enable"] | None = None,
        datamask_unmasked_time: int | None = None,
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
        report_viewer: Literal["none", "read", "read-write"] | None = None,
        rpc_permit: Literal["read-write", "none", "read"] | None = None,
        run_report: Literal["none", "read", "read-write"] | None = None,
        scope: Literal["global", "adom"] | None = None,
        script_access: Literal["none", "read", "read-write"] | None = None,
        script_run: Literal["none", "read", "read-write"] | None = None,
        super_user_profile: Literal["disable", "enable"] | None = None,
        system_setting: Literal["none", "read", "read-write"] | None = None,
        triage_events: Literal["none", "read", "read-write"] | None = None,
        update_incidents: Literal["none", "read", "read-write"] | None = None,
        write_passwd_access: Literal["all", "specify-by-user", "specify-by-profile"] | None = None,
        datamask_custom_fields: list[Any] | None = None,
        datamask_fields: list[Any] | None = None,
        datamask_key: list[Any] | None = None,
        description: str | None = None,
        profileid: str | None = None,
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
        write_passwd_profiles: list[Any] | None = None,
        write_passwd_user_list: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            profile: profile parameter
            adom_admin: adom-admin parameter
            adom_lock: adom-lock parameter
            adom_switch: adom-switch parameter
            allow_to_install: allow-to-install parameter
            change_password: change-password parameter
            datamask: datamask parameter
            datamask_custom_fields: datamask-custom-fields parameter
            datamask_custom_priority: datamask-custom-priority parameter
            datamask_fields: datamask-fields parameter
            datamask_key: datamask-key parameter
            ... (49 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/admin/profile"
        
        # Build data payload
        data = {}
        if adom_admin is not None:
            data["adom-admin"] = adom_admin
        if adom_lock is not None:
            data["adom-lock"] = adom_lock
        if adom_switch is not None:
            data["adom-switch"] = adom_switch
        if allow_to_install is not None:
            data["allow-to-install"] = allow_to_install
        if change_password is not None:
            data["change-password"] = change_password
        if datamask is not None:
            data["datamask"] = datamask
        if datamask_custom_fields is not None:
            data["datamask-custom-fields"] = datamask_custom_fields
        if datamask_custom_priority is not None:
            data["datamask-custom-priority"] = datamask_custom_priority
        if datamask_fields is not None:
            data["datamask-fields"] = datamask_fields
        if datamask_key is not None:
            data["datamask-key"] = datamask_key
        if datamask_unmasked_time is not None:
            data["datamask-unmasked-time"] = datamask_unmasked_time
        if description is not None:
            data["description"] = description
        if device_ap is not None:
            data["device-ap"] = device_ap
        if device_fortiextender is not None:
            data["device-fortiextender"] = device_fortiextender
        if device_fortiswitch is not None:
            data["device-fortiswitch"] = device_fortiswitch
        if device_manager is not None:
            data["device-manager"] = device_manager
        if device_op is not None:
            data["device-op"] = device_op
        if device_policy_package_lock is not None:
            data["device-policy-package-lock"] = device_policy_package_lock
        if device_wan_link_load_balance is not None:
            data["device-wan-link-load-balance"] = device_wan_link_load_balance
        if event_management is not None:
            data["event-management"] = event_management
        if execute_playbook is not None:
            data["execute-playbook"] = execute_playbook
        if fabric_viewer is not None:
            data["fabric-viewer"] = fabric_viewer
        if fgt_gui_proxy is not None:
            data["fgt-gui-proxy"] = fgt_gui_proxy
        if ips_lock is not None:
            data["ips-lock"] = ips_lock
        if ipv6_trusthost1 is not None:
            data["ipv6_trusthost1"] = ipv6_trusthost1
        if ipv6_trusthost10 is not None:
            data["ipv6_trusthost10"] = ipv6_trusthost10
        if ipv6_trusthost2 is not None:
            data["ipv6_trusthost2"] = ipv6_trusthost2
        if ipv6_trusthost3 is not None:
            data["ipv6_trusthost3"] = ipv6_trusthost3
        if ipv6_trusthost4 is not None:
            data["ipv6_trusthost4"] = ipv6_trusthost4
        if ipv6_trusthost5 is not None:
            data["ipv6_trusthost5"] = ipv6_trusthost5
        if ipv6_trusthost6 is not None:
            data["ipv6_trusthost6"] = ipv6_trusthost6
        if ipv6_trusthost7 is not None:
            data["ipv6_trusthost7"] = ipv6_trusthost7
        if ipv6_trusthost8 is not None:
            data["ipv6_trusthost8"] = ipv6_trusthost8
        if ipv6_trusthost9 is not None:
            data["ipv6_trusthost9"] = ipv6_trusthost9
        if log_viewer is not None:
            data["log-viewer"] = log_viewer
        if profileid is not None:
            data["profileid"] = profileid
        if report_viewer is not None:
            data["report-viewer"] = report_viewer
        if rpc_permit is not None:
            data["rpc-permit"] = rpc_permit
        if run_report is not None:
            data["run-report"] = run_report
        if scope is not None:
            data["scope"] = scope
        if script_access is not None:
            data["script-access"] = script_access
        if script_run is not None:
            data["script-run"] = script_run
        if super_user_profile is not None:
            data["super-user-profile"] = super_user_profile
        if system_setting is not None:
            data["system-setting"] = system_setting
        if triage_events is not None:
            data["triage-events"] = triage_events
        if trusthost1 is not None:
            data["trusthost1"] = trusthost1
        if trusthost10 is not None:
            data["trusthost10"] = trusthost10
        if trusthost2 is not None:
            data["trusthost2"] = trusthost2
        if trusthost3 is not None:
            data["trusthost3"] = trusthost3
        if trusthost4 is not None:
            data["trusthost4"] = trusthost4
        if trusthost5 is not None:
            data["trusthost5"] = trusthost5
        if trusthost6 is not None:
            data["trusthost6"] = trusthost6
        if trusthost7 is not None:
            data["trusthost7"] = trusthost7
        if trusthost8 is not None:
            data["trusthost8"] = trusthost8
        if trusthost9 is not None:
            data["trusthost9"] = trusthost9
        if update_incidents is not None:
            data["update-incidents"] = update_incidents
        if write_passwd_access is not None:
            data["write-passwd-access"] = write_passwd_access
        if write_passwd_profiles is not None:
            data["write-passwd-profiles"] = write_passwd_profiles
        if write_passwd_user_list is not None:
            data["write-passwd-user-list"] = write_passwd_user_list
        
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
        profile: int | str | None = None,
        adom_admin: Literal["disable", "enable"] | None = None,
        adom_lock: Literal["none", "read", "read-write"] | None = None,
        adom_switch: Literal["none", "read", "read-write"] | None = None,
        allow_to_install: Literal["disable", "enable"] | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        datamask: Literal["disable", "enable"] | None = None,
        datamask_custom_priority: Literal["disable", "enable"] | None = None,
        datamask_unmasked_time: int | None = None,
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
        report_viewer: Literal["none", "read", "read-write"] | None = None,
        rpc_permit: Literal["read-write", "none", "read"] | None = None,
        run_report: Literal["none", "read", "read-write"] | None = None,
        scope: Literal["global", "adom"] | None = None,
        script_access: Literal["none", "read", "read-write"] | None = None,
        script_run: Literal["none", "read", "read-write"] | None = None,
        super_user_profile: Literal["disable", "enable"] | None = None,
        system_setting: Literal["none", "read", "read-write"] | None = None,
        triage_events: Literal["none", "read", "read-write"] | None = None,
        update_incidents: Literal["none", "read", "read-write"] | None = None,
        write_passwd_access: Literal["all", "specify-by-user", "specify-by-profile"] | None = None,
        datamask_custom_fields: list[Any] | None = None,
        datamask_fields: list[Any] | None = None,
        datamask_key: list[Any] | None = None,
        description: str | None = None,
        profileid: str | None = None,
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
        write_passwd_profiles: list[Any] | None = None,
        write_passwd_user_list: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            profile: profile parameter
            adom_admin: adom-admin parameter
            adom_lock: adom-lock parameter
            adom_switch: adom-switch parameter
            allow_to_install: allow-to-install parameter
            change_password: change-password parameter
            datamask: datamask parameter
            datamask_custom_fields: datamask-custom-fields parameter
            datamask_custom_priority: datamask-custom-priority parameter
            datamask_fields: datamask-fields parameter
            datamask_key: datamask-key parameter
            ... (49 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if profile is not None:
            url = "/cli/global/system/admin/profile/{profile}"
            url = url.replace("{profile}", str(profile))
        else:
            url = "/cli/global/system/admin/profile"
        
        # Build data payload
        data = {}
        if adom_admin is not None:
            data["adom-admin"] = adom_admin
        if adom_lock is not None:
            data["adom-lock"] = adom_lock
        if adom_switch is not None:
            data["adom-switch"] = adom_switch
        if allow_to_install is not None:
            data["allow-to-install"] = allow_to_install
        if change_password is not None:
            data["change-password"] = change_password
        if datamask is not None:
            data["datamask"] = datamask
        if datamask_custom_fields is not None:
            data["datamask-custom-fields"] = datamask_custom_fields
        if datamask_custom_priority is not None:
            data["datamask-custom-priority"] = datamask_custom_priority
        if datamask_fields is not None:
            data["datamask-fields"] = datamask_fields
        if datamask_key is not None:
            data["datamask-key"] = datamask_key
        if datamask_unmasked_time is not None:
            data["datamask-unmasked-time"] = datamask_unmasked_time
        if description is not None:
            data["description"] = description
        if device_ap is not None:
            data["device-ap"] = device_ap
        if device_fortiextender is not None:
            data["device-fortiextender"] = device_fortiextender
        if device_fortiswitch is not None:
            data["device-fortiswitch"] = device_fortiswitch
        if device_manager is not None:
            data["device-manager"] = device_manager
        if device_op is not None:
            data["device-op"] = device_op
        if device_policy_package_lock is not None:
            data["device-policy-package-lock"] = device_policy_package_lock
        if device_wan_link_load_balance is not None:
            data["device-wan-link-load-balance"] = device_wan_link_load_balance
        if event_management is not None:
            data["event-management"] = event_management
        if execute_playbook is not None:
            data["execute-playbook"] = execute_playbook
        if fabric_viewer is not None:
            data["fabric-viewer"] = fabric_viewer
        if fgt_gui_proxy is not None:
            data["fgt-gui-proxy"] = fgt_gui_proxy
        if ips_lock is not None:
            data["ips-lock"] = ips_lock
        if ipv6_trusthost1 is not None:
            data["ipv6_trusthost1"] = ipv6_trusthost1
        if ipv6_trusthost10 is not None:
            data["ipv6_trusthost10"] = ipv6_trusthost10
        if ipv6_trusthost2 is not None:
            data["ipv6_trusthost2"] = ipv6_trusthost2
        if ipv6_trusthost3 is not None:
            data["ipv6_trusthost3"] = ipv6_trusthost3
        if ipv6_trusthost4 is not None:
            data["ipv6_trusthost4"] = ipv6_trusthost4
        if ipv6_trusthost5 is not None:
            data["ipv6_trusthost5"] = ipv6_trusthost5
        if ipv6_trusthost6 is not None:
            data["ipv6_trusthost6"] = ipv6_trusthost6
        if ipv6_trusthost7 is not None:
            data["ipv6_trusthost7"] = ipv6_trusthost7
        if ipv6_trusthost8 is not None:
            data["ipv6_trusthost8"] = ipv6_trusthost8
        if ipv6_trusthost9 is not None:
            data["ipv6_trusthost9"] = ipv6_trusthost9
        if log_viewer is not None:
            data["log-viewer"] = log_viewer
        if profileid is not None:
            data["profileid"] = profileid
        if report_viewer is not None:
            data["report-viewer"] = report_viewer
        if rpc_permit is not None:
            data["rpc-permit"] = rpc_permit
        if run_report is not None:
            data["run-report"] = run_report
        if scope is not None:
            data["scope"] = scope
        if script_access is not None:
            data["script-access"] = script_access
        if script_run is not None:
            data["script-run"] = script_run
        if super_user_profile is not None:
            data["super-user-profile"] = super_user_profile
        if system_setting is not None:
            data["system-setting"] = system_setting
        if triage_events is not None:
            data["triage-events"] = triage_events
        if trusthost1 is not None:
            data["trusthost1"] = trusthost1
        if trusthost10 is not None:
            data["trusthost10"] = trusthost10
        if trusthost2 is not None:
            data["trusthost2"] = trusthost2
        if trusthost3 is not None:
            data["trusthost3"] = trusthost3
        if trusthost4 is not None:
            data["trusthost4"] = trusthost4
        if trusthost5 is not None:
            data["trusthost5"] = trusthost5
        if trusthost6 is not None:
            data["trusthost6"] = trusthost6
        if trusthost7 is not None:
            data["trusthost7"] = trusthost7
        if trusthost8 is not None:
            data["trusthost8"] = trusthost8
        if trusthost9 is not None:
            data["trusthost9"] = trusthost9
        if update_incidents is not None:
            data["update-incidents"] = update_incidents
        if write_passwd_access is not None:
            data["write-passwd-access"] = write_passwd_access
        if write_passwd_profiles is not None:
            data["write-passwd-profiles"] = write_passwd_profiles
        if write_passwd_user_list is not None:
            data["write-passwd-user-list"] = write_passwd_user_list
        
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
        profile: int | str | None = None,
        adom_admin: Literal["disable", "enable"] | None = None,
        adom_lock: Literal["none", "read", "read-write"] | None = None,
        adom_switch: Literal["none", "read", "read-write"] | None = None,
        allow_to_install: Literal["disable", "enable"] | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        datamask: Literal["disable", "enable"] | None = None,
        datamask_custom_priority: Literal["disable", "enable"] | None = None,
        datamask_unmasked_time: int | None = None,
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
        report_viewer: Literal["none", "read", "read-write"] | None = None,
        rpc_permit: Literal["read-write", "none", "read"] | None = None,
        run_report: Literal["none", "read", "read-write"] | None = None,
        scope: Literal["global", "adom"] | None = None,
        script_access: Literal["none", "read", "read-write"] | None = None,
        script_run: Literal["none", "read", "read-write"] | None = None,
        super_user_profile: Literal["disable", "enable"] | None = None,
        system_setting: Literal["none", "read", "read-write"] | None = None,
        triage_events: Literal["none", "read", "read-write"] | None = None,
        update_incidents: Literal["none", "read", "read-write"] | None = None,
        write_passwd_access: Literal["all", "specify-by-user", "specify-by-profile"] | None = None,
        datamask_custom_fields: list[Any] | None = None,
        datamask_fields: list[Any] | None = None,
        datamask_key: list[Any] | None = None,
        description: str | None = None,
        profileid: str | None = None,
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
        write_passwd_profiles: list[Any] | None = None,
        write_passwd_user_list: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            profile: profile parameter
            adom_admin: adom-admin parameter
            adom_lock: adom-lock parameter
            adom_switch: adom-switch parameter
            allow_to_install: allow-to-install parameter
            change_password: change-password parameter
            datamask: datamask parameter
            datamask_custom_fields: datamask-custom-fields parameter
            datamask_custom_priority: datamask-custom-priority parameter
            datamask_fields: datamask-fields parameter
            datamask_key: datamask-key parameter
            ... (49 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if profile is not None:
            url = "/cli/global/system/admin/profile/{profile}"
            url = url.replace("{profile}", str(profile))
        else:
            url = "/cli/global/system/admin/profile"
        
        # Build data payload
        data = {}
        if adom_admin is not None:
            data["adom-admin"] = adom_admin
        if adom_lock is not None:
            data["adom-lock"] = adom_lock
        if adom_switch is not None:
            data["adom-switch"] = adom_switch
        if allow_to_install is not None:
            data["allow-to-install"] = allow_to_install
        if change_password is not None:
            data["change-password"] = change_password
        if datamask is not None:
            data["datamask"] = datamask
        if datamask_custom_fields is not None:
            data["datamask-custom-fields"] = datamask_custom_fields
        if datamask_custom_priority is not None:
            data["datamask-custom-priority"] = datamask_custom_priority
        if datamask_fields is not None:
            data["datamask-fields"] = datamask_fields
        if datamask_key is not None:
            data["datamask-key"] = datamask_key
        if datamask_unmasked_time is not None:
            data["datamask-unmasked-time"] = datamask_unmasked_time
        if description is not None:
            data["description"] = description
        if device_ap is not None:
            data["device-ap"] = device_ap
        if device_fortiextender is not None:
            data["device-fortiextender"] = device_fortiextender
        if device_fortiswitch is not None:
            data["device-fortiswitch"] = device_fortiswitch
        if device_manager is not None:
            data["device-manager"] = device_manager
        if device_op is not None:
            data["device-op"] = device_op
        if device_policy_package_lock is not None:
            data["device-policy-package-lock"] = device_policy_package_lock
        if device_wan_link_load_balance is not None:
            data["device-wan-link-load-balance"] = device_wan_link_load_balance
        if event_management is not None:
            data["event-management"] = event_management
        if execute_playbook is not None:
            data["execute-playbook"] = execute_playbook
        if fabric_viewer is not None:
            data["fabric-viewer"] = fabric_viewer
        if fgt_gui_proxy is not None:
            data["fgt-gui-proxy"] = fgt_gui_proxy
        if ips_lock is not None:
            data["ips-lock"] = ips_lock
        if ipv6_trusthost1 is not None:
            data["ipv6_trusthost1"] = ipv6_trusthost1
        if ipv6_trusthost10 is not None:
            data["ipv6_trusthost10"] = ipv6_trusthost10
        if ipv6_trusthost2 is not None:
            data["ipv6_trusthost2"] = ipv6_trusthost2
        if ipv6_trusthost3 is not None:
            data["ipv6_trusthost3"] = ipv6_trusthost3
        if ipv6_trusthost4 is not None:
            data["ipv6_trusthost4"] = ipv6_trusthost4
        if ipv6_trusthost5 is not None:
            data["ipv6_trusthost5"] = ipv6_trusthost5
        if ipv6_trusthost6 is not None:
            data["ipv6_trusthost6"] = ipv6_trusthost6
        if ipv6_trusthost7 is not None:
            data["ipv6_trusthost7"] = ipv6_trusthost7
        if ipv6_trusthost8 is not None:
            data["ipv6_trusthost8"] = ipv6_trusthost8
        if ipv6_trusthost9 is not None:
            data["ipv6_trusthost9"] = ipv6_trusthost9
        if log_viewer is not None:
            data["log-viewer"] = log_viewer
        if profileid is not None:
            data["profileid"] = profileid
        if report_viewer is not None:
            data["report-viewer"] = report_viewer
        if rpc_permit is not None:
            data["rpc-permit"] = rpc_permit
        if run_report is not None:
            data["run-report"] = run_report
        if scope is not None:
            data["scope"] = scope
        if script_access is not None:
            data["script-access"] = script_access
        if script_run is not None:
            data["script-run"] = script_run
        if super_user_profile is not None:
            data["super-user-profile"] = super_user_profile
        if system_setting is not None:
            data["system-setting"] = system_setting
        if triage_events is not None:
            data["triage-events"] = triage_events
        if trusthost1 is not None:
            data["trusthost1"] = trusthost1
        if trusthost10 is not None:
            data["trusthost10"] = trusthost10
        if trusthost2 is not None:
            data["trusthost2"] = trusthost2
        if trusthost3 is not None:
            data["trusthost3"] = trusthost3
        if trusthost4 is not None:
            data["trusthost4"] = trusthost4
        if trusthost5 is not None:
            data["trusthost5"] = trusthost5
        if trusthost6 is not None:
            data["trusthost6"] = trusthost6
        if trusthost7 is not None:
            data["trusthost7"] = trusthost7
        if trusthost8 is not None:
            data["trusthost8"] = trusthost8
        if trusthost9 is not None:
            data["trusthost9"] = trusthost9
        if update_incidents is not None:
            data["update-incidents"] = update_incidents
        if write_passwd_access is not None:
            data["write-passwd-access"] = write_passwd_access
        if write_passwd_profiles is not None:
            data["write-passwd-profiles"] = write_passwd_profiles
        if write_passwd_user_list is not None:
            data["write-passwd-user-list"] = write_passwd_user_list
        
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

    def delete(self, profile: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            profile: profile parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if profile is not None:
            url = "/cli/global/system/admin/profile/{profile}"
            url = url.replace("{profile}", str(profile))
        else:
            url = "/cli/global/system/admin/profile"
        
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

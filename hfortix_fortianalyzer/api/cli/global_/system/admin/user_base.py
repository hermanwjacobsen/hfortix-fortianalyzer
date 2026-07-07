"""
FortiAnalyzer API endpoint: cli.global.system.admin.user

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminUser:
    """
    FortiAnalyzer endpoint: cli.global.system.admin.user
    
    
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
        user: int | str | None = None,
        fields: list[Literal["adom-access", "autoreg-user", "avatar", "ca", "change-password", "cors-allow-origin", "description", "dev-group", "email-address", "ext-auth-accprofile-override", "ext-auth-adom-override", "ext-auth-group-match", "fingerprint", "first-name", "force-password-change", "fortiai", "group", "ipv6_trusthost1", "ipv6_trusthost10", "ipv6_trusthost2", "ipv6_trusthost3", "ipv6_trusthost4", "ipv6_trusthost5", "ipv6_trusthost6", "ipv6_trusthost7", "ipv6_trusthost8", "ipv6_trusthost9", "last-name", "ldap-server", "login-max", "mobile-number", "old-password", "pager-number", "password", "password-expire", "phone-number", "profileid", "radius_server", "rpc-permit", "ssh-public-key1", "ssh-public-key2", "ssh-public-key3", "subject", "tacacs-plus-server", "th-from-profile", "th6-from-profile", "trusthost1", "trusthost10", "trusthost2", "trusthost3", "trusthost4", "trusthost5", "trusthost6", "trusthost7", "trusthost8", "trusthost9", "two-factor-auth", "use-global-theme", "user-theme", "user_type", "userid", "wildcard"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            user: user parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None:
            url = "/cli/global/system/admin/user/{user}"
            url = url.replace("{user}", str(user))
        else:
            url = "/cli/global/system/admin/user"
        
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
        user: int | str | None = None,
        adom_access: Literal["all", "specify", "exclude", "per-adom-profile"] | None = None,
        autoreg_user: Literal["disable", "enable"] | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        ext_auth_accprofile_override: Literal["disable", "enable"] | None = None,
        ext_auth_adom_override: Literal["disable", "enable"] | None = None,
        force_password_change: Literal["disable", "enable"] | None = None,
        fortiai: Literal["disable", "enable"] | None = None,
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
        login_max: int | None = None,
        profileid: str | None = None,
        rpc_permit: Literal["read-write", "none", "read", "from-profile"] | None = None,
        th_from_profile: int | None = None,
        th6_from_profile: int | None = None,
        two_factor_auth: Literal["disable", "password", "ftc-ftm", "ftc-email", "ftc-sms"] | None = None,
        use_global_theme: Literal["disable", "enable"] | None = None,
        user_theme: Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None = None,
        user_type: Literal["local", "radius", "ldap", "tacacs-plus", "pki-auth", "group", "sso", "api"] | None = None,
        wildcard: Literal["disable", "enable"] | None = None,
        adom: list[Any] | None = None,
        avatar: str | None = None,
        ca: str | None = None,
        cors_allow_origin: str | None = None,
        dashboard: list[Any] | None = None,
        dashboard_tabs: list[Any] | None = None,
        description: str | None = None,
        dev_group: str | None = None,
        email_address: str | None = None,
        ext_auth_group_match: str | None = None,
        fingerprint: str | None = None,
        first_name: str | None = None,
        group: str | None = None,
        last_name: str | None = None,
        ldap_server: str | None = None,
        meta_data: list[Any] | None = None,
        mobile_number: str | None = None,
        old_password: str | None = None,
        pager_number: str | None = None,
        password: str | None = None,
        password_expire: str | None = None,
        phone_number: str | None = None,
        policy_block: list[Any] | None = None,
        policy_package: list[Any] | None = None,
        radius_server: str | None = None,
        ssh_public_key1: list[Any] | None = None,
        ssh_public_key2: list[Any] | None = None,
        ssh_public_key3: list[Any] | None = None,
        subject: str | None = None,
        tacacs_plus_server: str | None = None,
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
        userid: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            user: user parameter
            adom: adom parameter
            adom_access: adom-access parameter
            autoreg_user: autoreg-user parameter
            avatar: avatar parameter
            ca: ca parameter
            change_password: change-password parameter
            cors_allow_origin: cors-allow-origin parameter
            dashboard: dashboard parameter
            dashboard_tabs: dashboard-tabs parameter
            description: description parameter
            ... (58 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/admin/user"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if adom_access is not None:
            data["adom-access"] = adom_access
        if autoreg_user is not None:
            data["autoreg-user"] = autoreg_user
        if avatar is not None:
            data["avatar"] = avatar
        if ca is not None:
            data["ca"] = ca
        if change_password is not None:
            data["change-password"] = change_password
        if cors_allow_origin is not None:
            data["cors-allow-origin"] = cors_allow_origin
        if dashboard is not None:
            data["dashboard"] = dashboard
        if dashboard_tabs is not None:
            data["dashboard-tabs"] = dashboard_tabs
        if description is not None:
            data["description"] = description
        if dev_group is not None:
            data["dev-group"] = dev_group
        if email_address is not None:
            data["email-address"] = email_address
        if ext_auth_accprofile_override is not None:
            data["ext-auth-accprofile-override"] = ext_auth_accprofile_override
        if ext_auth_adom_override is not None:
            data["ext-auth-adom-override"] = ext_auth_adom_override
        if ext_auth_group_match is not None:
            data["ext-auth-group-match"] = ext_auth_group_match
        if fingerprint is not None:
            data["fingerprint"] = fingerprint
        if first_name is not None:
            data["first-name"] = first_name
        if force_password_change is not None:
            data["force-password-change"] = force_password_change
        if fortiai is not None:
            data["fortiai"] = fortiai
        if group is not None:
            data["group"] = group
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
        if last_name is not None:
            data["last-name"] = last_name
        if ldap_server is not None:
            data["ldap-server"] = ldap_server
        if login_max is not None:
            data["login-max"] = login_max
        if meta_data is not None:
            data["meta-data"] = meta_data
        if mobile_number is not None:
            data["mobile-number"] = mobile_number
        if old_password is not None:
            data["old-password"] = old_password
        if pager_number is not None:
            data["pager-number"] = pager_number
        if password is not None:
            data["password"] = password
        if password_expire is not None:
            data["password-expire"] = password_expire
        if phone_number is not None:
            data["phone-number"] = phone_number
        if policy_block is not None:
            data["policy-block"] = policy_block
        if policy_package is not None:
            data["policy-package"] = policy_package
        if profileid is not None:
            data["profileid"] = profileid
        if radius_server is not None:
            data["radius_server"] = radius_server
        if rpc_permit is not None:
            data["rpc-permit"] = rpc_permit
        if ssh_public_key1 is not None:
            data["ssh-public-key1"] = ssh_public_key1
        if ssh_public_key2 is not None:
            data["ssh-public-key2"] = ssh_public_key2
        if ssh_public_key3 is not None:
            data["ssh-public-key3"] = ssh_public_key3
        if subject is not None:
            data["subject"] = subject
        if tacacs_plus_server is not None:
            data["tacacs-plus-server"] = tacacs_plus_server
        if th_from_profile is not None:
            data["th-from-profile"] = th_from_profile
        if th6_from_profile is not None:
            data["th6-from-profile"] = th6_from_profile
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
        if two_factor_auth is not None:
            data["two-factor-auth"] = two_factor_auth
        if use_global_theme is not None:
            data["use-global-theme"] = use_global_theme
        if user_theme is not None:
            data["user-theme"] = user_theme
        if user_type is not None:
            data["user_type"] = user_type
        if userid is not None:
            data["userid"] = userid
        if wildcard is not None:
            data["wildcard"] = wildcard
        
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
        user: int | str | None = None,
        adom_access: Literal["all", "specify", "exclude", "per-adom-profile"] | None = None,
        autoreg_user: Literal["disable", "enable"] | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        ext_auth_accprofile_override: Literal["disable", "enable"] | None = None,
        ext_auth_adom_override: Literal["disable", "enable"] | None = None,
        force_password_change: Literal["disable", "enable"] | None = None,
        fortiai: Literal["disable", "enable"] | None = None,
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
        login_max: int | None = None,
        profileid: str | None = None,
        rpc_permit: Literal["read-write", "none", "read", "from-profile"] | None = None,
        th_from_profile: int | None = None,
        th6_from_profile: int | None = None,
        two_factor_auth: Literal["disable", "password", "ftc-ftm", "ftc-email", "ftc-sms"] | None = None,
        use_global_theme: Literal["disable", "enable"] | None = None,
        user_theme: Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None = None,
        user_type: Literal["local", "radius", "ldap", "tacacs-plus", "pki-auth", "group", "sso", "api"] | None = None,
        wildcard: Literal["disable", "enable"] | None = None,
        adom: list[Any] | None = None,
        avatar: str | None = None,
        ca: str | None = None,
        cors_allow_origin: str | None = None,
        dashboard: list[Any] | None = None,
        dashboard_tabs: list[Any] | None = None,
        description: str | None = None,
        dev_group: str | None = None,
        email_address: str | None = None,
        ext_auth_group_match: str | None = None,
        fingerprint: str | None = None,
        first_name: str | None = None,
        group: str | None = None,
        last_name: str | None = None,
        ldap_server: str | None = None,
        meta_data: list[Any] | None = None,
        mobile_number: str | None = None,
        old_password: str | None = None,
        pager_number: str | None = None,
        password: str | None = None,
        password_expire: str | None = None,
        phone_number: str | None = None,
        policy_block: list[Any] | None = None,
        policy_package: list[Any] | None = None,
        radius_server: str | None = None,
        ssh_public_key1: list[Any] | None = None,
        ssh_public_key2: list[Any] | None = None,
        ssh_public_key3: list[Any] | None = None,
        subject: str | None = None,
        tacacs_plus_server: str | None = None,
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
        userid: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            user: user parameter
            adom: adom parameter
            adom_access: adom-access parameter
            autoreg_user: autoreg-user parameter
            avatar: avatar parameter
            ca: ca parameter
            change_password: change-password parameter
            cors_allow_origin: cors-allow-origin parameter
            dashboard: dashboard parameter
            dashboard_tabs: dashboard-tabs parameter
            description: description parameter
            ... (58 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None:
            url = "/cli/global/system/admin/user/{user}"
            url = url.replace("{user}", str(user))
        else:
            url = "/cli/global/system/admin/user"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if adom_access is not None:
            data["adom-access"] = adom_access
        if autoreg_user is not None:
            data["autoreg-user"] = autoreg_user
        if avatar is not None:
            data["avatar"] = avatar
        if ca is not None:
            data["ca"] = ca
        if change_password is not None:
            data["change-password"] = change_password
        if cors_allow_origin is not None:
            data["cors-allow-origin"] = cors_allow_origin
        if dashboard is not None:
            data["dashboard"] = dashboard
        if dashboard_tabs is not None:
            data["dashboard-tabs"] = dashboard_tabs
        if description is not None:
            data["description"] = description
        if dev_group is not None:
            data["dev-group"] = dev_group
        if email_address is not None:
            data["email-address"] = email_address
        if ext_auth_accprofile_override is not None:
            data["ext-auth-accprofile-override"] = ext_auth_accprofile_override
        if ext_auth_adom_override is not None:
            data["ext-auth-adom-override"] = ext_auth_adom_override
        if ext_auth_group_match is not None:
            data["ext-auth-group-match"] = ext_auth_group_match
        if fingerprint is not None:
            data["fingerprint"] = fingerprint
        if first_name is not None:
            data["first-name"] = first_name
        if force_password_change is not None:
            data["force-password-change"] = force_password_change
        if fortiai is not None:
            data["fortiai"] = fortiai
        if group is not None:
            data["group"] = group
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
        if last_name is not None:
            data["last-name"] = last_name
        if ldap_server is not None:
            data["ldap-server"] = ldap_server
        if login_max is not None:
            data["login-max"] = login_max
        if meta_data is not None:
            data["meta-data"] = meta_data
        if mobile_number is not None:
            data["mobile-number"] = mobile_number
        if old_password is not None:
            data["old-password"] = old_password
        if pager_number is not None:
            data["pager-number"] = pager_number
        if password is not None:
            data["password"] = password
        if password_expire is not None:
            data["password-expire"] = password_expire
        if phone_number is not None:
            data["phone-number"] = phone_number
        if policy_block is not None:
            data["policy-block"] = policy_block
        if policy_package is not None:
            data["policy-package"] = policy_package
        if profileid is not None:
            data["profileid"] = profileid
        if radius_server is not None:
            data["radius_server"] = radius_server
        if rpc_permit is not None:
            data["rpc-permit"] = rpc_permit
        if ssh_public_key1 is not None:
            data["ssh-public-key1"] = ssh_public_key1
        if ssh_public_key2 is not None:
            data["ssh-public-key2"] = ssh_public_key2
        if ssh_public_key3 is not None:
            data["ssh-public-key3"] = ssh_public_key3
        if subject is not None:
            data["subject"] = subject
        if tacacs_plus_server is not None:
            data["tacacs-plus-server"] = tacacs_plus_server
        if th_from_profile is not None:
            data["th-from-profile"] = th_from_profile
        if th6_from_profile is not None:
            data["th6-from-profile"] = th6_from_profile
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
        if two_factor_auth is not None:
            data["two-factor-auth"] = two_factor_auth
        if use_global_theme is not None:
            data["use-global-theme"] = use_global_theme
        if user_theme is not None:
            data["user-theme"] = user_theme
        if user_type is not None:
            data["user_type"] = user_type
        if userid is not None:
            data["userid"] = userid
        if wildcard is not None:
            data["wildcard"] = wildcard
        
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
        user: int | str | None = None,
        adom_access: Literal["all", "specify", "exclude", "per-adom-profile"] | None = None,
        autoreg_user: Literal["disable", "enable"] | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        ext_auth_accprofile_override: Literal["disable", "enable"] | None = None,
        ext_auth_adom_override: Literal["disable", "enable"] | None = None,
        force_password_change: Literal["disable", "enable"] | None = None,
        fortiai: Literal["disable", "enable"] | None = None,
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
        login_max: int | None = None,
        profileid: str | None = None,
        rpc_permit: Literal["read-write", "none", "read", "from-profile"] | None = None,
        th_from_profile: int | None = None,
        th6_from_profile: int | None = None,
        two_factor_auth: Literal["disable", "password", "ftc-ftm", "ftc-email", "ftc-sms"] | None = None,
        use_global_theme: Literal["disable", "enable"] | None = None,
        user_theme: Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None = None,
        user_type: Literal["local", "radius", "ldap", "tacacs-plus", "pki-auth", "group", "sso", "api"] | None = None,
        wildcard: Literal["disable", "enable"] | None = None,
        adom: list[Any] | None = None,
        avatar: str | None = None,
        ca: str | None = None,
        cors_allow_origin: str | None = None,
        dashboard: list[Any] | None = None,
        dashboard_tabs: list[Any] | None = None,
        description: str | None = None,
        dev_group: str | None = None,
        email_address: str | None = None,
        ext_auth_group_match: str | None = None,
        fingerprint: str | None = None,
        first_name: str | None = None,
        group: str | None = None,
        last_name: str | None = None,
        ldap_server: str | None = None,
        meta_data: list[Any] | None = None,
        mobile_number: str | None = None,
        old_password: str | None = None,
        pager_number: str | None = None,
        password: str | None = None,
        password_expire: str | None = None,
        phone_number: str | None = None,
        policy_block: list[Any] | None = None,
        policy_package: list[Any] | None = None,
        radius_server: str | None = None,
        ssh_public_key1: list[Any] | None = None,
        ssh_public_key2: list[Any] | None = None,
        ssh_public_key3: list[Any] | None = None,
        subject: str | None = None,
        tacacs_plus_server: str | None = None,
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
        userid: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            user: user parameter
            adom: adom parameter
            adom_access: adom-access parameter
            autoreg_user: autoreg-user parameter
            avatar: avatar parameter
            ca: ca parameter
            change_password: change-password parameter
            cors_allow_origin: cors-allow-origin parameter
            dashboard: dashboard parameter
            dashboard_tabs: dashboard-tabs parameter
            description: description parameter
            ... (58 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None:
            url = "/cli/global/system/admin/user/{user}"
            url = url.replace("{user}", str(user))
        else:
            url = "/cli/global/system/admin/user"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if adom_access is not None:
            data["adom-access"] = adom_access
        if autoreg_user is not None:
            data["autoreg-user"] = autoreg_user
        if avatar is not None:
            data["avatar"] = avatar
        if ca is not None:
            data["ca"] = ca
        if change_password is not None:
            data["change-password"] = change_password
        if cors_allow_origin is not None:
            data["cors-allow-origin"] = cors_allow_origin
        if dashboard is not None:
            data["dashboard"] = dashboard
        if dashboard_tabs is not None:
            data["dashboard-tabs"] = dashboard_tabs
        if description is not None:
            data["description"] = description
        if dev_group is not None:
            data["dev-group"] = dev_group
        if email_address is not None:
            data["email-address"] = email_address
        if ext_auth_accprofile_override is not None:
            data["ext-auth-accprofile-override"] = ext_auth_accprofile_override
        if ext_auth_adom_override is not None:
            data["ext-auth-adom-override"] = ext_auth_adom_override
        if ext_auth_group_match is not None:
            data["ext-auth-group-match"] = ext_auth_group_match
        if fingerprint is not None:
            data["fingerprint"] = fingerprint
        if first_name is not None:
            data["first-name"] = first_name
        if force_password_change is not None:
            data["force-password-change"] = force_password_change
        if fortiai is not None:
            data["fortiai"] = fortiai
        if group is not None:
            data["group"] = group
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
        if last_name is not None:
            data["last-name"] = last_name
        if ldap_server is not None:
            data["ldap-server"] = ldap_server
        if login_max is not None:
            data["login-max"] = login_max
        if meta_data is not None:
            data["meta-data"] = meta_data
        if mobile_number is not None:
            data["mobile-number"] = mobile_number
        if old_password is not None:
            data["old-password"] = old_password
        if pager_number is not None:
            data["pager-number"] = pager_number
        if password is not None:
            data["password"] = password
        if password_expire is not None:
            data["password-expire"] = password_expire
        if phone_number is not None:
            data["phone-number"] = phone_number
        if policy_block is not None:
            data["policy-block"] = policy_block
        if policy_package is not None:
            data["policy-package"] = policy_package
        if profileid is not None:
            data["profileid"] = profileid
        if radius_server is not None:
            data["radius_server"] = radius_server
        if rpc_permit is not None:
            data["rpc-permit"] = rpc_permit
        if ssh_public_key1 is not None:
            data["ssh-public-key1"] = ssh_public_key1
        if ssh_public_key2 is not None:
            data["ssh-public-key2"] = ssh_public_key2
        if ssh_public_key3 is not None:
            data["ssh-public-key3"] = ssh_public_key3
        if subject is not None:
            data["subject"] = subject
        if tacacs_plus_server is not None:
            data["tacacs-plus-server"] = tacacs_plus_server
        if th_from_profile is not None:
            data["th-from-profile"] = th_from_profile
        if th6_from_profile is not None:
            data["th6-from-profile"] = th6_from_profile
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
        if two_factor_auth is not None:
            data["two-factor-auth"] = two_factor_auth
        if use_global_theme is not None:
            data["use-global-theme"] = use_global_theme
        if user_theme is not None:
            data["user-theme"] = user_theme
        if user_type is not None:
            data["user_type"] = user_type
        if userid is not None:
            data["userid"] = userid
        if wildcard is not None:
            data["wildcard"] = wildcard
        
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

    def delete(self, user: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            user: user parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None:
            url = "/cli/global/system/admin/user/{user}"
            url = url.replace("{user}", str(user))
        else:
            url = "/cli/global/system/admin/user"
        
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

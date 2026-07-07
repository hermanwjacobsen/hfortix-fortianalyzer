"""FortiAnalyzer admin system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import group
    from . import ldap
    from . import profile
    from . import radius
    from . import setting
    from . import tacacs
    from . import user

__all__ = ["Admin"]


class Admin:
    """FortiAnalyzer admin system API endpoints."""

    group: "group.CliGlobalSystemAdminGroup"
    ldap: "ldap.CliGlobalSystemAdminLdap"
    profile: "profile.CliGlobalSystemAdminProfile"
    radius: "radius.CliGlobalSystemAdminRadius"
    setting: "setting.CliGlobalSystemAdminSetting"
    tacacs: "tacacs.CliGlobalSystemAdminTacacs"
    user: "user.CliGlobalSystemAdminUser"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Admin namespace with JSON-RPC client."""
        from . import group as group_module
        from . import ldap as ldap_module
        from . import profile as profile_module
        from . import radius as radius_module
        from . import setting as setting_module
        from . import tacacs as tacacs_module
        from . import user as user_module

        self.group = group_module.CliGlobalSystemAdminGroup(client)
        self.ldap = ldap_module.CliGlobalSystemAdminLdap(client)
        self.profile = profile_module.CliGlobalSystemAdminProfile(client)
        self.radius = radius_module.CliGlobalSystemAdminRadius(client)
        self.setting = setting_module.CliGlobalSystemAdminSetting(client)
        self.tacacs = tacacs_module.CliGlobalSystemAdminTacacs(client)
        self.user = user_module.CliGlobalSystemAdminUser(client)

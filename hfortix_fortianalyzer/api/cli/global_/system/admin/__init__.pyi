"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .group import CliGlobalSystemAdminGroup
    from .ldap import CliGlobalSystemAdminLdap
    from .profile import CliGlobalSystemAdminProfile
    from .radius import CliGlobalSystemAdminRadius
    from .setting import CliGlobalSystemAdminSetting
    from .tacacs import CliGlobalSystemAdminTacacs
    from .user import CliGlobalSystemAdminUser

__all__ = ["Admin"]


class Admin:
    """Admin endpoints."""

    group: CliGlobalSystemAdminGroup
    ldap: CliGlobalSystemAdminLdap
    profile: CliGlobalSystemAdminProfile
    radius: CliGlobalSystemAdminRadius
    setting: CliGlobalSystemAdminSetting
    tacacs: CliGlobalSystemAdminTacacs
    user: CliGlobalSystemAdminUser

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

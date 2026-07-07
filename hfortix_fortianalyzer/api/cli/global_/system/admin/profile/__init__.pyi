"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .datamask_custom_fields import CliGlobalSystemAdminProfileDatamaskCustomFields
    from .write_passwd_profiles import CliGlobalSystemAdminProfileWritePasswdProfiles
    from .write_passwd_user_list import CliGlobalSystemAdminProfileWritePasswdUserList

__all__ = ["CliGlobalSystemAdminProfile"]


from ..profile_base import CliGlobalSystemAdminProfile as CliGlobalSystemAdminProfileBase

class CliGlobalSystemAdminProfile(CliGlobalSystemAdminProfileBase):
    """CliGlobalSystemAdminProfile endpoints."""

    datamask_custom_fields: CliGlobalSystemAdminProfileDatamaskCustomFields
    write_passwd_profiles: CliGlobalSystemAdminProfileWritePasswdProfiles
    write_passwd_user_list: CliGlobalSystemAdminProfileWritePasswdUserList

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

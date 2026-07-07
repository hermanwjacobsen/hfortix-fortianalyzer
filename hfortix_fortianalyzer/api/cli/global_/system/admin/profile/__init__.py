"""FortiAnalyzer profile admin API endpoints."""

from __future__ import annotations

from ..profile_base import CliGlobalSystemAdminProfile as CliGlobalSystemAdminProfileBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import datamask_custom_fields
    from . import write_passwd_profiles
    from . import write_passwd_user_list

__all__ = ["CliGlobalSystemAdminProfile"]


class CliGlobalSystemAdminProfile(CliGlobalSystemAdminProfileBase):
    """FortiAnalyzer profile admin API endpoints."""

    datamask_custom_fields: "datamask_custom_fields.CliGlobalSystemAdminProfileDatamaskCustomFields"
    write_passwd_profiles: "write_passwd_profiles.CliGlobalSystemAdminProfileWritePasswdProfiles"
    write_passwd_user_list: "write_passwd_user_list.CliGlobalSystemAdminProfileWritePasswdUserList"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemAdminProfile with endpoint methods and child modules."""
        super().__init__(client)

        from . import datamask_custom_fields as datamask_custom_fields_module
        from . import write_passwd_profiles as write_passwd_profiles_module
        from . import write_passwd_user_list as write_passwd_user_list_module

        self.datamask_custom_fields = datamask_custom_fields_module.CliGlobalSystemAdminProfileDatamaskCustomFields(client)
        self.write_passwd_profiles = write_passwd_profiles_module.CliGlobalSystemAdminProfileWritePasswdProfiles(client)
        self.write_passwd_user_list = write_passwd_user_list_module.CliGlobalSystemAdminProfileWritePasswdUserList(client)

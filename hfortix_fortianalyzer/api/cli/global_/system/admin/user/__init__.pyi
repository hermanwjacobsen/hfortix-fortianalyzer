"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .adom import CliGlobalSystemAdminUserAdom
    from .dashboard import CliGlobalSystemAdminUserDashboard
    from .dashboard_tabs import CliGlobalSystemAdminUserDashboardTabs
    from .meta_data import CliGlobalSystemAdminUserMetaData
    from .policy_block import CliGlobalSystemAdminUserPolicyBlock
    from .policy_package import CliGlobalSystemAdminUserPolicyPackage

__all__ = ["CliGlobalSystemAdminUser"]


from ..user_base import CliGlobalSystemAdminUser as CliGlobalSystemAdminUserBase

class CliGlobalSystemAdminUser(CliGlobalSystemAdminUserBase):
    """CliGlobalSystemAdminUser endpoints."""

    adom: CliGlobalSystemAdminUserAdom
    dashboard: CliGlobalSystemAdminUserDashboard
    dashboard_tabs: CliGlobalSystemAdminUserDashboardTabs
    meta_data: CliGlobalSystemAdminUserMetaData
    policy_block: CliGlobalSystemAdminUserPolicyBlock
    policy_package: CliGlobalSystemAdminUserPolicyPackage

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

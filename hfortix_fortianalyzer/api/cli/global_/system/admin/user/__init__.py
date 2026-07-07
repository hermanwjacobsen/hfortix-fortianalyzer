"""FortiAnalyzer user admin API endpoints."""

from __future__ import annotations

from ..user_base import CliGlobalSystemAdminUser as CliGlobalSystemAdminUserBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom
    from . import dashboard
    from . import dashboard_tabs
    from . import meta_data
    from . import policy_block
    from . import policy_package

__all__ = ["CliGlobalSystemAdminUser"]


class CliGlobalSystemAdminUser(CliGlobalSystemAdminUserBase):
    """FortiAnalyzer user admin API endpoints."""

    adom: "adom.CliGlobalSystemAdminUserAdom"
    dashboard: "dashboard.CliGlobalSystemAdminUserDashboard"
    dashboard_tabs: "dashboard_tabs.CliGlobalSystemAdminUserDashboardTabs"
    meta_data: "meta_data.CliGlobalSystemAdminUserMetaData"
    policy_block: "policy_block.CliGlobalSystemAdminUserPolicyBlock"
    policy_package: "policy_package.CliGlobalSystemAdminUserPolicyPackage"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemAdminUser with endpoint methods and child modules."""
        super().__init__(client)

        from . import adom as adom_module
        from . import dashboard as dashboard_module
        from . import dashboard_tabs as dashboard_tabs_module
        from . import meta_data as meta_data_module
        from . import policy_block as policy_block_module
        from . import policy_package as policy_package_module

        self.adom = adom_module.CliGlobalSystemAdminUserAdom(client)
        self.dashboard = dashboard_module.CliGlobalSystemAdminUserDashboard(client)
        self.dashboard_tabs = dashboard_tabs_module.CliGlobalSystemAdminUserDashboardTabs(client)
        self.meta_data = meta_data_module.CliGlobalSystemAdminUserMetaData(client)
        self.policy_block = policy_block_module.CliGlobalSystemAdminUserPolicyBlock(client)
        self.policy_package = policy_package_module.CliGlobalSystemAdminUserPolicyPackage(client)

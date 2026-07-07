"""FortiAnalyzer snmp system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import community
    from . import sysinfo
    from . import user

__all__ = ["SNMP"]


class SNMP:
    """FortiAnalyzer snmp system API endpoints."""

    community: "community.CliGlobalSystemSnmpCommunity"
    sysinfo: "sysinfo.CliGlobalSystemSnmpSysinfo"
    user: "user.CliGlobalSystemSnmpUser"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize SNMP namespace with JSON-RPC client."""
        from . import community as community_module
        from . import sysinfo as sysinfo_module
        from . import user as user_module

        self.community = community_module.CliGlobalSystemSnmpCommunity(client)
        self.sysinfo = sysinfo_module.CliGlobalSystemSnmpSysinfo(client)
        self.user = user_module.CliGlobalSystemSnmpUser(client)

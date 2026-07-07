"""FortiAnalyzer community snmp API endpoints."""

from __future__ import annotations

from ..community_base import CliGlobalSystemSnmpCommunity as CliGlobalSystemSnmpCommunityBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import hosts
    from . import hosts6

__all__ = ["CliGlobalSystemSnmpCommunity"]


class CliGlobalSystemSnmpCommunity(CliGlobalSystemSnmpCommunityBase):
    """FortiAnalyzer community snmp API endpoints."""

    hosts: "hosts.CliGlobalSystemSnmpCommunityHosts"
    hosts6: "hosts6.CliGlobalSystemSnmpCommunityHosts6"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemSnmpCommunity with endpoint methods and child modules."""
        super().__init__(client)

        from . import hosts as hosts_module
        from . import hosts6 as hosts6_module

        self.hosts = hosts_module.CliGlobalSystemSnmpCommunityHosts(client)
        self.hosts6 = hosts6_module.CliGlobalSystemSnmpCommunityHosts6(client)

"""FortiAnalyzer interface system API endpoints."""

from __future__ import annotations

from ..interface_base import CliGlobalSystemInterface as CliGlobalSystemInterfaceBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ipv6
    from . import member

__all__ = ["CliGlobalSystemInterface"]


class CliGlobalSystemInterface(CliGlobalSystemInterfaceBase):
    """FortiAnalyzer interface system API endpoints."""

    ipv6: "ipv6.CliGlobalSystemInterfaceIpv6"
    member: "member.CliGlobalSystemInterfaceMember"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemInterface with endpoint methods and child modules."""
        super().__init__(client)

        from . import ipv6 as ipv6_module
        from . import member as member_module

        self.ipv6 = ipv6_module.CliGlobalSystemInterfaceIpv6(client)
        self.member = member_module.CliGlobalSystemInterfaceMember(client)

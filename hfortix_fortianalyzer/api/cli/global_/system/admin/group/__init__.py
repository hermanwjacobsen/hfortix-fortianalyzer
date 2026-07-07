"""FortiAnalyzer group admin API endpoints."""

from __future__ import annotations

from ..group_base import CliGlobalSystemAdminGroup as CliGlobalSystemAdminGroupBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import member

__all__ = ["CliGlobalSystemAdminGroup"]


class CliGlobalSystemAdminGroup(CliGlobalSystemAdminGroupBase):
    """FortiAnalyzer group admin API endpoints."""

    member: "member.CliGlobalSystemAdminGroupMember"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemAdminGroup with endpoint methods and child modules."""
        super().__init__(client)

        from . import member as member_module

        self.member = member_module.CliGlobalSystemAdminGroupMember(client)

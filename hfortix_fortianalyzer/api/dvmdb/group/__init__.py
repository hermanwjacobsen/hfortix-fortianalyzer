"""FortiAnalyzer group API endpoints."""

from __future__ import annotations

from ..group_base import DvmdbGroup as DvmdbGroupBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import object_member

__all__ = ["DvmdbGroup"]


class DvmdbGroup(DvmdbGroupBase):
    """FortiAnalyzer group API endpoints."""

    object_member: "object_member.DvmdbGroupObjectMember"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize DvmdbGroup with endpoint methods and child modules."""
        super().__init__(client)

        from . import object_member as object_member_module

        self.object_member = object_member_module.DvmdbGroupObjectMember(client)

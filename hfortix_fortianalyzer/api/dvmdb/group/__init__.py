"""FortiManager group API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import object_member

__all__ = ["Group"]


class Group:
    """FortiManager group API endpoints."""

    object_member: "object_member.DvmdbGroupObjectMember"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Group namespace with JSON-RPC client."""
        from . import object_member as object_member_module

        self.object_member = object_member_module.DvmdbGroupObjectMember(client)

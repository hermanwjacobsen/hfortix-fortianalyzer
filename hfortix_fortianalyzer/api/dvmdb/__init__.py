"""FortiManager dvmdb API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom
    from . import device
    from . import folder
    from . import group
    from . import object_member

__all__ = ["Dvmdb"]


class Dvmdb:
    """FortiManager dvmdb API endpoints."""

    adom: "adom.DvmdbAdom"
    device: "device.Device"
    folder: "folder.DvmdbFolder"
    group: "group.Group"
    object_member: "object_member.DvmdbObjectMember"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Dvmdb namespace with JSON-RPC client."""
        from . import adom as adom_module
        from . import device as device_module
        from . import folder as folder_module
        from . import group as group_module
        from . import object_member as object_member_module

        self.adom = adom_module.DvmdbAdom(client)
        self.device = device_module.Device(client)
        self.folder = folder_module.DvmdbFolder(client)
        self.group = group_module.Group(client)
        self.object_member = object_member_module.DvmdbObjectMember(client)

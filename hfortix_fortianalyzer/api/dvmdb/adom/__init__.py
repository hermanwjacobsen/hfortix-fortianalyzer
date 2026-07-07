"""FortiAnalyzer adom API endpoints."""

from __future__ import annotations

from ..adom_base import DvmdbAdom as DvmdbAdomBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import device
    from . import folder
    from . import group
    from . import object_member

__all__ = ["DvmdbAdom"]


class DvmdbAdom(DvmdbAdomBase):
    """FortiAnalyzer adom API endpoints."""

    device: "device.DvmdbAdomDevice"
    folder: "folder.DvmdbAdomFolder"
    group: "group.DvmdbAdomGroup"
    object_member: "object_member.DvmdbAdomObjectMember"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize DvmdbAdom with endpoint methods and child modules."""
        super().__init__(client)

        from . import device as device_module
        from . import folder as folder_module
        from . import group as group_module
        from . import object_member as object_member_module

        self.device = device_module.DvmdbAdomDevice(client)
        self.folder = folder_module.DvmdbAdomFolder(client)
        self.group = group_module.DvmdbAdomGroup(client)
        self.object_member = object_member_module.DvmdbAdomObjectMember(client)

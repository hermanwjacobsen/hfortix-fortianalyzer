"""FortiAnalyzer dvmdb API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom
    from . import device
    from . import folder
    from . import group

__all__ = ["Dvmdb"]


class Dvmdb:
    """FortiAnalyzer dvmdb API endpoints."""

    adom: "adom.DvmdbAdom"
    device: "device.DvmdbDevice"
    folder: "folder.DvmdbFolder"
    group: "group.DvmdbGroup"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Dvmdb namespace with JSON-RPC client."""
        from . import adom as adom_module
        from . import device as device_module
        from . import folder as folder_module
        from . import group as group_module

        self.adom = adom_module.DvmdbAdom(client)
        self.device = device_module.DvmdbDevice(client)
        self.folder = folder_module.DvmdbFolder(client)
        self.group = group_module.DvmdbGroup(client)

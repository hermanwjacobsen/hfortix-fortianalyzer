"""FortiAnalyzer del_ cmd API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import dev_list
    from . import device

__all__ = ["Del"]


class Del:
    """FortiAnalyzer del_ cmd API endpoints."""

    dev_list: "dev_list.DvmCmdDelDevList"
    device: "device.DvmCmdDelDevice"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Del namespace with JSON-RPC client."""
        from . import dev_list as dev_list_module
        from . import device as device_module

        self.dev_list = dev_list_module.DvmCmdDelDevList(client)
        self.device = device_module.DvmCmdDelDevice(client)

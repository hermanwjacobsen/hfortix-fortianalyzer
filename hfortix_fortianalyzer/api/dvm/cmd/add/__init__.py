"""FortiAnalyzer add cmd API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import dev_list
    from . import device

__all__ = ["Add"]


class Add:
    """FortiAnalyzer add cmd API endpoints."""

    dev_list: "dev_list.DvmCmdAddDevList"
    device: "device.DvmCmdAddDevice"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Add namespace with JSON-RPC client."""
        from . import dev_list as dev_list_module
        from . import device as device_module

        self.dev_list = dev_list_module.DvmCmdAddDevList(client)
        self.device = device_module.DvmCmdAddDevice(client)

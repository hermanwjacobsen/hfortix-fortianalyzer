"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .dev_list import DvmCmdAddDevList
    from .device import DvmCmdAddDevice

__all__ = ["Add"]


class Add:
    """Add endpoints."""

    dev_list: DvmCmdAddDevList
    device: DvmCmdAddDevice

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

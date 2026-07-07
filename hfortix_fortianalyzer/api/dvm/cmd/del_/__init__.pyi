"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .dev_list import DvmCmdDelDevList
    from .device import DvmCmdDelDevice

__all__ = ["Del"]


class Del:
    """Del endpoints."""

    dev_list: DvmCmdDelDevList
    device: DvmCmdDelDevice

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

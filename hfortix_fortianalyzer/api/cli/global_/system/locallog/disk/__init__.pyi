"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .filter import CliGlobalSystemLocallogDiskFilter
    from .setting import CliGlobalSystemLocallogDiskSetting

__all__ = ["Disk"]


class Disk:
    """Disk endpoints."""

    filter: CliGlobalSystemLocallogDiskFilter
    setting: CliGlobalSystemLocallogDiskSetting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

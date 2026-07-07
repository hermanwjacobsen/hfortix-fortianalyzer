"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .filter import CliGlobalSystemLocallogMemoryFilter
    from .setting import CliGlobalSystemLocallogMemorySetting

__all__ = ["Memory"]


class Memory:
    """Memory endpoints."""

    filter: CliGlobalSystemLocallogMemoryFilter
    setting: CliGlobalSystemLocallogMemorySetting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

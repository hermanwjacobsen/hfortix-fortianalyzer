"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .auto_cache import CliGlobalSystemFortiviewAutoCache
    from .setting import CliGlobalSystemFortiviewSetting

__all__ = ["Fortiview"]


class Fortiview:
    """Fortiview endpoints."""

    auto_cache: CliGlobalSystemFortiviewAutoCache
    setting: CliGlobalSystemFortiviewSetting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

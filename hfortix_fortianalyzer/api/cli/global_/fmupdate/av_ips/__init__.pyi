"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .advanced_log import CliGlobalFmupdateAvIpsAdvancedLog

__all__ = ["Avips"]


class Avips:
    """Avips endpoints."""

    advanced_log: CliGlobalFmupdateAvIpsAdvancedLog

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

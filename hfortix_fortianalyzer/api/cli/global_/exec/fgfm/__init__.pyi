"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .reclaim_dev_tunnel import CliGlobalExecFgfmReclaimDevTunnel

__all__ = ["Fgfm"]


class Fgfm:
    """Fgfm endpoints."""

    reclaim_dev_tunnel: CliGlobalExecFgfmReclaimDevTunnel

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

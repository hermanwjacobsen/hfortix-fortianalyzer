"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .private_server import CliGlobalFmupdateServerAccessPrioritiesPrivateServer

__all__ = ["CliGlobalFmupdateServerAccessPriorities"]


from ..server_access_priorities_base import CliGlobalFmupdateServerAccessPriorities as CliGlobalFmupdateServerAccessPrioritiesBase

class CliGlobalFmupdateServerAccessPriorities(CliGlobalFmupdateServerAccessPrioritiesBase):
    """CliGlobalFmupdateServerAccessPriorities endpoints."""

    private_server: CliGlobalFmupdateServerAccessPrioritiesPrivateServer

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

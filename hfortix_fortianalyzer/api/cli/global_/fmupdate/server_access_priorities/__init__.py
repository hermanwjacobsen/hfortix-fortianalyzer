"""FortiAnalyzer server_access_priorities fmupdate API endpoints."""

from __future__ import annotations

from ..server_access_priorities_base import CliGlobalFmupdateServerAccessPriorities as CliGlobalFmupdateServerAccessPrioritiesBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import private_server

__all__ = ["CliGlobalFmupdateServerAccessPriorities"]


class CliGlobalFmupdateServerAccessPriorities(CliGlobalFmupdateServerAccessPrioritiesBase):
    """FortiAnalyzer server_access_priorities fmupdate API endpoints."""

    private_server: "private_server.CliGlobalFmupdateServerAccessPrioritiesPrivateServer"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalFmupdateServerAccessPriorities with endpoint methods and child modules."""
        super().__init__(client)

        from . import private_server as private_server_module

        self.private_server = private_server_module.CliGlobalFmupdateServerAccessPrioritiesPrivateServer(client)

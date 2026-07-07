"""FortiAnalyzer dvm API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import cmd

__all__ = ["Dvm"]


class Dvm:
    """FortiAnalyzer dvm API endpoints."""

    cmd: "cmd.Cmd"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Dvm namespace with JSON-RPC client."""
        from . import cmd as cmd_module

        self.cmd = cmd_module.Cmd(client)

"""FortiAnalyzer rescan adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import history
    from . import run

__all__ = ["Rescan"]


class Rescan:
    """FortiAnalyzer rescan adom API endpoints."""

    history: "history.IocAdomRescanHistory"
    run: "run.IocAdomRescanRun"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Rescan namespace with JSON-RPC client."""
        from . import history as history_module
        from . import run as run_module

        self.history = history_module.IocAdomRescanHistory(client)
        self.run = run_module.IocAdomRescanRun(client)

"""FortiAnalyzer adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import run

__all__ = ["Adom"]


class Adom:
    """FortiAnalyzer adom API endpoints."""

    run: "run.FortiviewAdomRun"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Adom namespace with JSON-RPC client."""
        from . import run as run_module

        self.run = run_module.FortiviewAdomRun(client)

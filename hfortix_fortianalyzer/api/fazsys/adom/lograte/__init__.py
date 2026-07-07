"""FortiAnalyzer lograte adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import history

__all__ = ["Lograte"]


class Lograte:
    """FortiAnalyzer lograte adom API endpoints."""

    history: "history.FazsysAdomLograteHistory"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Lograte namespace with JSON-RPC client."""
        from . import history as history_module

        self.history = history_module.FazsysAdomLograteHistory(client)

"""FortiAnalyzer adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import events
    from . import rescan

__all__ = ["Adom"]


class Adom:
    """FortiAnalyzer adom API endpoints."""

    events: "events.Events"
    rescan: "rescan.Rescan"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Adom namespace with JSON-RPC client."""
        from . import events as events_module
        from . import rescan as rescan_module

        self.events = events_module.Events(client)
        self.rescan = rescan_module.Rescan(client)

"""FortiAnalyzer events adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ack

__all__ = ["Events"]


class Events:
    """FortiAnalyzer events adom API endpoints."""

    ack: "ack.IocAdomEventsAck"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Events namespace with JSON-RPC client."""
        from . import ack as ack_module

        self.ack = ack_module.IocAdomEventsAck(client)

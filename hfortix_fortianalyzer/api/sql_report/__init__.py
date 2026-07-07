"""FortiAnalyzer sql_report API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import layout
    from . import schedule

__all__ = ["Sqlreport"]


class Sqlreport:
    """FortiAnalyzer sql_report API endpoints."""

    layout: "layout.Layout"
    schedule: "schedule.Schedule"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Sqlreport namespace with JSON-RPC client."""
        from . import layout as layout_module
        from . import schedule as schedule_module

        self.layout = layout_module.Layout(client)
        self.schedule = schedule_module.Schedule(client)

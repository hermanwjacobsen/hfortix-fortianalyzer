"""FortiAnalyzer logsearch adom API endpoints."""

from __future__ import annotations

from ..logsearch_base import LogviewAdomLogsearch as LogviewAdomLogsearchBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import count

__all__ = ["LogviewAdomLogsearch"]


class LogviewAdomLogsearch(LogviewAdomLogsearchBase):
    """FortiAnalyzer logsearch adom API endpoints."""

    count: "count.LogviewAdomLogsearchCount"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize LogviewAdomLogsearch with endpoint methods and child modules."""
        super().__init__(client)

        from . import count as count_module

        self.count = count_module.LogviewAdomLogsearchCount(client)

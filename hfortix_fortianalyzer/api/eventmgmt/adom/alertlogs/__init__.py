"""FortiAnalyzer alertlogs adom API endpoints."""

from __future__ import annotations

from ..alertlogs_base import EventmgmtAdomAlertlogs as EventmgmtAdomAlertlogsBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import count

__all__ = ["EventmgmtAdomAlertlogs"]


class EventmgmtAdomAlertlogs(EventmgmtAdomAlertlogsBase):
    """FortiAnalyzer alertlogs adom API endpoints."""

    count: "count.EventmgmtAdomAlertlogsCount"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize EventmgmtAdomAlertlogs with endpoint methods and child modules."""
        super().__init__(client)

        from . import count as count_module

        self.count = count_module.EventmgmtAdomAlertlogsCount(client)

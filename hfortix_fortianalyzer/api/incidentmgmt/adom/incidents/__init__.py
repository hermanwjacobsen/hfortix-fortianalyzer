"""FortiAnalyzer incidents adom API endpoints."""

from __future__ import annotations

from ..incidents_base import IncidentmgmtAdomIncidents as IncidentmgmtAdomIncidentsBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import count

__all__ = ["IncidentmgmtAdomIncidents"]


class IncidentmgmtAdomIncidents(IncidentmgmtAdomIncidentsBase):
    """FortiAnalyzer incidents adom API endpoints."""

    count: "count.IncidentmgmtAdomIncidentsCount"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize IncidentmgmtAdomIncidents with endpoint methods and child modules."""
        super().__init__(client)

        from . import count as count_module

        self.count = count_module.IncidentmgmtAdomIncidentsCount(client)

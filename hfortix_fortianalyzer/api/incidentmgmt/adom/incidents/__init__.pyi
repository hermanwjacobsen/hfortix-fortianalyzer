"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .count import IncidentmgmtAdomIncidentsCount

__all__ = ["IncidentmgmtAdomIncidents"]


from ..incidents_base import IncidentmgmtAdomIncidents as IncidentmgmtAdomIncidentsBase

class IncidentmgmtAdomIncidents(IncidentmgmtAdomIncidentsBase):
    """IncidentmgmtAdomIncidents endpoints."""

    count: IncidentmgmtAdomIncidentsCount

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

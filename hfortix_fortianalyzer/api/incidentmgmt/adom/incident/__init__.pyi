"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .stats import IncidentmgmtAdomIncidentStats

__all__ = ["IncidentmgmtAdomIncident"]


from ..incident_base import IncidentmgmtAdomIncident as IncidentmgmtAdomIncidentBase

class IncidentmgmtAdomIncident(IncidentmgmtAdomIncidentBase):
    """IncidentmgmtAdomIncident endpoints."""

    stats: IncidentmgmtAdomIncidentStats

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

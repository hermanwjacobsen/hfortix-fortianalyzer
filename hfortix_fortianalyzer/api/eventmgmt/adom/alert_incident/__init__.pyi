"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .stats import EventmgmtAdomAlertIncidentStats

__all__ = ["Alertincident"]


class Alertincident:
    """Alertincident endpoints."""

    stats: EventmgmtAdomAlertIncidentStats

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .indicator import SoarAdomIncidentIndicator

__all__ = ["Incident"]


class Incident:
    """Incident endpoints."""

    indicator: SoarAdomIncidentIndicator

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

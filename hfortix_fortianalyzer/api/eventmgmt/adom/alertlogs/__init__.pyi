"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .count import EventmgmtAdomAlertlogsCount

__all__ = ["EventmgmtAdomAlertlogs"]


from ..alertlogs_base import EventmgmtAdomAlertlogs as EventmgmtAdomAlertlogsBase

class EventmgmtAdomAlertlogs(EventmgmtAdomAlertlogsBase):
    """EventmgmtAdomAlertlogs endpoints."""

    count: EventmgmtAdomAlertlogsCount

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

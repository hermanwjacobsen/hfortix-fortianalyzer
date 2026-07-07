"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ack import EventmgmtAdomAlertsAck
    from .assign import EventmgmtAdomAlertsAssign
    from .comment import EventmgmtAdomAlertsComment
    from .count import EventmgmtAdomAlertsCount
    from .export import EventmgmtAdomAlertsExport
    from .extra_details import EventmgmtAdomAlertsExtraDetails
    from .import_ import EventmgmtAdomAlertsImport
    from .read import EventmgmtAdomAlertsRead
    from .unack import EventmgmtAdomAlertsUnack

__all__ = ["EventmgmtAdomAlerts"]


from ..alerts_base import EventmgmtAdomAlerts as EventmgmtAdomAlertsBase

class EventmgmtAdomAlerts(EventmgmtAdomAlertsBase):
    """EventmgmtAdomAlerts endpoints."""

    ack: EventmgmtAdomAlertsAck
    assign: EventmgmtAdomAlertsAssign
    comment: EventmgmtAdomAlertsComment
    count: EventmgmtAdomAlertsCount
    export: EventmgmtAdomAlertsExport
    extra_details: EventmgmtAdomAlertsExtraDetails
    import_: EventmgmtAdomAlertsImport
    read: EventmgmtAdomAlertsRead
    unack: EventmgmtAdomAlertsUnack

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

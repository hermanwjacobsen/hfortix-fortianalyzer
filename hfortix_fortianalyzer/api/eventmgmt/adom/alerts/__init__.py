"""FortiAnalyzer alerts adom API endpoints."""

from __future__ import annotations

from ..alerts_base import EventmgmtAdomAlerts as EventmgmtAdomAlertsBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ack
    from . import assign
    from . import comment
    from . import count
    from . import export
    from . import extra_details
    from . import import_
    from . import read
    from . import unack

__all__ = ["EventmgmtAdomAlerts"]


class EventmgmtAdomAlerts(EventmgmtAdomAlertsBase):
    """FortiAnalyzer alerts adom API endpoints."""

    ack: "ack.EventmgmtAdomAlertsAck"
    assign: "assign.EventmgmtAdomAlertsAssign"
    comment: "comment.EventmgmtAdomAlertsComment"
    count: "count.EventmgmtAdomAlertsCount"
    export: "export.EventmgmtAdomAlertsExport"
    extra_details: "extra_details.EventmgmtAdomAlertsExtraDetails"
    import_: "import_.EventmgmtAdomAlertsImport"
    read: "read.EventmgmtAdomAlertsRead"
    unack: "unack.EventmgmtAdomAlertsUnack"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize EventmgmtAdomAlerts with endpoint methods and child modules."""
        super().__init__(client)

        from . import ack as ack_module
        from . import assign as assign_module
        from . import comment as comment_module
        from . import count as count_module
        from . import export as export_module
        from . import extra_details as extra_details_module
        from . import import_ as import__module
        from . import read as read_module
        from . import unack as unack_module

        self.ack = ack_module.EventmgmtAdomAlertsAck(client)
        self.assign = assign_module.EventmgmtAdomAlertsAssign(client)
        self.comment = comment_module.EventmgmtAdomAlertsComment(client)
        self.count = count_module.EventmgmtAdomAlertsCount(client)
        self.export = export_module.EventmgmtAdomAlertsExport(client)
        self.extra_details = extra_details_module.EventmgmtAdomAlertsExtraDetails(client)
        self.import_ = import__module.EventmgmtAdomAlertsImport(client)
        self.read = read_module.EventmgmtAdomAlertsRead(client)
        self.unack = unack_module.EventmgmtAdomAlertsUnack(client)

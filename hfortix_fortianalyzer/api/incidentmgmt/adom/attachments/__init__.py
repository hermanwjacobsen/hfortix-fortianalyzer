"""FortiAnalyzer attachments adom API endpoints."""

from __future__ import annotations

from ..attachments_base import IncidentmgmtAdomAttachments as IncidentmgmtAdomAttachmentsBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import count

__all__ = ["IncidentmgmtAdomAttachments"]


class IncidentmgmtAdomAttachments(IncidentmgmtAdomAttachmentsBase):
    """FortiAnalyzer attachments adom API endpoints."""

    count: "count.IncidentmgmtAdomAttachmentsCount"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize IncidentmgmtAdomAttachments with endpoint methods and child modules."""
        super().__init__(client)

        from . import count as count_module

        self.count = count_module.IncidentmgmtAdomAttachmentsCount(client)

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .count import IncidentmgmtAdomAttachmentsCount

__all__ = ["IncidentmgmtAdomAttachments"]


from ..attachments_base import IncidentmgmtAdomAttachments as IncidentmgmtAdomAttachmentsBase

class IncidentmgmtAdomAttachments(IncidentmgmtAdomAttachmentsBase):
    """IncidentmgmtAdomAttachments endpoints."""

    count: IncidentmgmtAdomAttachmentsCount

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

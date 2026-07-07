"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .attachment import IncidentmgmtAdomAttachment
    from .attachments import IncidentmgmtAdomAttachments
    from .epeu_history import IncidentmgmtAdomEpeuHistory
    from .incident import IncidentmgmtAdomIncident
    from .incidents import IncidentmgmtAdomIncidents

__all__ = ["Adom"]


class Adom:
    """Adom endpoints."""

    attachment: IncidentmgmtAdomAttachment
    attachments: IncidentmgmtAdomAttachments
    epeu_history: IncidentmgmtAdomEpeuHistory
    incident: IncidentmgmtAdomIncident
    incidents: IncidentmgmtAdomIncidents

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

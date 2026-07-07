"""FortiAnalyzer adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import attachment
    from . import attachments
    from . import epeu_history
    from . import incident
    from . import incidents

__all__ = ["Adom"]


class Adom:
    """FortiAnalyzer adom API endpoints."""

    attachment: "attachment.IncidentmgmtAdomAttachment"
    attachments: "attachments.IncidentmgmtAdomAttachments"
    epeu_history: "epeu_history.IncidentmgmtAdomEpeuHistory"
    incident: "incident.IncidentmgmtAdomIncident"
    incidents: "incidents.IncidentmgmtAdomIncidents"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Adom namespace with JSON-RPC client."""
        from . import attachment as attachment_module
        from . import attachments as attachments_module
        from . import epeu_history as epeu_history_module
        from . import incident as incident_module
        from . import incidents as incidents_module

        self.attachment = attachment_module.IncidentmgmtAdomAttachment(client)
        self.attachments = attachments_module.IncidentmgmtAdomAttachments(client)
        self.epeu_history = epeu_history_module.IncidentmgmtAdomEpeuHistory(client)
        self.incident = incident_module.IncidentmgmtAdomIncident(client)
        self.incidents = incidents_module.IncidentmgmtAdomIncidents(client)

"""FortiAnalyzer output config API endpoints."""

from __future__ import annotations

from ..output_base import ReportAdomConfigOutput as ReportAdomConfigOutputBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import email_recipients

__all__ = ["ReportAdomConfigOutput"]


class ReportAdomConfigOutput(ReportAdomConfigOutputBase):
    """FortiAnalyzer output config API endpoints."""

    email_recipients: "email_recipients.ReportAdomConfigOutputEmailRecipients"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize ReportAdomConfigOutput with endpoint methods and child modules."""
        super().__init__(client)

        from . import email_recipients as email_recipients_module

        self.email_recipients = email_recipients_module.ReportAdomConfigOutputEmailRecipients(client)

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .email_recipients import ReportAdomConfigOutputEmailRecipients

__all__ = ["ReportAdomConfigOutput"]


from ..output_base import ReportAdomConfigOutput as ReportAdomConfigOutputBase

class ReportAdomConfigOutput(ReportAdomConfigOutputBase):
    """ReportAdomConfigOutput endpoints."""

    email_recipients: ReportAdomConfigOutputEmailRecipients

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

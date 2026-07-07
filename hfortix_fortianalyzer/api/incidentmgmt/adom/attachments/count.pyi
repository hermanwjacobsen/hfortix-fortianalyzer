"""Type stubs for incidentmgmt.adom.attachments.count"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomAttachmentsCount:
    """FortiAnalyzer endpoint: incidentmgmt.adom.attachments.count"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        attachtype: Literal["alertevent", "log", "note", "logsearchfilter", "file", "report", "history", "sysnote", "enrichment"] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["IncidentmgmtAdomAttachmentsCount"]
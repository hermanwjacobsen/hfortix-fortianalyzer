"""Type stubs for incidentmgmt.adom.attachments"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomAttachments:
    """FortiAnalyzer endpoint: incidentmgmt.adom.attachments"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        attachments: list[dict[str, Any]],
        incid: str,
        apiver: int = 3,
        lastuser: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        attachids: list[float] | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        attachtype: Literal["alertevent", "log", "note", "logsearchfilter", "file", "report", "history", "sysnote", "enrichment"] | None = None,
        limit: float | None = None,
        offset: float | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["IncidentmgmtAdomAttachments"]
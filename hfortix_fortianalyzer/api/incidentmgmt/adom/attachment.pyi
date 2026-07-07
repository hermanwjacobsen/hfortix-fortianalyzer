"""Type stubs for incidentmgmt.adom.attachment"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomAttachment:
    """FortiAnalyzer endpoint: incidentmgmt.adom.attachment"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def update(
        self,
        attachid: str,
        adom: str,
        data: str,
        apiver: int = 3,
        attachsrc: Literal["manual", "playbook"] | None = None,
        attachsrcid: str | None = None,
        attachsrctrigger: str | None = None,
        lastrevision: float | None = None,
        lastuser: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["IncidentmgmtAdomAttachment"]
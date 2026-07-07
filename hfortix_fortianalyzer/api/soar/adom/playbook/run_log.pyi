"""Type stubs for soar.adom.playbook.run-log"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomPlaybookRunLog:
    """FortiAnalyzer endpoint: soar.adom.playbook.run-log"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        run_id: str,
        adom: str,
        apiver: int = 3,
        detail_on_error: Literal["true", "false"] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["SoarAdomPlaybookRunLog"]
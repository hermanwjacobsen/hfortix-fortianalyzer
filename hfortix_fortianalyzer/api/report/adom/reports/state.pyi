"""Type stubs for report.adom.reports.state"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomReportsState:
    """FortiAnalyzer endpoint: report.adom.reports.state"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        state: str,
        apiver: int = 3,
        sort_by: list[dict[str, Any]] | None = None,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None,
        title: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["ReportAdomReportsState"]
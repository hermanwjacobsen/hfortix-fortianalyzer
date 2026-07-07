"""Type stubs for report.adom.reports.data"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomReportsData:
    """FortiAnalyzer endpoint: report.adom.reports.data"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def delete(
        self,
        tid: str,
        adom: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        tid: str,
        adom: str,
        apiver: int = 3,
        data_type: str | None = None,
        format: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["ReportAdomReportsData"]
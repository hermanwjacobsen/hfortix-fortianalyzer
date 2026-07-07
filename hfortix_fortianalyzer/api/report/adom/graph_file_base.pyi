"""Type stubs for report.adom.graph-file"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomGraphFile:
    """FortiAnalyzer endpoint: report.adom.graph-file"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        data: str,
        file_name: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        file_name: list[str],
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        file_name: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["ReportAdomGraphFile"]
"""Type stubs for report.adom.graph-file.list"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomGraphFileList:
    """FortiAnalyzer endpoint: report.adom.graph-file.list"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        file_name: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["ReportAdomGraphFileList"]
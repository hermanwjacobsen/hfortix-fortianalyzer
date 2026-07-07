"""Type stubs for report.config.layout.folders"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportConfigLayoutFolders:
    """FortiAnalyzer endpoint: report.config.layout.folders"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["ReportConfigLayoutFolders"]
"""Type stubs for report.adom.config.layout-folder"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomConfigLayoutFolder:
    """FortiAnalyzer endpoint: report.adom.config.layout-folder"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["ReportAdomConfigLayoutFolder"]
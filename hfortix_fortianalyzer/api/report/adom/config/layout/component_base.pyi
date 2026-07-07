"""Type stubs for report.adom.config.layout.component"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomConfigLayoutComponent:
    """FortiAnalyzer endpoint: report.adom.config.layout.component"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        layout_id: str,
        adom: str,
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["ReportAdomConfigLayoutComponent"]
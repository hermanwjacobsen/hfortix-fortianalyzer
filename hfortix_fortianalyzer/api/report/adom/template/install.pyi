"""Type stubs for report.adom.template.install"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomTemplateInstall:
    """FortiAnalyzer endpoint: report.adom.template.install"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        language: str,
        apiver: int = 3,
        data: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["ReportAdomTemplateInstall"]
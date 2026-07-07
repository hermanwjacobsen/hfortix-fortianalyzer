"""Type stubs for report.adom.template.export"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomTemplateExport:
    """FortiAnalyzer endpoint: report.adom.template.export"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        dev_type: str | None = None,
        language: str | None = None,
        title: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["ReportAdomTemplateExport"]
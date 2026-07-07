"""Type stubs for report.template.delete"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportTemplateDelete:
    """FortiAnalyzer endpoint: report.template.delete"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        dev_type: str,
        language: str,
        apiver: int = 3,
        title: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["ReportTemplateDelete"]
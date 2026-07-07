"""Type stubs for report.adom.config.dataset.variable"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomConfigDatasetVariable:
    """FortiAnalyzer endpoint: report.adom.config.dataset.variable"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        dataset_name: str,
        adom: str,
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["ReportAdomConfigDatasetVariable"]
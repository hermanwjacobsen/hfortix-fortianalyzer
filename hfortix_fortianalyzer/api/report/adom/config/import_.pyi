"""Type stubs for report.adom.config.import"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomConfigImport:
    """FortiAnalyzer endpoint: report.adom.config.import"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        data: str,
        adoms: list[str] | None = None,
        apiver: int = 3,
        check_only: bool | None = None,
        conflict_option: Literal["skip", "replace", "fail"] | None = None,
        report_folder: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["ReportAdomConfigImport"]
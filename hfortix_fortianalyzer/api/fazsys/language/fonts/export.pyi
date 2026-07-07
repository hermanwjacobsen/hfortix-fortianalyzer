"""Type stubs for fazsys.language.fonts.export"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysLanguageFontsExport:
    """FortiAnalyzer endpoint: fazsys.language.fonts.export"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        apiver: int = 3,
        font: list[str] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["FazsysLanguageFontsExport"]
"""Type stubs for fazsys.language.fonts"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysLanguageFonts:
    """FortiAnalyzer endpoint: fazsys.language.fonts"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def delete(
        self,
        font_name: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["FazsysLanguageFonts"]
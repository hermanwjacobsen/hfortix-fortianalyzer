"""Type stubs for fazsys.language.translation-file.import"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysLanguageTranslationFileImport:
    """FortiAnalyzer endpoint: fazsys.language.translation-file.import"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        data: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["FazsysLanguageTranslationFileImport"]
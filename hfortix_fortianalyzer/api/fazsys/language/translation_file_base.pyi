"""Type stubs for fazsys.language.translation-file"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysLanguageTranslationFile:
    """FortiAnalyzer endpoint: fazsys.language.translation-file"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def delete(
        self,
        language_code: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["FazsysLanguageTranslationFile"]
"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .fonts import FazsysLanguageFonts
    from .translation_file import FazsysLanguageTranslationFile

__all__ = ["Language"]


class Language:
    """Language endpoints."""

    fonts: FazsysLanguageFonts
    translation_file: FazsysLanguageTranslationFile

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

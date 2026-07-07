"""FortiAnalyzer language API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import fonts
    from . import translation_file

__all__ = ["Language"]


class Language:
    """FortiAnalyzer language API endpoints."""

    fonts: "fonts.FazsysLanguageFonts"
    translation_file: "translation_file.FazsysLanguageTranslationFile"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Language namespace with JSON-RPC client."""
        from . import fonts as fonts_module
        from . import translation_file as translation_file_module

        self.fonts = fonts_module.FazsysLanguageFonts(client)
        self.translation_file = translation_file_module.FazsysLanguageTranslationFile(client)

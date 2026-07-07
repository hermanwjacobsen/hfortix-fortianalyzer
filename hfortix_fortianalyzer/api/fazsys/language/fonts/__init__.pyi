"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .export import FazsysLanguageFontsExport
    from .import_ import FazsysLanguageFontsImport
    from .list import FazsysLanguageFontsList

__all__ = ["FazsysLanguageFonts"]


from ..fonts_base import FazsysLanguageFonts as FazsysLanguageFontsBase

class FazsysLanguageFonts(FazsysLanguageFontsBase):
    """FazsysLanguageFonts endpoints."""

    export: FazsysLanguageFontsExport
    import_: FazsysLanguageFontsImport
    list: FazsysLanguageFontsList

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

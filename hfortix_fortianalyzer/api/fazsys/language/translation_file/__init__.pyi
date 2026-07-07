"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .export import FazsysLanguageTranslationFileExport
    from .import_ import FazsysLanguageTranslationFileImport
    from .list import FazsysLanguageTranslationFileList

__all__ = ["FazsysLanguageTranslationFile"]


from ..translation_file_base import FazsysLanguageTranslationFile as FazsysLanguageTranslationFileBase

class FazsysLanguageTranslationFile(FazsysLanguageTranslationFileBase):
    """FazsysLanguageTranslationFile endpoints."""

    export: FazsysLanguageTranslationFileExport
    import_: FazsysLanguageTranslationFileImport
    list: FazsysLanguageTranslationFileList

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

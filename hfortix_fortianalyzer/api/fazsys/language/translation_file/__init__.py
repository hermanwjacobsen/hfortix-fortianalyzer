"""FortiAnalyzer translation_file language API endpoints."""

from __future__ import annotations

from ..translation_file_base import FazsysLanguageTranslationFile as FazsysLanguageTranslationFileBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import export
    from . import import_
    from . import list

__all__ = ["FazsysLanguageTranslationFile"]


class FazsysLanguageTranslationFile(FazsysLanguageTranslationFileBase):
    """FortiAnalyzer translation_file language API endpoints."""

    export: "export.FazsysLanguageTranslationFileExport"
    import_: "import_.FazsysLanguageTranslationFileImport"
    list: "list.FazsysLanguageTranslationFileList"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize FazsysLanguageTranslationFile with endpoint methods and child modules."""
        super().__init__(client)

        from . import export as export_module
        from . import import_ as import__module
        from . import list as list_module

        self.export = export_module.FazsysLanguageTranslationFileExport(client)
        self.import_ = import__module.FazsysLanguageTranslationFileImport(client)
        self.list = list_module.FazsysLanguageTranslationFileList(client)

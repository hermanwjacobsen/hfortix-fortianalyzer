"""FortiAnalyzer fonts language API endpoints."""

from __future__ import annotations

from ..fonts_base import FazsysLanguageFonts as FazsysLanguageFontsBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import export
    from . import import_
    from . import list

__all__ = ["FazsysLanguageFonts"]


class FazsysLanguageFonts(FazsysLanguageFontsBase):
    """FortiAnalyzer fonts language API endpoints."""

    export: "export.FazsysLanguageFontsExport"
    import_: "import_.FazsysLanguageFontsImport"
    list: "list.FazsysLanguageFontsList"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize FazsysLanguageFonts with endpoint methods and child modules."""
        super().__init__(client)

        from . import export as export_module
        from . import import_ as import__module
        from . import list as list_module

        self.export = export_module.FazsysLanguageFontsExport(client)
        self.import_ = import__module.FazsysLanguageFontsImport(client)
        self.list = list_module.FazsysLanguageFontsList(client)

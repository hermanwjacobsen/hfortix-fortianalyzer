"""FortiAnalyzer template adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import export
    from . import install
    from . import language
    from . import list

__all__ = ["Template"]


class Template:
    """FortiAnalyzer template adom API endpoints."""

    export: "export.ReportAdomTemplateExport"
    install: "install.ReportAdomTemplateInstall"
    language: "language.ReportAdomTemplateLanguage"
    list: "list.ReportAdomTemplateList"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Template namespace with JSON-RPC client."""
        from . import export as export_module
        from . import install as install_module
        from . import language as language_module
        from . import list as list_module

        self.export = export_module.ReportAdomTemplateExport(client)
        self.install = install_module.ReportAdomTemplateInstall(client)
        self.language = language_module.ReportAdomTemplateLanguage(client)
        self.list = list_module.ReportAdomTemplateList(client)

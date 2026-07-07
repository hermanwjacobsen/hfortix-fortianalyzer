"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .export import ReportAdomTemplateExport
    from .install import ReportAdomTemplateInstall
    from .language import ReportAdomTemplateLanguage
    from .list import ReportAdomTemplateList

__all__ = ["Template"]


class Template:
    """Template endpoints."""

    export: ReportAdomTemplateExport
    install: ReportAdomTemplateInstall
    language: ReportAdomTemplateLanguage
    list: ReportAdomTemplateList

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

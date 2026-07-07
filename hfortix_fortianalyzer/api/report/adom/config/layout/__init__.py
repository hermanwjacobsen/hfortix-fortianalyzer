"""FortiAnalyzer layout config API endpoints."""

from __future__ import annotations

from ..layout_base import ReportAdomConfigLayout as ReportAdomConfigLayoutBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import component
    from . import footer
    from . import header

__all__ = ["ReportAdomConfigLayout"]


class ReportAdomConfigLayout(ReportAdomConfigLayoutBase):
    """FortiAnalyzer layout config API endpoints."""

    component: "component.ReportAdomConfigLayoutComponent"
    footer: "footer.ReportAdomConfigLayoutFooter"
    header: "header.ReportAdomConfigLayoutHeader"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize ReportAdomConfigLayout with endpoint methods and child modules."""
        super().__init__(client)

        from . import component as component_module
        from . import footer as footer_module
        from . import header as header_module

        self.component = component_module.ReportAdomConfigLayoutComponent(client)
        self.footer = footer_module.ReportAdomConfigLayoutFooter(client)
        self.header = header_module.ReportAdomConfigLayoutHeader(client)

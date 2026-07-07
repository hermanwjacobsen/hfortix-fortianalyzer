"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .component import ReportAdomConfigLayoutComponent
    from .footer import ReportAdomConfigLayoutFooter
    from .header import ReportAdomConfigLayoutHeader

__all__ = ["ReportAdomConfigLayout"]


from ..layout_base import ReportAdomConfigLayout as ReportAdomConfigLayoutBase

class ReportAdomConfigLayout(ReportAdomConfigLayoutBase):
    """ReportAdomConfigLayout endpoints."""

    component: ReportAdomConfigLayoutComponent
    footer: ReportAdomConfigLayoutFooter
    header: ReportAdomConfigLayoutHeader

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

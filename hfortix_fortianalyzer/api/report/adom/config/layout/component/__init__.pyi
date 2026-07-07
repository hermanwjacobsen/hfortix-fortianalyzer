"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .variable import ReportAdomConfigLayoutComponentVariable

__all__ = ["ReportAdomConfigLayoutComponent"]


from ..component_base import ReportAdomConfigLayoutComponent as ReportAdomConfigLayoutComponentBase

class ReportAdomConfigLayoutComponent(ReportAdomConfigLayoutComponentBase):
    """ReportAdomConfigLayoutComponent endpoints."""

    variable: ReportAdomConfigLayoutComponentVariable

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

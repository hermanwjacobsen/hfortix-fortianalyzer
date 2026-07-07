"""FortiAnalyzer component layout API endpoints."""

from __future__ import annotations

from ..component_base import ReportAdomConfigLayoutComponent as ReportAdomConfigLayoutComponentBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import variable

__all__ = ["ReportAdomConfigLayoutComponent"]


class ReportAdomConfigLayoutComponent(ReportAdomConfigLayoutComponentBase):
    """FortiAnalyzer component layout API endpoints."""

    variable: "variable.ReportAdomConfigLayoutComponentVariable"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize ReportAdomConfigLayoutComponent with endpoint methods and child modules."""
        super().__init__(client)

        from . import variable as variable_module

        self.variable = variable_module.ReportAdomConfigLayoutComponentVariable(client)

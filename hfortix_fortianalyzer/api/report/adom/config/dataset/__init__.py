"""FortiAnalyzer dataset config API endpoints."""

from __future__ import annotations

from ..dataset_base import ReportAdomConfigDataset as ReportAdomConfigDatasetBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import variable

__all__ = ["ReportAdomConfigDataset"]


class ReportAdomConfigDataset(ReportAdomConfigDatasetBase):
    """FortiAnalyzer dataset config API endpoints."""

    variable: "variable.ReportAdomConfigDatasetVariable"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize ReportAdomConfigDataset with endpoint methods and child modules."""
        super().__init__(client)

        from . import variable as variable_module

        self.variable = variable_module.ReportAdomConfigDatasetVariable(client)

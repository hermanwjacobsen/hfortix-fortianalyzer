"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .variable import ReportAdomConfigDatasetVariable

__all__ = ["ReportAdomConfigDataset"]


from ..dataset_base import ReportAdomConfigDataset as ReportAdomConfigDatasetBase

class ReportAdomConfigDataset(ReportAdomConfigDatasetBase):
    """ReportAdomConfigDataset endpoints."""

    variable: ReportAdomConfigDatasetVariable

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

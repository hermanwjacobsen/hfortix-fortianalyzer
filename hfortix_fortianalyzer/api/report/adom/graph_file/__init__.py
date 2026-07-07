"""FortiAnalyzer graph_file adom API endpoints."""

from __future__ import annotations

from ..graph_file_base import ReportAdomGraphFile as ReportAdomGraphFileBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import data
    from . import list

__all__ = ["ReportAdomGraphFile"]


class ReportAdomGraphFile(ReportAdomGraphFileBase):
    """FortiAnalyzer graph_file adom API endpoints."""

    data: "data.ReportAdomGraphFileData"
    list: "list.ReportAdomGraphFileList"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize ReportAdomGraphFile with endpoint methods and child modules."""
        super().__init__(client)

        from . import data as data_module
        from . import list as list_module

        self.data = data_module.ReportAdomGraphFileData(client)
        self.list = list_module.ReportAdomGraphFileList(client)

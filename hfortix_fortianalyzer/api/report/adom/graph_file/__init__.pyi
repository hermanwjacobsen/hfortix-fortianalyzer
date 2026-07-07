"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .data import ReportAdomGraphFileData
    from .list import ReportAdomGraphFileList

__all__ = ["ReportAdomGraphFile"]


from ..graph_file_base import ReportAdomGraphFile as ReportAdomGraphFileBase

class ReportAdomGraphFile(ReportAdomGraphFileBase):
    """ReportAdomGraphFile endpoints."""

    data: ReportAdomGraphFileData
    list: ReportAdomGraphFileList

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

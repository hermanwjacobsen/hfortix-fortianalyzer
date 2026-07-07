"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .count import LogviewAdomLogsearchCount

__all__ = ["LogviewAdomLogsearch"]


from ..logsearch_base import LogviewAdomLogsearch as LogviewAdomLogsearchBase

class LogviewAdomLogsearch(LogviewAdomLogsearchBase):
    """LogviewAdomLogsearch endpoints."""

    count: LogviewAdomLogsearchCount

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .status import SysHaStatus

__all__ = ["HA"]


class HA:
    """HA endpoints."""

    status: SysHaStatus

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

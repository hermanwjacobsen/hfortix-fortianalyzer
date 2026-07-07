"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .hosts import CliGlobalSystemSnmpCommunityHosts
    from .hosts6 import CliGlobalSystemSnmpCommunityHosts6

__all__ = ["CliGlobalSystemSnmpCommunity"]


from ..community_base import CliGlobalSystemSnmpCommunity as CliGlobalSystemSnmpCommunityBase

class CliGlobalSystemSnmpCommunity(CliGlobalSystemSnmpCommunityBase):
    """CliGlobalSystemSnmpCommunity endpoints."""

    hosts: CliGlobalSystemSnmpCommunityHosts
    hosts6: CliGlobalSystemSnmpCommunityHosts6

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

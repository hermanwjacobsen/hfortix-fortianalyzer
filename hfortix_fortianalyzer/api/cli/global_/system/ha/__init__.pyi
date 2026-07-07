"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .peer import CliGlobalSystemHaPeer
    from .private_peer import CliGlobalSystemHaPrivatePeer
    from .vip import CliGlobalSystemHaVip

__all__ = ["CliGlobalSystemHa"]


from ..ha_base import CliGlobalSystemHa as CliGlobalSystemHaBase

class CliGlobalSystemHa(CliGlobalSystemHaBase):
    """CliGlobalSystemHa endpoints."""

    peer: CliGlobalSystemHaPeer
    private_peer: CliGlobalSystemHaPrivatePeer
    vip: CliGlobalSystemHaVip

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

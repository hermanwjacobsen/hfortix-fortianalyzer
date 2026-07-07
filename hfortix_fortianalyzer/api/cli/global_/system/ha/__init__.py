"""FortiAnalyzer ha system API endpoints."""

from __future__ import annotations

from ..ha_base import CliGlobalSystemHa as CliGlobalSystemHaBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import peer
    from . import private_peer
    from . import vip

__all__ = ["CliGlobalSystemHa"]


class CliGlobalSystemHa(CliGlobalSystemHaBase):
    """FortiAnalyzer ha system API endpoints."""

    peer: "peer.CliGlobalSystemHaPeer"
    private_peer: "private_peer.CliGlobalSystemHaPrivatePeer"
    vip: "vip.CliGlobalSystemHaVip"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemHa with endpoint methods and child modules."""
        super().__init__(client)

        from . import peer as peer_module
        from . import private_peer as private_peer_module
        from . import vip as vip_module

        self.peer = peer_module.CliGlobalSystemHaPeer(client)
        self.private_peer = private_peer_module.CliGlobalSystemHaPrivatePeer(client)
        self.vip = vip_module.CliGlobalSystemHaVip(client)

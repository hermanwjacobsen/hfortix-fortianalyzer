"""FortiAnalyzer indicator adom API endpoints."""

from __future__ import annotations

from ..indicator_base import SoarAdomIndicator as SoarAdomIndicatorBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import block
    from . import enrichment
    from . import unblock

__all__ = ["SoarAdomIndicator"]


class SoarAdomIndicator(SoarAdomIndicatorBase):
    """FortiAnalyzer indicator adom API endpoints."""

    block: "block.SoarAdomIndicatorBlock"
    enrichment: "enrichment.SoarAdomIndicatorEnrichment"
    unblock: "unblock.SoarAdomIndicatorUnblock"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize SoarAdomIndicator with endpoint methods and child modules."""
        super().__init__(client)

        from . import block as block_module
        from . import enrichment as enrichment_module
        from . import unblock as unblock_module

        self.block = block_module.SoarAdomIndicatorBlock(client)
        self.enrichment = enrichment_module.SoarAdomIndicatorEnrichment(client)
        self.unblock = unblock_module.SoarAdomIndicatorUnblock(client)

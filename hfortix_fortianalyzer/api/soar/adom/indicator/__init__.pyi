"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .block import SoarAdomIndicatorBlock
    from .enrichment import SoarAdomIndicatorEnrichment
    from .unblock import SoarAdomIndicatorUnblock

__all__ = ["SoarAdomIndicator"]


from ..indicator_base import SoarAdomIndicator as SoarAdomIndicatorBase

class SoarAdomIndicator(SoarAdomIndicatorBase):
    """SoarAdomIndicator endpoints."""

    block: SoarAdomIndicatorBlock
    enrichment: SoarAdomIndicatorEnrichment
    unblock: SoarAdomIndicatorUnblock

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .events import Events
    from .rescan import Rescan

__all__ = ["Adom"]


class Adom:
    """Adom endpoints."""

    events: Events
    rescan: Rescan

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

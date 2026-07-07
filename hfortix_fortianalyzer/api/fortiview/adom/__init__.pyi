"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .run import FortiviewAdomRun

__all__ = ["Adom"]


class Adom:
    """Adom endpoints."""

    run: FortiviewAdomRun

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

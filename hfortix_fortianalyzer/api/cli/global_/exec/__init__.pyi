"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .fgfm import Fgfm

__all__ = ["Exec"]


class Exec:
    """Exec endpoints."""

    fgfm: Fgfm

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

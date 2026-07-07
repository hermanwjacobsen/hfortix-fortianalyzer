"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .cmd import Cmd

__all__ = ["Dvm"]


class Dvm:
    """Dvm endpoints."""

    cmd: Cmd

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

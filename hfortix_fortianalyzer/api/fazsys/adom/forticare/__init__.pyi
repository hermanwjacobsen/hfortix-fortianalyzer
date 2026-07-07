"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .licinfo import FazsysAdomForticareLicinfo

__all__ = ["Forticare"]


class Forticare:
    """Forticare endpoints."""

    licinfo: FazsysAdomForticareLicinfo

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

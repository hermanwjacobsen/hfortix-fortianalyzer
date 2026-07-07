"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .adom import Adom
    from .pcapfile import LogviewPcapfile

__all__ = ["Logview"]


class Logview:
    """Logview endpoints."""

    adom: Adom
    pcapfile: LogviewPcapfile

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

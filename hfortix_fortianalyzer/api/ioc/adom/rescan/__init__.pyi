"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .history import IocAdomRescanHistory
    from .run import IocAdomRescanRun

__all__ = ["Rescan"]


class Rescan:
    """Rescan endpoints."""

    history: IocAdomRescanHistory
    run: IocAdomRescanRun

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

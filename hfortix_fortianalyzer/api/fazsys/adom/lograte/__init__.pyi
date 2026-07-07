"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .history import FazsysAdomLograteHistory

__all__ = ["Lograte"]


class Lograte:
    """Lograte endpoints."""

    history: FazsysAdomLograteHistory

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

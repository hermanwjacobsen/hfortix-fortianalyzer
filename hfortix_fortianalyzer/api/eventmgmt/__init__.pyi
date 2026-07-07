"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .adom import Adom

__all__ = ["Eventmgmt"]


class Eventmgmt:
    """Eventmgmt endpoints."""

    adom: Adom

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

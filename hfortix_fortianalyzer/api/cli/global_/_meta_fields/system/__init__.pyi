"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .admin import Admin

__all__ = ["System"]


class System:
    """System endpoints."""

    admin: Admin

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

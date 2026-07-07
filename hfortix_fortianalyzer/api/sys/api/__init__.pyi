"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .sdnconnector import SysApiSdnconnector

__all__ = ["API"]


class API:
    """API endpoints."""

    sdnconnector: SysApiSdnconnector

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

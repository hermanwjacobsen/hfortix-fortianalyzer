"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .json import SysProxyJson

__all__ = ["Proxy"]


class Proxy:
    """Proxy endpoints."""

    json: SysProxyJson

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

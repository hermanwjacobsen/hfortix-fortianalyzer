"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .adom import Adom
    from .license import License

__all__ = ["Ioc"]


class Ioc:
    """Ioc endpoints."""

    adom: Adom
    license: License

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

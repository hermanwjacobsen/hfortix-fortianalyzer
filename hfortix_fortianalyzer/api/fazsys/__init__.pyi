"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .adom import Adom
    from .language import Language
    from .monitor import Monitor
    from .storage_info import FazsysStorageInfo

__all__ = ["Fazsys"]


class Fazsys:
    """Fazsys endpoints."""

    adom: Adom
    language: Language
    monitor: Monitor
    storage_info: FazsysStorageInfo

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

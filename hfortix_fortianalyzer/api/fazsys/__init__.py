"""FortiAnalyzer fazsys API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom
    from . import language
    from . import monitor
    from . import storage_info

__all__ = ["Fazsys"]


class Fazsys:
    """FortiAnalyzer fazsys API endpoints."""

    adom: "adom.Adom"
    language: "language.Language"
    monitor: "monitor.Monitor"
    storage_info: "storage_info.FazsysStorageInfo"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Fazsys namespace with JSON-RPC client."""
        from . import adom as adom_module
        from . import language as language_module
        from . import monitor as monitor_module
        from . import storage_info as storage_info_module

        self.adom = adom_module.Adom(client)
        self.language = language_module.Language(client)
        self.monitor = monitor_module.Monitor(client)
        self.storage_info = storage_info_module.FazsysStorageInfo(client)

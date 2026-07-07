"""FortiAnalyzer ioc API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom
    from . import license

__all__ = ["Ioc"]


class Ioc:
    """FortiAnalyzer ioc API endpoints."""

    adom: "adom.Adom"
    license: "license.License"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Ioc namespace with JSON-RPC client."""
        from . import adom as adom_module
        from . import license as license_module

        self.adom = adom_module.Adom(client)
        self.license = license_module.License(client)

"""FortiAnalyzer logview API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom
    from . import pcapfile

__all__ = ["Logview"]


class Logview:
    """FortiAnalyzer logview API endpoints."""

    adom: "adom.Adom"
    pcapfile: "pcapfile.LogviewPcapfile"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Logview namespace with JSON-RPC client."""
        from . import adom as adom_module
        from . import pcapfile as pcapfile_module

        self.adom = adom_module.Adom(client)
        self.pcapfile = pcapfile_module.LogviewPcapfile(client)

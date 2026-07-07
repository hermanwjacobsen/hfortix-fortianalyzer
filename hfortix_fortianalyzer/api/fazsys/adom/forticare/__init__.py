"""FortiAnalyzer forticare adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import licinfo

__all__ = ["Forticare"]


class Forticare:
    """FortiAnalyzer forticare adom API endpoints."""

    licinfo: "licinfo.FazsysAdomForticareLicinfo"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Forticare namespace with JSON-RPC client."""
        from . import licinfo as licinfo_module

        self.licinfo = licinfo_module.FazsysAdomForticareLicinfo(client)

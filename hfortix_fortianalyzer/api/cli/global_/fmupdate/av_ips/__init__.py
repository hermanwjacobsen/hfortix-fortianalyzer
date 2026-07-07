"""FortiAnalyzer av_ips fmupdate API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import advanced_log

__all__ = ["Avips"]


class Avips:
    """FortiAnalyzer av_ips fmupdate API endpoints."""

    advanced_log: "advanced_log.CliGlobalFmupdateAvIpsAdvancedLog"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Avips namespace with JSON-RPC client."""
        from . import advanced_log as advanced_log_module

        self.advanced_log = advanced_log_module.CliGlobalFmupdateAvIpsAdvancedLog(client)

"""FortiAnalyzer analyzer fmupdate API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import virusreport

__all__ = ["Analyzer"]


class Analyzer:
    """FortiAnalyzer analyzer fmupdate API endpoints."""

    virusreport: "virusreport.CliGlobalFmupdateAnalyzerVirusreport"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Analyzer namespace with JSON-RPC client."""
        from . import virusreport as virusreport_module

        self.virusreport = virusreport_module.CliGlobalFmupdateAnalyzerVirusreport(client)

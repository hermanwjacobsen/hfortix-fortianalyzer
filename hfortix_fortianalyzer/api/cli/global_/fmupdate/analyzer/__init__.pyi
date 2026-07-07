"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .virusreport import CliGlobalFmupdateAnalyzerVirusreport

__all__ = ["Analyzer"]


class Analyzer:
    """Analyzer endpoints."""

    virusreport: CliGlobalFmupdateAnalyzerVirusreport

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

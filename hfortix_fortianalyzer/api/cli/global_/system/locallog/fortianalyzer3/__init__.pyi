"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .filter import CliGlobalSystemLocallogFortianalyzer3Filter
    from .setting import CliGlobalSystemLocallogFortianalyzer3Setting

__all__ = ["Fortianalyzer3"]


class Fortianalyzer3:
    """Fortianalyzer3 endpoints."""

    filter: CliGlobalSystemLocallogFortianalyzer3Filter
    setting: CliGlobalSystemLocallogFortianalyzer3Setting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

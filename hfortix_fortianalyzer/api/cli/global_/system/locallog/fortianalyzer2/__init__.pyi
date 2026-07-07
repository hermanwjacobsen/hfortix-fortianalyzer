"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .filter import CliGlobalSystemLocallogFortianalyzer2Filter
    from .setting import CliGlobalSystemLocallogFortianalyzer2Setting

__all__ = ["Fortianalyzer2"]


class Fortianalyzer2:
    """Fortianalyzer2 endpoints."""

    filter: CliGlobalSystemLocallogFortianalyzer2Filter
    setting: CliGlobalSystemLocallogFortianalyzer2Setting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

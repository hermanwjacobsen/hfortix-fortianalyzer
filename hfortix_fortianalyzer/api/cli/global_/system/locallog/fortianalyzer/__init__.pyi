"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .filter import CliGlobalSystemLocallogFortianalyzerFilter
    from .setting import CliGlobalSystemLocallogFortianalyzerSetting

__all__ = ["Fortianalyzer"]


class Fortianalyzer:
    """Fortianalyzer endpoints."""

    filter: CliGlobalSystemLocallogFortianalyzerFilter
    setting: CliGlobalSystemLocallogFortianalyzerSetting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

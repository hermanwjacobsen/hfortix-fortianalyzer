"""FortiAnalyzer fortianalyzer3 locallog API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import filter
    from . import setting

__all__ = ["Fortianalyzer3"]


class Fortianalyzer3:
    """FortiAnalyzer fortianalyzer3 locallog API endpoints."""

    filter: "filter.CliGlobalSystemLocallogFortianalyzer3Filter"
    setting: "setting.CliGlobalSystemLocallogFortianalyzer3Setting"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Fortianalyzer3 namespace with JSON-RPC client."""
        from . import filter as filter_module
        from . import setting as setting_module

        self.filter = filter_module.CliGlobalSystemLocallogFortianalyzer3Filter(client)
        self.setting = setting_module.CliGlobalSystemLocallogFortianalyzer3Setting(client)

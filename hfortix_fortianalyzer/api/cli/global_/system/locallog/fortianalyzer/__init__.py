"""FortiAnalyzer fortianalyzer locallog API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import filter
    from . import setting

__all__ = ["Fortianalyzer"]


class Fortianalyzer:
    """FortiAnalyzer fortianalyzer locallog API endpoints."""

    filter: "filter.CliGlobalSystemLocallogFortianalyzerFilter"
    setting: "setting.CliGlobalSystemLocallogFortianalyzerSetting"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Fortianalyzer namespace with JSON-RPC client."""
        from . import filter as filter_module
        from . import setting as setting_module

        self.filter = filter_module.CliGlobalSystemLocallogFortianalyzerFilter(client)
        self.setting = setting_module.CliGlobalSystemLocallogFortianalyzerSetting(client)

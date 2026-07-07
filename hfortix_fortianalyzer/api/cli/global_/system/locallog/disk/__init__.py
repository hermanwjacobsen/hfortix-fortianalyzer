"""FortiAnalyzer disk locallog API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import filter
    from . import setting

__all__ = ["Disk"]


class Disk:
    """FortiAnalyzer disk locallog API endpoints."""

    filter: "filter.CliGlobalSystemLocallogDiskFilter"
    setting: "setting.CliGlobalSystemLocallogDiskSetting"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Disk namespace with JSON-RPC client."""
        from . import filter as filter_module
        from . import setting as setting_module

        self.filter = filter_module.CliGlobalSystemLocallogDiskFilter(client)
        self.setting = setting_module.CliGlobalSystemLocallogDiskSetting(client)

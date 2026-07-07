"""FortiAnalyzer fortiview system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import auto_cache
    from . import setting

__all__ = ["Fortiview"]


class Fortiview:
    """FortiAnalyzer fortiview system API endpoints."""

    auto_cache: "auto_cache.CliGlobalSystemFortiviewAutoCache"
    setting: "setting.CliGlobalSystemFortiviewSetting"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Fortiview namespace with JSON-RPC client."""
        from . import auto_cache as auto_cache_module
        from . import setting as setting_module

        self.auto_cache = auto_cache_module.CliGlobalSystemFortiviewAutoCache(client)
        self.setting = setting_module.CliGlobalSystemFortiviewSetting(client)

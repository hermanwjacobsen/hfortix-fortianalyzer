"""FortiAnalyzer report system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import auto_cache
    from . import est_browse_time
    from . import group
    from . import setting

__all__ = ["Report"]


class Report:
    """FortiAnalyzer report system API endpoints."""

    auto_cache: "auto_cache.CliGlobalSystemReportAutoCache"
    est_browse_time: "est_browse_time.CliGlobalSystemReportEstBrowseTime"
    group: "group.CliGlobalSystemReportGroup"
    setting: "setting.CliGlobalSystemReportSetting"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Report namespace with JSON-RPC client."""
        from . import auto_cache as auto_cache_module
        from . import est_browse_time as est_browse_time_module
        from . import group as group_module
        from . import setting as setting_module

        self.auto_cache = auto_cache_module.CliGlobalSystemReportAutoCache(client)
        self.est_browse_time = est_browse_time_module.CliGlobalSystemReportEstBrowseTime(client)
        self.group = group_module.CliGlobalSystemReportGroup(client)
        self.setting = setting_module.CliGlobalSystemReportSetting(client)

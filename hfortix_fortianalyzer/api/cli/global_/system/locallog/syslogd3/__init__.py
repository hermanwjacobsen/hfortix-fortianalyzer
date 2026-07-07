"""FortiAnalyzer syslogd3 locallog API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import filter
    from . import setting

__all__ = ["Syslogd3"]


class Syslogd3:
    """FortiAnalyzer syslogd3 locallog API endpoints."""

    filter: "filter.CliGlobalSystemLocallogSyslogd3Filter"
    setting: "setting.CliGlobalSystemLocallogSyslogd3Setting"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Syslogd3 namespace with JSON-RPC client."""
        from . import filter as filter_module
        from . import setting as setting_module

        self.filter = filter_module.CliGlobalSystemLocallogSyslogd3Filter(client)
        self.setting = setting_module.CliGlobalSystemLocallogSyslogd3Setting(client)

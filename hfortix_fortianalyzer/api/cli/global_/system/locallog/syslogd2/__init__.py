"""FortiAnalyzer syslogd2 locallog API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import filter
    from . import setting

__all__ = ["Syslogd2"]


class Syslogd2:
    """FortiAnalyzer syslogd2 locallog API endpoints."""

    filter: "filter.CliGlobalSystemLocallogSyslogd2Filter"
    setting: "setting.CliGlobalSystemLocallogSyslogd2Setting"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Syslogd2 namespace with JSON-RPC client."""
        from . import filter as filter_module
        from . import setting as setting_module

        self.filter = filter_module.CliGlobalSystemLocallogSyslogd2Filter(client)
        self.setting = setting_module.CliGlobalSystemLocallogSyslogd2Setting(client)

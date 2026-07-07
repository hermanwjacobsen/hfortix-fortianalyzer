"""FortiAnalyzer tacacs_accounting locallog API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import filter
    from . import setting

__all__ = ["Tacacsaccounting"]


class Tacacsaccounting:
    """FortiAnalyzer tacacs_accounting locallog API endpoints."""

    filter: "filter.CliGlobalSystemLocallogTacacsAccountingFilter"
    setting: "setting.CliGlobalSystemLocallogTacacsAccountingSetting"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Tacacsaccounting namespace with JSON-RPC client."""
        from . import filter as filter_module
        from . import setting as setting_module

        self.filter = filter_module.CliGlobalSystemLocallogTacacsAccountingFilter(client)
        self.setting = setting_module.CliGlobalSystemLocallogTacacsAccountingSetting(client)

"""FortiAnalyzer client_profile log_fetch API endpoints."""

from __future__ import annotations

from ..client_profile_base import CliGlobalSystemLogFetchClientProfile as CliGlobalSystemLogFetchClientProfileBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import device_filter
    from . import log_filter

__all__ = ["CliGlobalSystemLogFetchClientProfile"]


class CliGlobalSystemLogFetchClientProfile(CliGlobalSystemLogFetchClientProfileBase):
    """FortiAnalyzer client_profile log_fetch API endpoints."""

    device_filter: "device_filter.CliGlobalSystemLogFetchClientProfileDeviceFilter"
    log_filter: "log_filter.CliGlobalSystemLogFetchClientProfileLogFilter"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemLogFetchClientProfile with endpoint methods and child modules."""
        super().__init__(client)

        from . import device_filter as device_filter_module
        from . import log_filter as log_filter_module

        self.device_filter = device_filter_module.CliGlobalSystemLogFetchClientProfileDeviceFilter(client)
        self.log_filter = log_filter_module.CliGlobalSystemLogFetchClientProfileLogFilter(client)

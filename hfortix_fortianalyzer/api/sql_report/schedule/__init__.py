"""FortiAnalyzer schedule API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import devices
    from . import soc_cust_filters

__all__ = ["Schedule"]


class Schedule:
    """FortiAnalyzer schedule API endpoints."""

    devices: "devices.Devices"
    soc_cust_filters: "soc_cust_filters.SqlReportScheduleSocCustFilters"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Schedule namespace with JSON-RPC client."""
        from . import devices as devices_module
        from . import soc_cust_filters as soc_cust_filters_module

        self.devices = devices_module.Devices(client)
        self.soc_cust_filters = soc_cust_filters_module.SqlReportScheduleSocCustFilters(client)

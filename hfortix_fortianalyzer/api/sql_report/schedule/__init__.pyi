"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .devices import Devices
    from .soc_cust_filters import SqlReportScheduleSocCustFilters

__all__ = ["Schedule"]


class Schedule:
    """Schedule endpoints."""

    devices: Devices
    soc_cust_filters: SqlReportScheduleSocCustFilters

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

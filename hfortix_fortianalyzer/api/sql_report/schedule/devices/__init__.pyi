"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .interfaces import SqlReportScheduleDevicesInterfaces

__all__ = ["Devices"]


class Devices:
    """Devices endpoints."""

    interfaces: SqlReportScheduleDevicesInterfaces

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

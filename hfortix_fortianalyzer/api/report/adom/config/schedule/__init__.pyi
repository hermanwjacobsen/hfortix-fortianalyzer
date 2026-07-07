"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .address_filter import ReportAdomConfigScheduleAddressFilter
    from .devices import ReportAdomConfigScheduleDevices
    from .filter import ReportAdomConfigScheduleFilter
    from .report_layout import ReportAdomConfigScheduleReportLayout

__all__ = ["ReportAdomConfigSchedule"]


from ..schedule_base import ReportAdomConfigSchedule as ReportAdomConfigScheduleBase

class ReportAdomConfigSchedule(ReportAdomConfigScheduleBase):
    """ReportAdomConfigSchedule endpoints."""

    address_filter: ReportAdomConfigScheduleAddressFilter
    devices: ReportAdomConfigScheduleDevices
    filter: ReportAdomConfigScheduleFilter
    report_layout: ReportAdomConfigScheduleReportLayout

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

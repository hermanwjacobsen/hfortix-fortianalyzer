"""FortiAnalyzer schedule config API endpoints."""

from __future__ import annotations

from ..schedule_base import ReportAdomConfigSchedule as ReportAdomConfigScheduleBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import address_filter
    from . import devices
    from . import filter
    from . import report_layout

__all__ = ["ReportAdomConfigSchedule"]


class ReportAdomConfigSchedule(ReportAdomConfigScheduleBase):
    """FortiAnalyzer schedule config API endpoints."""

    address_filter: "address_filter.ReportAdomConfigScheduleAddressFilter"
    devices: "devices.ReportAdomConfigScheduleDevices"
    filter: "filter.ReportAdomConfigScheduleFilter"
    report_layout: "report_layout.ReportAdomConfigScheduleReportLayout"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize ReportAdomConfigSchedule with endpoint methods and child modules."""
        super().__init__(client)

        from . import address_filter as address_filter_module
        from . import devices as devices_module
        from . import filter as filter_module
        from . import report_layout as report_layout_module

        self.address_filter = address_filter_module.ReportAdomConfigScheduleAddressFilter(client)
        self.devices = devices_module.ReportAdomConfigScheduleDevices(client)
        self.filter = filter_module.ReportAdomConfigScheduleFilter(client)
        self.report_layout = report_layout_module.ReportAdomConfigScheduleReportLayout(client)

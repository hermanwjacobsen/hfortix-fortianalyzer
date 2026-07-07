"""FortiAnalyzer group report API endpoints."""

from __future__ import annotations

from ..group_base import CliGlobalSystemReportGroup as CliGlobalSystemReportGroupBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import chart_alternative
    from . import group_by

__all__ = ["CliGlobalSystemReportGroup"]


class CliGlobalSystemReportGroup(CliGlobalSystemReportGroupBase):
    """FortiAnalyzer group report API endpoints."""

    chart_alternative: "chart_alternative.CliGlobalSystemReportGroupChartAlternative"
    group_by: "group_by.CliGlobalSystemReportGroupGroupBy"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemReportGroup with endpoint methods and child modules."""
        super().__init__(client)

        from . import chart_alternative as chart_alternative_module
        from . import group_by as group_by_module

        self.chart_alternative = chart_alternative_module.CliGlobalSystemReportGroupChartAlternative(client)
        self.group_by = group_by_module.CliGlobalSystemReportGroupGroupBy(client)

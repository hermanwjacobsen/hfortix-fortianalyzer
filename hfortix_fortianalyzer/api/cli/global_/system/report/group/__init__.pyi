"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .chart_alternative import CliGlobalSystemReportGroupChartAlternative
    from .group_by import CliGlobalSystemReportGroupGroupBy

__all__ = ["CliGlobalSystemReportGroup"]


from ..group_base import CliGlobalSystemReportGroup as CliGlobalSystemReportGroupBase

class CliGlobalSystemReportGroup(CliGlobalSystemReportGroupBase):
    """CliGlobalSystemReportGroup endpoints."""

    chart_alternative: CliGlobalSystemReportGroupChartAlternative
    group_by: CliGlobalSystemReportGroupGroupBy

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .drill_down_table import ReportAdomConfigChartDrillDownTable
    from .table_columns import ReportAdomConfigChartTableColumns
    from .variable_template import ReportAdomConfigChartVariableTemplate

__all__ = ["ReportAdomConfigChart"]


from ..chart_base import ReportAdomConfigChart as ReportAdomConfigChartBase

class ReportAdomConfigChart(ReportAdomConfigChartBase):
    """ReportAdomConfigChart endpoints."""

    drill_down_table: ReportAdomConfigChartDrillDownTable
    table_columns: ReportAdomConfigChartTableColumns
    variable_template: ReportAdomConfigChartVariableTemplate

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

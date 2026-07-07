"""FortiAnalyzer chart config API endpoints."""

from __future__ import annotations

from ..chart_base import ReportAdomConfigChart as ReportAdomConfigChartBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import drill_down_table
    from . import table_columns
    from . import variable_template

__all__ = ["ReportAdomConfigChart"]


class ReportAdomConfigChart(ReportAdomConfigChartBase):
    """FortiAnalyzer chart config API endpoints."""

    drill_down_table: "drill_down_table.ReportAdomConfigChartDrillDownTable"
    table_columns: "table_columns.ReportAdomConfigChartTableColumns"
    variable_template: "variable_template.ReportAdomConfigChartVariableTemplate"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize ReportAdomConfigChart with endpoint methods and child modules."""
        super().__init__(client)

        from . import drill_down_table as drill_down_table_module
        from . import table_columns as table_columns_module
        from . import variable_template as variable_template_module

        self.drill_down_table = drill_down_table_module.ReportAdomConfigChartDrillDownTable(client)
        self.table_columns = table_columns_module.ReportAdomConfigChartTableColumns(client)
        self.variable_template = variable_template_module.ReportAdomConfigChartVariableTemplate(client)

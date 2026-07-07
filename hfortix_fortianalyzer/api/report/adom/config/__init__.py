"""FortiAnalyzer config adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import chart
    from . import dataset
    from . import import_
    from . import layout
    from . import layout_folder
    from . import macro
    from . import output
    from . import schedule

__all__ = ["Config"]


class Config:
    """FortiAnalyzer config adom API endpoints."""

    chart: "chart.ReportAdomConfigChart"
    dataset: "dataset.ReportAdomConfigDataset"
    import_: "import_.ReportAdomConfigImport"
    layout: "layout.ReportAdomConfigLayout"
    layout_folder: "layout_folder.ReportAdomConfigLayoutFolder"
    macro: "macro.ReportAdomConfigMacro"
    output: "output.ReportAdomConfigOutput"
    schedule: "schedule.ReportAdomConfigSchedule"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Config namespace with JSON-RPC client."""
        from . import chart as chart_module
        from . import dataset as dataset_module
        from . import import_ as import__module
        from . import layout as layout_module
        from . import layout_folder as layout_folder_module
        from . import macro as macro_module
        from . import output as output_module
        from . import schedule as schedule_module

        self.chart = chart_module.ReportAdomConfigChart(client)
        self.dataset = dataset_module.ReportAdomConfigDataset(client)
        self.import_ = import__module.ReportAdomConfigImport(client)
        self.layout = layout_module.ReportAdomConfigLayout(client)
        self.layout_folder = layout_folder_module.ReportAdomConfigLayoutFolder(client)
        self.macro = macro_module.ReportAdomConfigMacro(client)
        self.output = output_module.ReportAdomConfigOutput(client)
        self.schedule = schedule_module.ReportAdomConfigSchedule(client)

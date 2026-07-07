"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .chart import ReportAdomConfigChart
    from .dataset import ReportAdomConfigDataset
    from .import_ import ReportAdomConfigImport
    from .layout import ReportAdomConfigLayout
    from .layout_folder import ReportAdomConfigLayoutFolder
    from .macro import ReportAdomConfigMacro
    from .output import ReportAdomConfigOutput
    from .schedule import ReportAdomConfigSchedule

__all__ = ["Config"]


class Config:
    """Config endpoints."""

    chart: ReportAdomConfigChart
    dataset: ReportAdomConfigDataset
    import_: ReportAdomConfigImport
    layout: ReportAdomConfigLayout
    layout_folder: ReportAdomConfigLayoutFolder
    macro: ReportAdomConfigMacro
    output: ReportAdomConfigOutput
    schedule: ReportAdomConfigSchedule

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

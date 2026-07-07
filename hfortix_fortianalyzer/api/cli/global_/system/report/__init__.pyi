"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .auto_cache import CliGlobalSystemReportAutoCache
    from .est_browse_time import CliGlobalSystemReportEstBrowseTime
    from .group import CliGlobalSystemReportGroup
    from .setting import CliGlobalSystemReportSetting

__all__ = ["Report"]


class Report:
    """Report endpoints."""

    auto_cache: CliGlobalSystemReportAutoCache
    est_browse_time: CliGlobalSystemReportEstBrowseTime
    group: CliGlobalSystemReportGroup
    setting: CliGlobalSystemReportSetting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

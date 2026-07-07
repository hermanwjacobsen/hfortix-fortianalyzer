"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .config import Config
    from .config_file import Configfile
    from .graph_file import ReportAdomGraphFile
    from .reports import Reports
    from .run import ReportAdomRun
    from .template import Template

__all__ = ["Adom"]


class Adom:
    """Adom endpoints."""

    config: Config
    config_file: Configfile
    graph_file: ReportAdomGraphFile
    reports: Reports
    run: ReportAdomRun
    template: Template

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

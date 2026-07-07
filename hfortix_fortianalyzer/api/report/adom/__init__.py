"""FortiAnalyzer adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import config
    from . import config_file
    from . import graph_file
    from . import reports
    from . import run
    from . import template

__all__ = ["Adom"]


class Adom:
    """FortiAnalyzer adom API endpoints."""

    config: "config.Config"
    config_file: "config_file.Configfile"
    graph_file: "graph_file.ReportAdomGraphFile"
    reports: "reports.Reports"
    run: "run.ReportAdomRun"
    template: "template.Template"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Adom namespace with JSON-RPC client."""
        from . import config as config_module
        from . import config_file as config_file_module
        from . import graph_file as graph_file_module
        from . import reports as reports_module
        from . import run as run_module
        from . import template as template_module

        self.config = config_module.Config(client)
        self.config_file = config_file_module.Configfile(client)
        self.graph_file = graph_file_module.ReportAdomGraphFile(client)
        self.reports = reports_module.Reports(client)
        self.run = run_module.ReportAdomRun(client)
        self.template = template_module.Template(client)

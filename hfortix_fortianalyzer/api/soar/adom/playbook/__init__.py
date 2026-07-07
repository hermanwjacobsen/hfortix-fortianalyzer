"""FortiAnalyzer playbook adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import export
    from . import import_
    from . import run
    from . import run_log

__all__ = ["Playbook"]


class Playbook:
    """FortiAnalyzer playbook adom API endpoints."""

    export: "export.SoarAdomPlaybookExport"
    import_: "import_.SoarAdomPlaybookImport"
    run: "run.SoarAdomPlaybookRun"
    run_log: "run_log.SoarAdomPlaybookRunLog"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Playbook namespace with JSON-RPC client."""
        from . import export as export_module
        from . import import_ as import__module
        from . import run as run_module
        from . import run_log as run_log_module

        self.export = export_module.SoarAdomPlaybookExport(client)
        self.import_ = import__module.SoarAdomPlaybookImport(client)
        self.run = run_module.SoarAdomPlaybookRun(client)
        self.run_log = run_log_module.SoarAdomPlaybookRunLog(client)

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .export import SoarAdomPlaybookExport
    from .import_ import SoarAdomPlaybookImport
    from .run import SoarAdomPlaybookRun
    from .run_log import SoarAdomPlaybookRunLog

__all__ = ["Playbook"]


class Playbook:
    """Playbook endpoints."""

    export: SoarAdomPlaybookExport
    import_: SoarAdomPlaybookImport
    run: SoarAdomPlaybookRun
    run_log: SoarAdomPlaybookRunLog

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

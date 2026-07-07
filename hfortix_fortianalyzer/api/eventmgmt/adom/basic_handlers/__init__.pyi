"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .export import EventmgmtAdomBasicHandlersExport
    from .import_ import EventmgmtAdomBasicHandlersImport

__all__ = ["Basichandlers"]


class Basichandlers:
    """Basichandlers endpoints."""

    export: EventmgmtAdomBasicHandlersExport
    import_: EventmgmtAdomBasicHandlersImport

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

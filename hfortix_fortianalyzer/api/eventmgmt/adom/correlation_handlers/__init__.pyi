"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .export import EventmgmtAdomCorrelationHandlersExport
    from .import_ import EventmgmtAdomCorrelationHandlersImport

__all__ = ["Correlationhandlers"]


class Correlationhandlers:
    """Correlationhandlers endpoints."""

    export: EventmgmtAdomCorrelationHandlersExport
    import_: EventmgmtAdomCorrelationHandlersImport

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .logfields import LogviewAdomLogfields
    from .logfiles import Logfiles
    from .logsearch import LogviewAdomLogsearch
    from .logstats import LogviewAdomLogstats

__all__ = ["Adom"]


class Adom:
    """Adom endpoints."""

    logfields: LogviewAdomLogfields
    logfiles: Logfiles
    logsearch: LogviewAdomLogsearch
    logstats: LogviewAdomLogstats

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

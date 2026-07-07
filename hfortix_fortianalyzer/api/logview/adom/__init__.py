"""FortiAnalyzer adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import logfields
    from . import logfiles
    from . import logsearch
    from . import logstats

__all__ = ["Adom"]


class Adom:
    """FortiAnalyzer adom API endpoints."""

    logfields: "logfields.LogviewAdomLogfields"
    logfiles: "logfiles.Logfiles"
    logsearch: "logsearch.LogviewAdomLogsearch"
    logstats: "logstats.LogviewAdomLogstats"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Adom namespace with JSON-RPC client."""
        from . import logfields as logfields_module
        from . import logfiles as logfiles_module
        from . import logsearch as logsearch_module
        from . import logstats as logstats_module

        self.logfields = logfields_module.LogviewAdomLogfields(client)
        self.logfiles = logfiles_module.Logfiles(client)
        self.logsearch = logsearch_module.LogviewAdomLogsearch(client)
        self.logstats = logstats_module.LogviewAdomLogstats(client)

"""Type stubs for logview.adom.logfields"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogfields:
    """FortiAnalyzer endpoint: logview.adom.logfields"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        devtype: str | None = None,
        logtype: Literal["traffic", "app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "history", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "waf", "gtp", "ztna", "security"] | None = None,
        subtype: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["LogviewAdomLogfields"]
"""Type stubs for logview.adom.logfiles.search"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogfilesSearch:
    """FortiAnalyzer endpoint: logview.adom.logfiles.search"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        devid: str,
        filename: str,
        logtype: Literal["traffic", "app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "history", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "waf", "gtp"],
        vdom: str,
        apiver: int = 3,
        case_sensitive: bool | None = None,
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["LogviewAdomLogfilesSearch"]
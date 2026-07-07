"""Type stubs for logview.adom.logsearch"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogsearch:
    """FortiAnalyzer endpoint: logview.adom.logsearch"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        device: list[dict[str, Any]],
        logtype: Literal["traffic", "app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "history", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "waf", "gtp"],
        time_range: dict[str, Any],
        tid: int | str | None = None,
        apiver: int = 3,
        case_sensitive: bool | None = None,
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None,
        time_order: Literal["desc", "asc"] | None = None,
        timezone: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3,
        limit: float | None = None,
        offset: float | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["LogviewAdomLogsearch"]
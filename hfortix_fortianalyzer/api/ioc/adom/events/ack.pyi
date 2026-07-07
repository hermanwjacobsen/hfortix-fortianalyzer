"""Type stubs for ioc.adom.events.ack"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IocAdomEventsAck:
    """FortiAnalyzer endpoint: ioc.adom.events.ack"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def update(
        self,
        adom: str,
        events: list[dict[str, Any]],
        apiver: int = 3,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["IocAdomEventsAck"]
"""Type stubs for logview.adom.logstats"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogstats:
    """FortiAnalyzer endpoint: logview.adom.logstats"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        device: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["LogviewAdomLogstats"]
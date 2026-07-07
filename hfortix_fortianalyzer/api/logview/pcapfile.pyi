"""Type stubs for logview.pcapfile"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewPcapfile:
    """FortiAnalyzer endpoint: logview.pcapfile"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        key_data: str,
        key_type: Literal["log-data", "pcapurl"],
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["LogviewPcapfile"]
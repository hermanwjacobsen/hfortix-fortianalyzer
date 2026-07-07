"""Type stubs for soar.adom.indicator.unblock"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomIndicatorUnblock:
    """FortiAnalyzer endpoint: soar.adom.indicator.unblock"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def execute(
        self,
        adom: str,
        indicator_uuid: list[str],
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """EXECUTE operation."""
        ...


__all__ = ["SoarAdomIndicatorUnblock"]
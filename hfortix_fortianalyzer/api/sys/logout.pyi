"""Type stubs for sys.logout"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysLogout:
    """FortiAnalyzer endpoint: sys.logout"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
    ) -> FortiAnalyzerResponse:
        """EXEC operation."""
        ...


__all__ = ["SysLogout"]
"""Type stubs for sys.reboot"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysReboot:
    """FortiAnalyzer endpoint: sys.reboot"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        message: str | None = None,
    ) -> FortiAnalyzerResponse:
        """EXEC operation."""
        ...


__all__ = ["SysReboot"]
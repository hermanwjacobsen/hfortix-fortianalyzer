"""Type stubs for ioc.adom.rescan.run"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IocAdomRescanRun:
    """FortiAnalyzer endpoint: ioc.adom.rescan.run"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...

    def delete(
        self,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["IocAdomRescanRun"]
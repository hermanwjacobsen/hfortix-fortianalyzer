"""Type stubs for fazsys.adom.storage-info-history"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysAdomStorageInfoHistory:
    """FortiAnalyzer endpoint: fazsys.adom.storage-info-history"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        time_range: dict[str, Any],
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["FazsysAdomStorageInfoHistory"]
"""Type stubs for fazsys.adom.enduser-avatar"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FazsysAdomEnduserAvatar:
    """FortiAnalyzer endpoint: fazsys.adom.enduser-avatar"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        user: list[dict[str, Any]],
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["FazsysAdomEnduserAvatar"]
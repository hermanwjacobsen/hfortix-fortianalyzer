"""Type stubs for dvmdb.adom.object member"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbAdomObjectMember:
    """FortiAnalyzer endpoint: dvmdb.adom.object member"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        object_member: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        object_member: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def set(
        self,
        adom: str,
        object_member: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        adom: str,
        object_member: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["DvmdbAdomObjectMember"]
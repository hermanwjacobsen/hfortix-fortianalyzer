"""Type stubs for dvmdb.adom.group.object member"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbAdomGroupObjectMember:
    """FortiAnalyzer endpoint: dvmdb.adom.group.object member"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        group: str,
        object_member: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        group: str,
        object_member: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def set(
        self,
        adom: str,
        group: str,
        object_member: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        adom: str,
        group: str,
        object_member: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["DvmdbAdomGroupObjectMember"]
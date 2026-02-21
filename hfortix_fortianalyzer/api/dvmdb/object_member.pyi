"""Type stubs for dvmdb.object member"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse



class DvmdbObjectMember:
    """FortiAnalyzer endpoint: dvmdb.object member"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str | None = None,
        name: str | None = None,
        vdom: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str | None = None,
        name: str | None = None,
        vdom: str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def set(
        self,
        adom: str | None = None,
        name: str | None = None,
        vdom: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        adom: str | None = None,
        name: str | None = None,
        vdom: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["DvmdbObjectMember"]
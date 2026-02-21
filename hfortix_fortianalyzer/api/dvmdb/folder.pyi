"""Type stubs for dvmdb.folder"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbFolderAddResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbFolder endpoint with autocomplete support."""

    # ========================================================================
    # HTTP Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def http_status_code(self) -> int | None: ...
    @property
    def http_response_time(self) -> float | None: ...
    @property
    def http_method(self) -> str | None: ...
    @property
    def http_url(self) -> str | None: ...

    # ========================================================================
    # API Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def api_status_code(self) -> int | None: ...
    @property
    def api_status_message(self) -> str | None: ...
    @property
    def api_id(self) -> int | None: ...
    @property
    def api_url(self) -> str | None: ...
    @property
    def api_raw(self) -> dict[str, Any]: ...

    # ========================================================================
    # Data Fields (specific to this endpoint)
    # ========================================================================
    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    class DvmdbFolderItem:
        """Item yielded when iterating over DvmdbFolderResponse."""

        @property
        def name(self) -> str: ...

        # Inherited from FortiAnalyzerObject
        @property
        def raw(self) -> dict[str, Any]: ...
        @property
        def dict(self) -> dict[str, Any]: ...
        @property
        def json(self) -> str: ...
        def __getitem__(self, key: str) -> Any: ...

    # Inherited methods from FortiAnalyzerResponse
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[DvmdbFolderItem]: ...
    def __len__(self) -> int: ...


class DvmdbFolderGetResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbFolder endpoint with autocomplete support."""

    # ========================================================================
    # HTTP Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def http_status_code(self) -> int | None: ...
    @property
    def http_response_time(self) -> float | None: ...
    @property
    def http_method(self) -> str | None: ...
    @property
    def http_url(self) -> str | None: ...

    # ========================================================================
    # API Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def api_status_code(self) -> int | None: ...
    @property
    def api_status_message(self) -> str | None: ...
    @property
    def api_id(self) -> int | None: ...
    @property
    def api_url(self) -> str | None: ...
    @property
    def api_raw(self) -> dict[str, Any]: ...

    # ========================================================================
    # Data Fields (specific to this endpoint)
    # ========================================================================
    @property
    def oid(self) -> int | None:
        """Object ID (dynamically added by FortiAnalyzer API, not in Swagger schema)"""
        ...

    @property
    def desc(self) -> str | None:
        """Field: desc"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def parent(self) -> int | None:
        """Field: parent"""
        ...

    class DvmdbFolderItem:
        """Item yielded when iterating over DvmdbFolderResponse."""

        @property
        def oid(self) -> int: ...
        @property
        def desc(self) -> str: ...
        @property
        def name(self) -> str: ...
        @property
        def parent(self) -> int: ...

        # Inherited from FortiAnalyzerObject
        @property
        def raw(self) -> dict[str, Any]: ...
        @property
        def dict(self) -> dict[str, Any]: ...
        @property
        def json(self) -> str: ...
        def __getitem__(self, key: str) -> Any: ...

    # Inherited methods from FortiAnalyzerResponse
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[DvmdbFolderItem]: ...
    def __len__(self) -> int: ...



class DvmdbFolder:
    """FortiAnalyzer endpoint: dvmdb.folder"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None,
    ) -> DvmdbFolderAddResponse:
        """ADD operation."""
        ...

    def get(
        self,
        adom: str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["desc", "name", "parent"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> DvmdbFolderGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        adom: str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None,
    ) -> DvmdbFolderAddResponse:
        """SET operation."""
        ...

    def update(
        self,
        adom: str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None,
    ) -> DvmdbFolderAddResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        adom: str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["DvmdbFolder", "DvmdbFolderGetResponse", "DvmdbFolderAddResponse"]
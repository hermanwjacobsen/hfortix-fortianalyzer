"""Type stubs for dvmdb.adom.folder"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbAdomFolderAddItem:
    """Item yielded when iterating over DvmdbAdomFolderAddResponse."""

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


class DvmdbAdomFolderAddResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbAdomFolderAdd endpoint with autocomplete support."""

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
    def __iter__(self) -> Iterator[DvmdbAdomFolderAddItem]: ...
    def __len__(self) -> int: ...


class DvmdbAdomFolderGetItem:
    """Item yielded when iterating over DvmdbAdomFolderGetResponse."""

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


class DvmdbAdomFolderGetResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbAdomFolderGet endpoint with autocomplete support."""

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
    def __iter__(self) -> Iterator[DvmdbAdomFolderGetItem]: ...
    def __len__(self) -> int: ...


class DvmdbAdomFolder:
    """FortiAnalyzer endpoint: dvmdb.adom.folder"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        folder: int | str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None,
    ) -> DvmdbAdomFolderAddResponse:
        """ADD operation."""
        ...

    def get(
        self,
        adom: str,
        folder: int | str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["desc", "name", "parent"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> DvmdbAdomFolderGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        adom: str,
        folder: int | str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None,
    ) -> DvmdbAdomFolderAddResponse:
        """SET operation."""
        ...

    def update(
        self,
        adom: str,
        folder: int | str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None,
    ) -> DvmdbAdomFolderAddResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        adom: str,
        folder: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["DvmdbAdomFolder", "DvmdbAdomFolderAddResponse", "DvmdbAdomFolderGetResponse"]
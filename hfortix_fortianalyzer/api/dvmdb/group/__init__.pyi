"""Type stubs for dvmdb.group"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbGroupAddResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbGroup endpoint with autocomplete support."""

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

    class DvmdbGroupItem:
        """Item yielded when iterating over DvmdbGroupResponse."""

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
    def __iter__(self) -> Iterator[DvmdbGroupItem]: ...
    def __len__(self) -> int: ...


class DvmdbGroupGetResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbGroup endpoint with autocomplete support."""

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
    def cluster_type(self) -> Literal["unknown", "vwan", "ums_aws", "ums_azure", "ums_gcp"] | None:
        """Field: cluster_type"""
        ...

    @property
    def desc(self) -> str | None:
        """Field: desc"""
        ...

    @property
    def id_(self) -> str | None:
        """Field: id"""
        ...

    @property
    def meta_fields(self) -> dict[str, Any] | None:
        """Default metafields: none."""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def os_type(self) -> Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None:
        """Field: os_type"""
        ...

    @property
    def type_(self) -> Literal["normal", "default", "auto", "cluster", "fabric"] | None:
        """Field: type"""
        ...

    class DvmdbGroupItem:
        """Item yielded when iterating over DvmdbGroupResponse."""

        @property
        def oid(self) -> int: ...
        @property
        def cluster_type(self) -> Literal["unknown", "vwan", "ums_aws", "ums_azure", "ums_gcp"]: ...
        @property
        def desc(self) -> str: ...
        @property
        def id_(self) -> str: ...
        @property
        def meta_fields(self) -> dict[str, Any]: ...
        @property
        def name(self) -> str: ...
        @property
        def os_type(self) -> Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"]: ...
        @property
        def type_(self) -> Literal["normal", "default", "auto", "cluster", "fabric"]: ...

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
    def __iter__(self) -> Iterator[DvmdbGroupItem]: ...
    def __len__(self) -> int: ...



class DvmdbGroup:
    """FortiAnalyzer endpoint: dvmdb.group"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str | None = None,
        cluster_type: Literal["unknown", "vwan", "ums_aws", "ums_azure", "ums_gcp"] | None = None,
        desc: str | None = None,
        id_: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        type_: Literal["normal", "default", "auto", "cluster", "fabric"] | None = None,
    ) -> DvmdbGroupAddResponse:
        """ADD operation."""
        ...

    def get(
        self,
        adom: str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["cluster_type", "desc", "id", "name", "os_type", "type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        meta_fields: list[str] | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> DvmdbGroupGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        adom: str | None = None,
        cluster_type: Literal["unknown", "vwan", "ums_aws", "ums_azure", "ums_gcp"] | None = None,
        desc: str | None = None,
        id_: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        type_: Literal["normal", "default", "auto", "cluster", "fabric"] | None = None,
    ) -> DvmdbGroupAddResponse:
        """SET operation."""
        ...

    def update(
        self,
        adom: str | None = None,
        cluster_type: Literal["unknown", "vwan", "ums_aws", "ums_azure", "ums_gcp"] | None = None,
        desc: str | None = None,
        id_: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        type_: Literal["normal", "default", "auto", "cluster", "fabric"] | None = None,
    ) -> DvmdbGroupAddResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        adom: str | None = None,
        cluster_type: Literal["unknown", "vwan", "ums_aws", "ums_azure", "ums_gcp"] | None = None,
        desc: str | None = None,
        id_: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        type_: Literal["normal", "default", "auto", "cluster", "fabric"] | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["DvmdbGroup", "DvmdbGroupAddResponse", "DvmdbGroupGetResponse"]
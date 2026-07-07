"""Type stubs for dvmdb.device.vdom"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbDeviceVdomAddItem:
    """Item yielded when iterating over DvmdbDeviceVdomAddResponse."""

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


class DvmdbDeviceVdomAddResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbDeviceVdomAdd endpoint with autocomplete support."""

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
    def __iter__(self) -> Iterator[DvmdbDeviceVdomAddItem]: ...
    def __len__(self) -> int: ...


class DvmdbDeviceVdomGetItem:
    """Item yielded when iterating over DvmdbDeviceVdomGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def comments(self) -> str: ...
    @property
    def meta_fields(self) -> dict[str, Any]: ...
    @property
    def name(self) -> str: ...
    @property
    def opmode(self) -> Literal["nat", "transparent"]: ...
    @property
    def rtm_prof_id(self) -> int: ...
    @property
    def status(self) -> str: ...
    @property
    def vdom_type(self) -> Literal["traffic", "admin"]: ...
    @property
    def vpn_id(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class DvmdbDeviceVdomGetResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbDeviceVdomGet endpoint with autocomplete support."""

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
    def comments(self) -> str | None:
        """Field: comments"""
        ...

    @property
    def meta_fields(self) -> dict[str, Any] | None:
        """Field: meta fields"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def opmode(self) -> Literal["nat", "transparent"] | None:
        """Field: opmode"""
        ...

    @property
    def rtm_prof_id(self) -> int | None:
        """Field: rtm_prof_id"""
        ...

    @property
    def status(self) -> str | None:
        """Field: status"""
        ...

    @property
    def vdom_type(self) -> Literal["traffic", "admin"] | None:
        """Field: vdom_type"""
        ...

    @property
    def vpn_id(self) -> int | None:
        """Field: vpn_id"""
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
    def __iter__(self) -> Iterator[DvmdbDeviceVdomGetItem]: ...
    def __len__(self) -> int: ...


class DvmdbDeviceVdom:
    """FortiAnalyzer endpoint: dvmdb.device.vdom"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        device: str,
        vdom: int | str | None = None,
        comments: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        opmode: Literal["nat", "transparent"] | None = None,
        rtm_prof_id: int | None = None,
        status: str | None = None,
        vdom_type: Literal["traffic", "admin"] | None = None,
        vpn_id: int | None = None,
    ) -> DvmdbDeviceVdomAddResponse:
        """ADD operation."""
        ...

    def get(
        self,
        device: str,
        vdom: int | str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["comments", "name", "opmode", "rtm_prof_id", "status", "vdom_type", "vpn_id"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        meta_fields: list[str] | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> DvmdbDeviceVdomGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        device: str,
        vdom: int | str | None = None,
        comments: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        opmode: Literal["nat", "transparent"] | None = None,
        rtm_prof_id: int | None = None,
        status: str | None = None,
        vdom_type: Literal["traffic", "admin"] | None = None,
        vpn_id: int | None = None,
    ) -> DvmdbDeviceVdomAddResponse:
        """SET operation."""
        ...

    def update(
        self,
        device: str,
        vdom: int | str | None = None,
        comments: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        opmode: Literal["nat", "transparent"] | None = None,
        rtm_prof_id: int | None = None,
        status: str | None = None,
        vdom_type: Literal["traffic", "admin"] | None = None,
        vpn_id: int | None = None,
    ) -> DvmdbDeviceVdomAddResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        device: str,
        vdom: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["DvmdbDeviceVdom", "DvmdbDeviceVdomGetResponse", "DvmdbDeviceVdomAddResponse"]
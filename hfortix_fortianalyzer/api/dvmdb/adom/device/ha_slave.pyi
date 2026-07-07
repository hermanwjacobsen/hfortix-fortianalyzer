"""Type stubs for dvmdb.adom.device.ha_slave"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbAdomDeviceHaSlaveGetItem:
    """Item yielded when iterating over DvmdbAdomDeviceHaSlaveGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def conf_status(self) -> int: ...
    @property
    def idx(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def prio(self) -> int: ...
    @property
    def role(self) -> Literal["slave", "master"]: ...
    @property
    def sn(self) -> str: ...
    @property
    def status(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class DvmdbAdomDeviceHaSlaveGetResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbAdomDeviceHaSlaveGet endpoint with autocomplete support."""

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
    def conf_status(self) -> int | None:
        """Field: conf_status"""
        ...

    @property
    def idx(self) -> int | None:
        """Field: idx"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def prio(self) -> int | None:
        """Field: prio"""
        ...

    @property
    def role(self) -> Literal["slave", "master"] | None:
        """Field: role"""
        ...

    @property
    def sn(self) -> str | None:
        """Field: sn"""
        ...

    @property
    def status(self) -> int | None:
        """Field: status"""
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
    def __iter__(self) -> Iterator[DvmdbAdomDeviceHaSlaveGetItem]: ...
    def __len__(self) -> int: ...


class DvmdbAdomDeviceHaSlave:
    """FortiAnalyzer endpoint: dvmdb.adom.device.ha_slave"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        device: str,
        ha_slave: int | str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["conf_status", "idx", "name", "prio", "role", "sn", "status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> DvmdbAdomDeviceHaSlaveGetResponse:
        """GET operation."""
        ...


__all__ = ["DvmdbAdomDeviceHaSlave", "DvmdbAdomDeviceHaSlaveGetResponse"]
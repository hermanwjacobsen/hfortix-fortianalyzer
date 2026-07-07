"""Type stubs for sys.ha.status"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysHaStatusGetItem:
    """Item yielded when iterating over SysHaStatusGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def ha_gropu_id(self) -> int: ...
    @property
    def ha_group_name(self) -> str: ...
    @property
    def hb_interval(self) -> int: ...
    @property
    def hb_intreface(self) -> str: ...
    @property
    def members(self) -> list[MembersItem]: ...
    @property
    def mode(self) -> Literal["standalone", "a-p"]: ...
    @property
    def role(self) -> Literal["standalone", "master", "slave"]: ...
    @property
    def status(self) -> Literal["down", "up"]: ...
    @property
    def vip_interface(self) -> str: ...
    @property
    def virtual_ip(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class MembersItem:
    """Nested item type for members array."""

    @property
    def ip(self) -> str: ...
    @property
    def role(self) -> Literal["master", "slave"]: ...
    @property
    def serialno(self) -> str: ...
    @property
    def status(self) -> Literal["down", "negotiating", "synchronizing", "up"]: ...


class SysHaStatusGetResponse(FortiAnalyzerResponse):
    """Typed response for SysHaStatusGet endpoint with autocomplete support."""

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
    def ha_gropu_id(self) -> int | None:
        """Field: ha-gropu-id"""
        ...

    @property
    def ha_group_name(self) -> str | None:
        """Field: ha-group-name"""
        ...

    @property
    def hb_interval(self) -> int | None:
        """Field: hb-interval"""
        ...

    @property
    def hb_intreface(self) -> str | None:
        """Field: hb-intreface"""
        ...

    @property
    def members(self) -> list[MembersItem]:
        """Field: members"""
        ...

    @property
    def mode(self) -> Literal["standalone", "a-p"] | None:
        """Field: mode"""
        ...

    @property
    def role(self) -> Literal["standalone", "master", "slave"] | None:
        """Field: role"""
        ...

    @property
    def status(self) -> Literal["down", "up"] | None:
        """Field: status"""
        ...

    @property
    def vip_interface(self) -> str | None:
        """Field: vip-interface"""
        ...

    @property
    def virtual_ip(self) -> str | None:
        """Field: virtual-ip"""
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
    def __iter__(self) -> Iterator[SysHaStatusGetItem]: ...
    def __len__(self) -> int: ...


class SysHaStatus:
    """FortiAnalyzer endpoint: sys.ha.status"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> SysHaStatusGetResponse:
        """GET operation."""
        ...


__all__ = ["SysHaStatus", "SysHaStatusGetResponse"]
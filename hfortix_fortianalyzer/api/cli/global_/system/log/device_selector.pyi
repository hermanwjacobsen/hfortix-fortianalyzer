"""Type stubs for cli.global.system.log.device-selector"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogDeviceSelectorGetItem:
    """Item yielded when iterating over CliGlobalSystemLogDeviceSelectorGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def action(self) -> Literal["include", "exclude"]: ...
    @property
    def comment(self) -> str: ...
    @property
    def devid(self) -> str: ...
    @property
    def expire(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def srcip(self) -> str: ...
    @property
    def srcip_mode(self) -> Literal["UDP514", "TCP514", "any"]: ...
    @property
    def type(self) -> Literal["unspecified", "devid", "srcip"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogDeviceSelectorGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogDeviceSelectorGet endpoint with autocomplete support."""

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
    def action(self) -> Literal["include", "exclude"] | None:
        """Field: action"""
        ...

    @property
    def comment(self) -> str | None:
        """Field: comment"""
        ...

    @property
    def devid(self) -> str | None:
        """Field: devid"""
        ...

    @property
    def expire(self) -> str | None:
        """Field: expire"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def srcip(self) -> str | None:
        """Field: srcip"""
        ...

    @property
    def srcip_mode(self) -> Literal["UDP514", "TCP514", "any"] | None:
        """Field: srcip-mode"""
        ...

    @property
    def type(self) -> Literal["unspecified", "devid", "srcip"] | None:
        """Field: type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogDeviceSelectorGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogDeviceSelector:
    """FortiAnalyzer endpoint: cli.global.system.log.device-selector"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        device_selector: int | str | None = None,
        fields: list[Literal["action", "comment", "devid", "expire", "id", "srcip", "srcip-mode", "type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLogDeviceSelectorGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        device_selector: int | str | None = None,
        action: Literal["include", "exclude"] | None = None,
        comment: str | None = None,
        devid: str | None = None,
        expire: str | None = None,
        id: int | None = None,
        srcip: str | None = None,
        srcip_mode: Literal["UDP514", "TCP514", "any"] | None = None,
        type: Literal["unspecified", "devid", "srcip"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        device_selector: int | str | None = None,
        action: Literal["include", "exclude"] | None = None,
        comment: str | None = None,
        devid: str | None = None,
        expire: str | None = None,
        id: int | None = None,
        srcip: str | None = None,
        srcip_mode: Literal["UDP514", "TCP514", "any"] | None = None,
        type: Literal["unspecified", "devid", "srcip"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        device_selector: int | str | None = None,
        action: Literal["include", "exclude"] | None = None,
        comment: str | None = None,
        devid: str | None = None,
        expire: str | None = None,
        id: int | None = None,
        srcip: str | None = None,
        srcip_mode: Literal["UDP514", "TCP514", "any"] | None = None,
        type: Literal["unspecified", "devid", "srcip"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        device_selector: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLogDeviceSelector", "CliGlobalSystemLogDeviceSelectorGetResponse"]
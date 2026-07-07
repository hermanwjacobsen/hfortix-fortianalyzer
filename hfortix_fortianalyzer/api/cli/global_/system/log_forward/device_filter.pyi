"""Type stubs for cli.global.system.log-forward.device-filter"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogForwardDeviceFilterGetItem:
    """Item yielded when iterating over CliGlobalSystemLogForwardDeviceFilterGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def action(self) -> Literal["include", "exclude", "include-like", "exclude-like"]: ...
    @property
    def adom(self) -> str: ...
    @property
    def device(self) -> str: ...
    @property
    def id(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogForwardDeviceFilterGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogForwardDeviceFilterGet endpoint with autocomplete support."""

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
    def action(self) -> Literal["include", "exclude", "include-like", "exclude-like"] | None:
        """Field: action"""
        ...

    @property
    def adom(self) -> str | None:
        """Field: adom"""
        ...

    @property
    def device(self) -> str | None:
        """Field: device"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogForwardDeviceFilterGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogForwardDeviceFilter:
    """FortiAnalyzer endpoint: cli.global.system.log-forward.device-filter"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        log_forward: str,
        device_filter: int | str | None = None,
        fields: list[Literal["action", "adom", "device", "id"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLogForwardDeviceFilterGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        log_forward: str,
        device_filter: int | str | None = None,
        action: Literal["include", "exclude", "include-like", "exclude-like"] | None = None,
        adom: str | None = None,
        device: str | None = None,
        id: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        log_forward: str,
        device_filter: int | str | None = None,
        action: Literal["include", "exclude", "include-like", "exclude-like"] | None = None,
        adom: str | None = None,
        device: str | None = None,
        id: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        log_forward: str,
        device_filter: int | str | None = None,
        action: Literal["include", "exclude", "include-like", "exclude-like"] | None = None,
        adom: str | None = None,
        device: str | None = None,
        id: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        log_forward: str,
        device_filter: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLogForwardDeviceFilter", "CliGlobalSystemLogForwardDeviceFilterGetResponse"]
"""Type stubs for cli.global.fmupdate.fgd-setting.server-override"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFgdSettingServerOverrideGetItem:
    """Item yielded when iterating over CliGlobalFmupdateFgdSettingServerOverrideGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def servlist(self) -> list[ServlistItem]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class ServlistItem:
    """Nested item type for servlist array."""

    @property
    def id(self) -> int: ...
    @property
    def ip(self) -> str: ...
    @property
    def ip6(self) -> str: ...
    @property
    def port(self) -> int: ...
    @property
    def service_type(self) -> list[Any]: ...


class CliGlobalFmupdateFgdSettingServerOverrideGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateFgdSettingServerOverrideGet endpoint with autocomplete support."""

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
    def servlist(self) -> list[ServlistItem]:
        """Field: servlist"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateFgdSettingServerOverrideGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateFgdSettingServerOverride:
    """FortiAnalyzer endpoint: cli.global.fmupdate.fgd-setting.server-override"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateFgdSettingServerOverrideGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        servlist: list[dict[str, Any]] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        servlist: list[dict[str, Any]] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateFgdSettingServerOverride", "CliGlobalFmupdateFgdSettingServerOverrideGetResponse"]
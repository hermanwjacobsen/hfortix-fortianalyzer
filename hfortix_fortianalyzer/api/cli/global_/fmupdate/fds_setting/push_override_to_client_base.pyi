"""Type stubs for cli.global.fmupdate.fds-setting.push-override-to-client"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFdsSettingPushOverrideToClientGetItem:
    """Item yielded when iterating over CliGlobalFmupdateFdsSettingPushOverrideToClientGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def announce_ip(self) -> list[AnnounceIpItem]: ...
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


class AnnounceIpItem:
    """Nested item type for announce-ip array."""

    @property
    def id(self) -> int: ...
    @property
    def ip(self) -> str: ...
    @property
    def port(self) -> int: ...


class CliGlobalFmupdateFdsSettingPushOverrideToClientGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateFdsSettingPushOverrideToClientGet endpoint with autocomplete support."""

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
    def announce_ip(self) -> list[AnnounceIpItem]:
        """Field: announce-ip"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateFdsSettingPushOverrideToClientGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateFdsSettingPushOverrideToClient:
    """FortiAnalyzer endpoint: cli.global.fmupdate.fds-setting.push-override-to-client"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateFdsSettingPushOverrideToClientGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        announce_ip: list[dict[str, Any]] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        announce_ip: list[dict[str, Any]] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateFdsSettingPushOverrideToClient", "CliGlobalFmupdateFdsSettingPushOverrideToClientGetResponse"]
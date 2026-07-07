"""Type stubs for cli.global.fmupdate.fds-setting.push-override-to-client.announce-ip"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIpGetItem:
    """Item yielded when iterating over CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIpGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def ip(self) -> str: ...
    @property
    def port(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIpGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIpGet endpoint with autocomplete support."""

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
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def ip(self) -> str | None:
        """Field: ip"""
        ...

    @property
    def port(self) -> int | None:
        """Field: port"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIpGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIp:
    """FortiAnalyzer endpoint: cli.global.fmupdate.fds-setting.push-override-to-client.announce-ip"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        announce_ip: int | str | None = None,
        fields: list[Literal["id", "ip", "port"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIpGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        announce_ip: int | str | None = None,
        id: int | None = None,
        ip: str | None = None,
        port: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        announce_ip: int | str | None = None,
        id: int | None = None,
        ip: str | None = None,
        port: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        announce_ip: int | str | None = None,
        id: int | None = None,
        ip: str | None = None,
        port: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        announce_ip: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIp", "CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIpGetResponse"]
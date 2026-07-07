"""Type stubs for cli.global.system.ntp"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemNtpGetItem:
    """Item yielded when iterating over CliGlobalSystemNtpGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def ntpserver(self) -> list[NtpserverItem]: ...
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


class NtpserverItem:
    """Nested item type for ntpserver array."""

    @property
    def authentication(self) -> Literal["disable", "enable"]: ...
    @property
    def id(self) -> int: ...
    @property
    def key(self) -> list[Any]: ...
    @property
    def key_fmt(self) -> Literal["ascii", "hex"]: ...
    @property
    def key_id(self) -> int: ...
    @property
    def key_type(self) -> Literal["md5", "sha256"]: ...
    @property
    def maxpoll(self) -> int: ...
    @property
    def minpoll(self) -> int: ...
    @property
    def ntpv3(self) -> Literal["disable", "enable"]: ...
    @property
    def server(self) -> str: ...


class CliGlobalSystemNtpGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemNtpGet endpoint with autocomplete support."""

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
    def ntpserver(self) -> list[NtpserverItem]:
        """Field: ntpserver"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemNtpGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemNtp:
    """FortiAnalyzer endpoint: cli.global.system.ntp"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemNtpGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        ntpserver: list[dict[str, Any]] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        ntpserver: list[dict[str, Any]] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemNtp", "CliGlobalSystemNtpGetResponse"]
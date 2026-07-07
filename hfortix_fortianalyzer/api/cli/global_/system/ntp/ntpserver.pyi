"""Type stubs for cli.global.system.ntp.ntpserver"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemNtpNtpserverGetItem:
    """Item yielded when iterating over CliGlobalSystemNtpNtpserverGetResponse."""

    @property
    def oid(self) -> int: ...
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

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemNtpNtpserverGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemNtpNtpserverGet endpoint with autocomplete support."""

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
    def authentication(self) -> Literal["disable", "enable"] | None:
        """Field: authentication"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def key(self) -> list[Any] | None:
        """Field: key"""
        ...

    @property
    def key_fmt(self) -> Literal["ascii", "hex"] | None:
        """Field: key-fmt"""
        ...

    @property
    def key_id(self) -> int | None:
        """Field: key-id"""
        ...

    @property
    def key_type(self) -> Literal["md5", "sha256"] | None:
        """Field: key-type"""
        ...

    @property
    def maxpoll(self) -> int | None:
        """Field: maxpoll"""
        ...

    @property
    def minpoll(self) -> int | None:
        """Field: minpoll"""
        ...

    @property
    def ntpv3(self) -> Literal["disable", "enable"] | None:
        """Field: ntpv3"""
        ...

    @property
    def server(self) -> str | None:
        """Field: server"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemNtpNtpserverGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemNtpNtpserver:
    """FortiAnalyzer endpoint: cli.global.system.ntp.ntpserver"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        ntpserver: int | str | None = None,
        fields: list[Literal["authentication", "id", "key", "key-fmt", "key-id", "key-type", "maxpoll", "minpoll", "ntpv3", "server"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemNtpNtpserverGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        ntpserver: int | str | None = None,
        authentication: Literal["disable", "enable"] | None = None,
        id: int | None = None,
        key: list[Any] | None = None,
        key_fmt: Literal["ascii", "hex"] | None = None,
        key_id: int | None = None,
        key_type: Literal["md5", "sha256"] | None = None,
        maxpoll: int | None = None,
        minpoll: int | None = None,
        ntpv3: Literal["disable", "enable"] | None = None,
        server: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        ntpserver: int | str | None = None,
        authentication: Literal["disable", "enable"] | None = None,
        id: int | None = None,
        key: list[Any] | None = None,
        key_fmt: Literal["ascii", "hex"] | None = None,
        key_id: int | None = None,
        key_type: Literal["md5", "sha256"] | None = None,
        maxpoll: int | None = None,
        minpoll: int | None = None,
        ntpv3: Literal["disable", "enable"] | None = None,
        server: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        ntpserver: int | str | None = None,
        authentication: Literal["disable", "enable"] | None = None,
        id: int | None = None,
        key: list[Any] | None = None,
        key_fmt: Literal["ascii", "hex"] | None = None,
        key_id: int | None = None,
        key_type: Literal["md5", "sha256"] | None = None,
        maxpoll: int | None = None,
        minpoll: int | None = None,
        ntpv3: Literal["disable", "enable"] | None = None,
        server: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        ntpserver: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemNtpNtpserver", "CliGlobalSystemNtpNtpserverGetResponse"]
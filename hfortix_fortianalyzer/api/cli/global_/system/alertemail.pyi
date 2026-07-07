"""Type stubs for cli.global.system.alertemail"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAlertemailGetItem:
    """Item yielded when iterating over CliGlobalSystemAlertemailGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def authentication(self) -> Literal["disable", "enable"]: ...
    @property
    def fromaddress(self) -> str: ...
    @property
    def fromname(self) -> str: ...
    @property
    def smtppassword(self) -> list[Any]: ...
    @property
    def smtpport(self) -> int: ...
    @property
    def smtpserver(self) -> str: ...
    @property
    def smtpuser(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAlertemailGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAlertemailGet endpoint with autocomplete support."""

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
    def fromaddress(self) -> str | None:
        """Field: fromaddress"""
        ...

    @property
    def fromname(self) -> str | None:
        """Field: fromname"""
        ...

    @property
    def smtppassword(self) -> list[Any] | None:
        """Field: smtppassword"""
        ...

    @property
    def smtpport(self) -> int | None:
        """Field: smtpport"""
        ...

    @property
    def smtpserver(self) -> str | None:
        """Field: smtpserver"""
        ...

    @property
    def smtpuser(self) -> str | None:
        """Field: smtpuser"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAlertemailGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAlertemail:
    """FortiAnalyzer endpoint: cli.global.system.alertemail"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemAlertemailGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        authentication: Literal["disable", "enable"] | None = None,
        fromaddress: str | None = None,
        fromname: str | None = None,
        smtppassword: list[Any] | None = None,
        smtpport: int | None = None,
        smtpserver: str | None = None,
        smtpuser: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        authentication: Literal["disable", "enable"] | None = None,
        fromaddress: str | None = None,
        fromname: str | None = None,
        smtppassword: list[Any] | None = None,
        smtpport: int | None = None,
        smtpserver: str | None = None,
        smtpuser: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemAlertemail", "CliGlobalSystemAlertemailGetResponse"]
"""Type stubs for cli.global.system.log.mail-domain"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogMailDomainGetItem:
    """Item yielded when iterating over CliGlobalSystemLogMailDomainGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def devices(self) -> str: ...
    @property
    def domain(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def vdom(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogMailDomainGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogMailDomainGet endpoint with autocomplete support."""

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
    def devices(self) -> str | None:
        """Field: devices"""
        ...

    @property
    def domain(self) -> str | None:
        """Field: domain"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def vdom(self) -> str | None:
        """Field: vdom"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogMailDomainGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogMailDomain:
    """FortiAnalyzer endpoint: cli.global.system.log.mail-domain"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        mail_domain: int | str | None = None,
        fields: list[Literal["devices", "domain", "id", "vdom"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLogMailDomainGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        mail_domain: int | str | None = None,
        devices: str | None = None,
        domain: str | None = None,
        id: int | None = None,
        vdom: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        mail_domain: int | str | None = None,
        devices: str | None = None,
        domain: str | None = None,
        id: int | None = None,
        vdom: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        mail_domain: int | str | None = None,
        devices: str | None = None,
        domain: str | None = None,
        id: int | None = None,
        vdom: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        mail_domain: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLogMailDomain", "CliGlobalSystemLogMailDomainGetResponse"]
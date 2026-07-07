"""Type stubs for cli.global.system.csf.trusted-list"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCsfTrustedListGetItem:
    """Item yielded when iterating over CliGlobalSystemCsfTrustedListGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def action(self) -> Literal["accept", "deny"]: ...
    @property
    def adom(self) -> list[AdomItem]: ...
    @property
    def adom_access(self) -> Literal["all", "specify"]: ...
    @property
    def authorization_type(self) -> Literal["serial", "certificate"]: ...
    @property
    def certificate(self) -> str: ...
    @property
    def downstream_authorization(self) -> Literal["disable", "enable"]: ...
    @property
    def ha_members(self) -> str: ...
    @property
    def index(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def serial(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class AdomItem:
    """Nested item type for adom array."""

    @property
    def adom_name(self) -> str: ...


class CliGlobalSystemCsfTrustedListGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCsfTrustedListGet endpoint with autocomplete support."""

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
    def action(self) -> Literal["accept", "deny"] | None:
        """Field: action"""
        ...

    @property
    def adom(self) -> list[AdomItem]:
        """Field: adom"""
        ...

    @property
    def adom_access(self) -> Literal["all", "specify"] | None:
        """Field: adom-access"""
        ...

    @property
    def authorization_type(self) -> Literal["serial", "certificate"] | None:
        """Field: authorization-type"""
        ...

    @property
    def certificate(self) -> str | None:
        """Field: certificate"""
        ...

    @property
    def downstream_authorization(self) -> Literal["disable", "enable"] | None:
        """Field: downstream-authorization"""
        ...

    @property
    def ha_members(self) -> str | None:
        """Field: ha-members"""
        ...

    @property
    def index(self) -> int | None:
        """Field: index"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def serial(self) -> str | None:
        """Field: serial"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemCsfTrustedListGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCsfTrustedList:
    """FortiAnalyzer endpoint: cli.global.system.csf.trusted-list"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        trusted_list: int | str | None = None,
        fields: list[Literal["action", "adom-access", "authorization-type", "certificate", "downstream-authorization", "ha-members", "index", "name", "serial"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemCsfTrustedListGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        trusted_list: int | str | None = None,
        action: Literal["accept", "deny"] | None = None,
        adom: list[dict[str, Any]] | None = None,
        adom_access: Literal["all", "specify"] | None = None,
        authorization_type: Literal["serial", "certificate"] | None = None,
        certificate: str | None = None,
        downstream_authorization: Literal["disable", "enable"] | None = None,
        ha_members: str | None = None,
        index: int | None = None,
        name: str | None = None,
        serial: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        trusted_list: int | str | None = None,
        action: Literal["accept", "deny"] | None = None,
        adom: list[dict[str, Any]] | None = None,
        adom_access: Literal["all", "specify"] | None = None,
        authorization_type: Literal["serial", "certificate"] | None = None,
        certificate: str | None = None,
        downstream_authorization: Literal["disable", "enable"] | None = None,
        ha_members: str | None = None,
        index: int | None = None,
        name: str | None = None,
        serial: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        trusted_list: int | str | None = None,
        action: Literal["accept", "deny"] | None = None,
        adom: list[dict[str, Any]] | None = None,
        adom_access: Literal["all", "specify"] | None = None,
        authorization_type: Literal["serial", "certificate"] | None = None,
        certificate: str | None = None,
        downstream_authorization: Literal["disable", "enable"] | None = None,
        ha_members: str | None = None,
        index: int | None = None,
        name: str | None = None,
        serial: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        trusted_list: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemCsfTrustedList", "CliGlobalSystemCsfTrustedListGetResponse"]
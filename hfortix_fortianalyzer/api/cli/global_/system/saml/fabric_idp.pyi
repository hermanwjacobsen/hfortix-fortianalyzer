"""Type stubs for cli.global.system.saml.fabric-idp"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSamlFabricIdpGetItem:
    """Item yielded when iterating over CliGlobalSystemSamlFabricIdpGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def dev_id(self) -> str: ...
    @property
    def idp_cert(self) -> str: ...
    @property
    def idp_entity_id(self) -> str: ...
    @property
    def idp_single_logout_url(self) -> str: ...
    @property
    def idp_single_sign_on_url(self) -> str: ...
    @property
    def idp_status(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemSamlFabricIdpGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSamlFabricIdpGet endpoint with autocomplete support."""

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
    def dev_id(self) -> str | None:
        """Field: dev-id"""
        ...

    @property
    def idp_cert(self) -> str | None:
        """Field: idp-cert"""
        ...

    @property
    def idp_entity_id(self) -> str | None:
        """Field: idp-entity-id"""
        ...

    @property
    def idp_single_logout_url(self) -> str | None:
        """Field: idp-single-logout-url"""
        ...

    @property
    def idp_single_sign_on_url(self) -> str | None:
        """Field: idp-single-sign-on-url"""
        ...

    @property
    def idp_status(self) -> Literal["disable", "enable"] | None:
        """Field: idp-status"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSamlFabricIdpGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSamlFabricIdp:
    """FortiAnalyzer endpoint: cli.global.system.saml.fabric-idp"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        fabric_idp: int | str | None = None,
        fields: list[Literal["dev-id", "idp-cert", "idp-entity-id", "idp-single-logout-url", "idp-single-sign-on-url", "idp-status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemSamlFabricIdpGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        fabric_idp: int | str | None = None,
        dev_id: str | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        idp_status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        fabric_idp: int | str | None = None,
        dev_id: str | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        idp_status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        fabric_idp: int | str | None = None,
        dev_id: str | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        idp_status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        fabric_idp: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemSamlFabricIdp", "CliGlobalSystemSamlFabricIdpGetResponse"]
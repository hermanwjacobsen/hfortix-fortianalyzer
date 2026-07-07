"""Type stubs for cli.global.system.saml.service-providers"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSamlServiceProvidersGetItem:
    """Item yielded when iterating over CliGlobalSystemSamlServiceProvidersGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def idp_entity_id(self) -> str: ...
    @property
    def idp_single_logout_url(self) -> str: ...
    @property
    def idp_single_sign_on_url(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def prefix(self) -> str: ...
    @property
    def sp_adom(self) -> str: ...
    @property
    def sp_cert(self) -> str: ...
    @property
    def sp_entity_id(self) -> str: ...
    @property
    def sp_profile(self) -> str: ...
    @property
    def sp_single_logout_url(self) -> str: ...
    @property
    def sp_single_sign_on_url(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemSamlServiceProvidersGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSamlServiceProvidersGet endpoint with autocomplete support."""

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
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def prefix(self) -> str | None:
        """Field: prefix"""
        ...

    @property
    def sp_adom(self) -> str | None:
        """Field: sp-adom"""
        ...

    @property
    def sp_cert(self) -> str | None:
        """Field: sp-cert"""
        ...

    @property
    def sp_entity_id(self) -> str | None:
        """Field: sp-entity-id"""
        ...

    @property
    def sp_profile(self) -> str | None:
        """Field: sp-profile"""
        ...

    @property
    def sp_single_logout_url(self) -> str | None:
        """Field: sp-single-logout-url"""
        ...

    @property
    def sp_single_sign_on_url(self) -> str | None:
        """Field: sp-single-sign-on-url"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSamlServiceProvidersGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSamlServiceProviders:
    """FortiAnalyzer endpoint: cli.global.system.saml.service-providers"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        service_providers: int | str | None = None,
        fields: list[Literal["idp-entity-id", "idp-single-logout-url", "idp-single-sign-on-url", "name", "prefix", "sp-adom", "sp-cert", "sp-entity-id", "sp-profile", "sp-single-logout-url", "sp-single-sign-on-url"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemSamlServiceProvidersGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        service_providers: int | str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        name: str | None = None,
        prefix: str | None = None,
        sp_adom: str | None = None,
        sp_cert: str | None = None,
        sp_entity_id: str | None = None,
        sp_profile: str | None = None,
        sp_single_logout_url: str | None = None,
        sp_single_sign_on_url: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        service_providers: int | str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        name: str | None = None,
        prefix: str | None = None,
        sp_adom: str | None = None,
        sp_cert: str | None = None,
        sp_entity_id: str | None = None,
        sp_profile: str | None = None,
        sp_single_logout_url: str | None = None,
        sp_single_sign_on_url: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        service_providers: int | str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        name: str | None = None,
        prefix: str | None = None,
        sp_adom: str | None = None,
        sp_cert: str | None = None,
        sp_entity_id: str | None = None,
        sp_profile: str | None = None,
        sp_single_logout_url: str | None = None,
        sp_single_sign_on_url: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        service_providers: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemSamlServiceProviders", "CliGlobalSystemSamlServiceProvidersGetResponse"]
"""Type stubs for cli.global.system.saml"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSamlGetItem:
    """Item yielded when iterating over CliGlobalSystemSamlGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def acs_url(self) -> str: ...
    @property
    def auth_request_signed(self) -> Literal["disable", "enable"]: ...
    @property
    def cert(self) -> str: ...
    @property
    def default_profile(self) -> str: ...
    @property
    def entity_id(self) -> str: ...
    @property
    def fabric_idp(self) -> list[FabricIdpItem]: ...
    @property
    def forticloud_sso(self) -> Literal["disable", "enable"]: ...
    @property
    def ha_config_sync(self) -> Literal["disable", "enable"]: ...
    @property
    def idp_cert(self) -> str: ...
    @property
    def idp_entity_id(self) -> str: ...
    @property
    def idp_single_logout_url(self) -> str: ...
    @property
    def idp_single_sign_on_url(self) -> str: ...
    @property
    def login_auto_redirect(self) -> Literal["disable", "enable"]: ...
    @property
    def logout_request_signed(self) -> Literal["disable", "enable"]: ...
    @property
    def logout_response_signed(self) -> Literal["disable", "enable"]: ...
    @property
    def role(self) -> Literal["IDP", "SP", "FAB-SP"]: ...
    @property
    def server_address(self) -> str: ...
    @property
    def service_providers(self) -> list[ServiceProvidersItem]: ...
    @property
    def sls_url(self) -> str: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def user_auto_create(self) -> Literal["disable", "enable"]: ...
    @property
    def want_assertions_signed(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class FabricIdpItem:
    """Nested item type for fabric-idp array."""

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

class ServiceProvidersItem:
    """Nested item type for service-providers array."""

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


class CliGlobalSystemSamlGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSamlGet endpoint with autocomplete support."""

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
    def acs_url(self) -> str | None:
        """Field: acs-url"""
        ...

    @property
    def auth_request_signed(self) -> Literal["disable", "enable"] | None:
        """Field: auth-request-signed"""
        ...

    @property
    def cert(self) -> str | None:
        """Field: cert"""
        ...

    @property
    def default_profile(self) -> str | None:
        """Field: default-profile"""
        ...

    @property
    def entity_id(self) -> str | None:
        """Field: entity-id"""
        ...

    @property
    def fabric_idp(self) -> list[FabricIdpItem]:
        """Field: fabric-idp"""
        ...

    @property
    def forticloud_sso(self) -> Literal["disable", "enable"] | None:
        """Field: forticloud-sso"""
        ...

    @property
    def ha_config_sync(self) -> Literal["disable", "enable"] | None:
        """Field: ha-config-sync"""
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
    def login_auto_redirect(self) -> Literal["disable", "enable"] | None:
        """Field: login-auto-redirect"""
        ...

    @property
    def logout_request_signed(self) -> Literal["disable", "enable"] | None:
        """Field: logout-request-signed"""
        ...

    @property
    def logout_response_signed(self) -> Literal["disable", "enable"] | None:
        """Field: logout-response-signed"""
        ...

    @property
    def role(self) -> Literal["IDP", "SP", "FAB-SP"] | None:
        """Field: role"""
        ...

    @property
    def server_address(self) -> str | None:
        """Field: server-address"""
        ...

    @property
    def service_providers(self) -> list[ServiceProvidersItem]:
        """Field: service-providers"""
        ...

    @property
    def sls_url(self) -> str | None:
        """Field: sls-url"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def user_auto_create(self) -> Literal["disable", "enable"] | None:
        """Field: user-auto-create"""
        ...

    @property
    def want_assertions_signed(self) -> Literal["disable", "enable"] | None:
        """Field: want-assertions-signed"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSamlGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSaml:
    """FortiAnalyzer endpoint: cli.global.system.saml"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemSamlGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        acs_url: str | None = None,
        auth_request_signed: Literal["disable", "enable"] | None = None,
        cert: str | None = None,
        default_profile: str | None = None,
        entity_id: str | None = None,
        fabric_idp: list[dict[str, Any]] | None = None,
        forticloud_sso: Literal["disable", "enable"] | None = None,
        ha_config_sync: Literal["disable", "enable"] | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        login_auto_redirect: Literal["disable", "enable"] | None = None,
        logout_request_signed: Literal["disable", "enable"] | None = None,
        logout_response_signed: Literal["disable", "enable"] | None = None,
        role: Literal["IDP", "SP", "FAB-SP"] | None = None,
        server_address: str | None = None,
        service_providers: list[dict[str, Any]] | None = None,
        sls_url: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        user_auto_create: Literal["disable", "enable"] | None = None,
        want_assertions_signed: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        acs_url: str | None = None,
        auth_request_signed: Literal["disable", "enable"] | None = None,
        cert: str | None = None,
        default_profile: str | None = None,
        entity_id: str | None = None,
        fabric_idp: list[dict[str, Any]] | None = None,
        forticloud_sso: Literal["disable", "enable"] | None = None,
        ha_config_sync: Literal["disable", "enable"] | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        login_auto_redirect: Literal["disable", "enable"] | None = None,
        logout_request_signed: Literal["disable", "enable"] | None = None,
        logout_response_signed: Literal["disable", "enable"] | None = None,
        role: Literal["IDP", "SP", "FAB-SP"] | None = None,
        server_address: str | None = None,
        service_providers: list[dict[str, Any]] | None = None,
        sls_url: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        user_auto_create: Literal["disable", "enable"] | None = None,
        want_assertions_signed: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemSaml", "CliGlobalSystemSamlGetResponse"]
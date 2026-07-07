"""
FortiAnalyzer API endpoint: cli.global.system.saml

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSaml:
    """
    FortiAnalyzer endpoint: cli.global.system.saml
    
    
    Available methods: get, set, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/saml"
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        auth_request_signed: Literal["disable", "enable"] | None = None,
        default_profile: str | None = None,
        forticloud_sso: Literal["disable", "enable"] | None = None,
        ha_config_sync: Literal["disable", "enable"] | None = None,
        login_auto_redirect: Literal["disable", "enable"] | None = None,
        logout_request_signed: Literal["disable", "enable"] | None = None,
        logout_response_signed: Literal["disable", "enable"] | None = None,
        role: Literal["IDP", "SP", "FAB-SP"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        user_auto_create: Literal["disable", "enable"] | None = None,
        want_assertions_signed: Literal["disable", "enable"] | None = None,
        acs_url: str | None = None,
        cert: str | None = None,
        entity_id: str | None = None,
        fabric_idp: list[Any] | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        server_address: str | None = None,
        service_providers: list[Any] | None = None,
        sls_url: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            acs_url: acs-url parameter
            auth_request_signed: auth-request-signed parameter
            cert: cert parameter
            default_profile: default-profile parameter
            entity_id: entity-id parameter
            fabric_idp: fabric-idp parameter
            forticloud_sso: forticloud-sso parameter
            ha_config_sync: ha-config-sync parameter
            idp_cert: idp-cert parameter
            idp_entity_id: idp-entity-id parameter
            ... (12 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/saml"
        
        # Build data payload
        data = {}
        if acs_url is not None:
            data["acs-url"] = acs_url
        if auth_request_signed is not None:
            data["auth-request-signed"] = auth_request_signed
        if cert is not None:
            data["cert"] = cert
        if default_profile is not None:
            data["default-profile"] = default_profile
        if entity_id is not None:
            data["entity-id"] = entity_id
        if fabric_idp is not None:
            data["fabric-idp"] = fabric_idp
        if forticloud_sso is not None:
            data["forticloud-sso"] = forticloud_sso
        if ha_config_sync is not None:
            data["ha-config-sync"] = ha_config_sync
        if idp_cert is not None:
            data["idp-cert"] = idp_cert
        if idp_entity_id is not None:
            data["idp-entity-id"] = idp_entity_id
        if idp_single_logout_url is not None:
            data["idp-single-logout-url"] = idp_single_logout_url
        if idp_single_sign_on_url is not None:
            data["idp-single-sign-on-url"] = idp_single_sign_on_url
        if login_auto_redirect is not None:
            data["login-auto-redirect"] = login_auto_redirect
        if logout_request_signed is not None:
            data["logout-request-signed"] = logout_request_signed
        if logout_response_signed is not None:
            data["logout-response-signed"] = logout_response_signed
        if role is not None:
            data["role"] = role
        if server_address is not None:
            data["server-address"] = server_address
        if service_providers is not None:
            data["service-providers"] = service_providers
        if sls_url is not None:
            data["sls-url"] = sls_url
        if status is not None:
            data["status"] = status
        if user_auto_create is not None:
            data["user-auto-create"] = user_auto_create
        if want_assertions_signed is not None:
            data["want-assertions-signed"] = want_assertions_signed
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def update(
        self,
        auth_request_signed: Literal["disable", "enable"] | None = None,
        default_profile: str | None = None,
        forticloud_sso: Literal["disable", "enable"] | None = None,
        ha_config_sync: Literal["disable", "enable"] | None = None,
        login_auto_redirect: Literal["disable", "enable"] | None = None,
        logout_request_signed: Literal["disable", "enable"] | None = None,
        logout_response_signed: Literal["disable", "enable"] | None = None,
        role: Literal["IDP", "SP", "FAB-SP"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        user_auto_create: Literal["disable", "enable"] | None = None,
        want_assertions_signed: Literal["disable", "enable"] | None = None,
        acs_url: str | None = None,
        cert: str | None = None,
        entity_id: str | None = None,
        fabric_idp: list[Any] | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None,
        server_address: str | None = None,
        service_providers: list[Any] | None = None,
        sls_url: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            acs_url: acs-url parameter
            auth_request_signed: auth-request-signed parameter
            cert: cert parameter
            default_profile: default-profile parameter
            entity_id: entity-id parameter
            fabric_idp: fabric-idp parameter
            forticloud_sso: forticloud-sso parameter
            ha_config_sync: ha-config-sync parameter
            idp_cert: idp-cert parameter
            idp_entity_id: idp-entity-id parameter
            ... (12 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/saml"
        
        # Build data payload
        data = {}
        if acs_url is not None:
            data["acs-url"] = acs_url
        if auth_request_signed is not None:
            data["auth-request-signed"] = auth_request_signed
        if cert is not None:
            data["cert"] = cert
        if default_profile is not None:
            data["default-profile"] = default_profile
        if entity_id is not None:
            data["entity-id"] = entity_id
        if fabric_idp is not None:
            data["fabric-idp"] = fabric_idp
        if forticloud_sso is not None:
            data["forticloud-sso"] = forticloud_sso
        if ha_config_sync is not None:
            data["ha-config-sync"] = ha_config_sync
        if idp_cert is not None:
            data["idp-cert"] = idp_cert
        if idp_entity_id is not None:
            data["idp-entity-id"] = idp_entity_id
        if idp_single_logout_url is not None:
            data["idp-single-logout-url"] = idp_single_logout_url
        if idp_single_sign_on_url is not None:
            data["idp-single-sign-on-url"] = idp_single_sign_on_url
        if login_auto_redirect is not None:
            data["login-auto-redirect"] = login_auto_redirect
        if logout_request_signed is not None:
            data["logout-request-signed"] = logout_request_signed
        if logout_response_signed is not None:
            data["logout-response-signed"] = logout_response_signed
        if role is not None:
            data["role"] = role
        if server_address is not None:
            data["server-address"] = server_address
        if service_providers is not None:
            data["service-providers"] = service_providers
        if sls_url is not None:
            data["sls-url"] = sls_url
        if status is not None:
            data["status"] = status
        if user_auto_create is not None:
            data["user-auto-create"] = user_auto_create
        if want_assertions_signed is not None:
            data["want-assertions-signed"] = want_assertions_signed
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

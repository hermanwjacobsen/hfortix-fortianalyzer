"""
FortiAnalyzer API endpoint: cli.global.system.saml.service-providers

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSamlServiceProviders:
    """
    FortiAnalyzer endpoint: cli.global.system.saml.service-providers
    
    
    Available methods: get, add, set, update, delete
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(
        self,
        service_providers: int | str | None = None,
        fields: list[Literal["idp-entity-id", "idp-single-logout-url", "idp-single-sign-on-url", "name", "prefix", "sp-adom", "sp-cert", "sp-entity-id", "sp-profile", "sp-single-logout-url", "sp-single-sign-on-url"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            service_providers: service-providers parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if service_providers is not None:
            url = "/cli/global/system/saml/service-providers/{service-providers}"
            url = url.replace("{service-providers}", str(service_providers))
        else:
            url = "/cli/global/system/saml/service-providers"
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        if fields is not None and fields and not isinstance(fields[0], list):
            fields = [fields]
        
        request_params = {}
        if fields is not None:
            request_params["fields"] = fields
        if filter is not None:
            request_params["filter"] = filter
        if loadsub is not None:
            request_params["loadsub"] = loadsub
        if option is not None:
            request_params["option"] = option
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            **request_params
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

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
        sp_single_sign_on_url: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            service_providers: service-providers parameter
            idp_entity_id: idp-entity-id parameter
            idp_single_logout_url: idp-single-logout-url parameter
            idp_single_sign_on_url: idp-single-sign-on-url parameter
            name: name parameter
            prefix: prefix parameter
            sp_adom: sp-adom parameter
            sp_cert: sp-cert parameter
            sp_entity_id: sp-entity-id parameter
            sp_profile: sp-profile parameter
            sp_single_logout_url: sp-single-logout-url parameter
            ... (1 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/saml/service-providers"
        
        # Build data payload
        data = {}
        if idp_entity_id is not None:
            data["idp-entity-id"] = idp_entity_id
        if idp_single_logout_url is not None:
            data["idp-single-logout-url"] = idp_single_logout_url
        if idp_single_sign_on_url is not None:
            data["idp-single-sign-on-url"] = idp_single_sign_on_url
        if name is not None:
            data["name"] = name
        if prefix is not None:
            data["prefix"] = prefix
        if sp_adom is not None:
            data["sp-adom"] = sp_adom
        if sp_cert is not None:
            data["sp-cert"] = sp_cert
        if sp_entity_id is not None:
            data["sp-entity-id"] = sp_entity_id
        if sp_profile is not None:
            data["sp-profile"] = sp_profile
        if sp_single_logout_url is not None:
            data["sp-single-logout-url"] = sp_single_logout_url
        if sp_single_sign_on_url is not None:
            data["sp-single-sign-on-url"] = sp_single_sign_on_url
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

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
        sp_single_sign_on_url: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            service_providers: service-providers parameter
            idp_entity_id: idp-entity-id parameter
            idp_single_logout_url: idp-single-logout-url parameter
            idp_single_sign_on_url: idp-single-sign-on-url parameter
            name: name parameter
            prefix: prefix parameter
            sp_adom: sp-adom parameter
            sp_cert: sp-cert parameter
            sp_entity_id: sp-entity-id parameter
            sp_profile: sp-profile parameter
            sp_single_logout_url: sp-single-logout-url parameter
            ... (1 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if service_providers is not None:
            url = "/cli/global/system/saml/service-providers/{service-providers}"
            url = url.replace("{service-providers}", str(service_providers))
        else:
            url = "/cli/global/system/saml/service-providers"
        
        # Build data payload
        data = {}
        if idp_entity_id is not None:
            data["idp-entity-id"] = idp_entity_id
        if idp_single_logout_url is not None:
            data["idp-single-logout-url"] = idp_single_logout_url
        if idp_single_sign_on_url is not None:
            data["idp-single-sign-on-url"] = idp_single_sign_on_url
        if name is not None:
            data["name"] = name
        if prefix is not None:
            data["prefix"] = prefix
        if sp_adom is not None:
            data["sp-adom"] = sp_adom
        if sp_cert is not None:
            data["sp-cert"] = sp_cert
        if sp_entity_id is not None:
            data["sp-entity-id"] = sp_entity_id
        if sp_profile is not None:
            data["sp-profile"] = sp_profile
        if sp_single_logout_url is not None:
            data["sp-single-logout-url"] = sp_single_logout_url
        if sp_single_sign_on_url is not None:
            data["sp-single-sign-on-url"] = sp_single_sign_on_url
        
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
        sp_single_sign_on_url: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            service_providers: service-providers parameter
            idp_entity_id: idp-entity-id parameter
            idp_single_logout_url: idp-single-logout-url parameter
            idp_single_sign_on_url: idp-single-sign-on-url parameter
            name: name parameter
            prefix: prefix parameter
            sp_adom: sp-adom parameter
            sp_cert: sp-cert parameter
            sp_entity_id: sp-entity-id parameter
            sp_profile: sp-profile parameter
            sp_single_logout_url: sp-single-logout-url parameter
            ... (1 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if service_providers is not None:
            url = "/cli/global/system/saml/service-providers/{service-providers}"
            url = url.replace("{service-providers}", str(service_providers))
        else:
            url = "/cli/global/system/saml/service-providers"
        
        # Build data payload
        data = {}
        if idp_entity_id is not None:
            data["idp-entity-id"] = idp_entity_id
        if idp_single_logout_url is not None:
            data["idp-single-logout-url"] = idp_single_logout_url
        if idp_single_sign_on_url is not None:
            data["idp-single-sign-on-url"] = idp_single_sign_on_url
        if name is not None:
            data["name"] = name
        if prefix is not None:
            data["prefix"] = prefix
        if sp_adom is not None:
            data["sp-adom"] = sp_adom
        if sp_cert is not None:
            data["sp-cert"] = sp_cert
        if sp_entity_id is not None:
            data["sp-entity-id"] = sp_entity_id
        if sp_profile is not None:
            data["sp-profile"] = sp_profile
        if sp_single_logout_url is not None:
            data["sp-single-logout-url"] = sp_single_logout_url
        if sp_single_sign_on_url is not None:
            data["sp-single-sign-on-url"] = sp_single_sign_on_url
        
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

    def delete(self, service_providers: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            service_providers: service-providers parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if service_providers is not None:
            url = "/cli/global/system/saml/service-providers/{service-providers}"
            url = url.replace("{service-providers}", str(service_providers))
        else:
            url = "/cli/global/system/saml/service-providers"
        
        data = {}
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

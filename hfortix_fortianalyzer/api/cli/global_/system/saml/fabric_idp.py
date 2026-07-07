"""
FortiAnalyzer API endpoint: cli.global.system.saml.fabric-idp

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSamlFabricIdp:
    """
    FortiAnalyzer endpoint: cli.global.system.saml.fabric-idp
    
    
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
        fabric_idp: int | str | None = None,
        fields: list[Literal["dev-id", "idp-cert", "idp-entity-id", "idp-single-logout-url", "idp-single-sign-on-url", "idp-status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            fabric_idp: fabric-idp parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if fabric_idp is not None:
            url = "/cli/global/system/saml/fabric-idp/{fabric-idp}"
            url = url.replace("{fabric-idp}", str(fabric_idp))
        else:
            url = "/cli/global/system/saml/fabric-idp"
        
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
        fabric_idp: int | str | None = None,
        idp_status: Literal["disable", "enable"] | None = None,
        dev_id: str | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            fabric_idp: fabric-idp parameter
            dev_id: dev-id parameter
            idp_cert: idp-cert parameter
            idp_entity_id: idp-entity-id parameter
            idp_single_logout_url: idp-single-logout-url parameter
            idp_single_sign_on_url: idp-single-sign-on-url parameter
            idp_status: idp-status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/saml/fabric-idp"
        
        # Build data payload
        data = {}
        if dev_id is not None:
            data["dev-id"] = dev_id
        if idp_cert is not None:
            data["idp-cert"] = idp_cert
        if idp_entity_id is not None:
            data["idp-entity-id"] = idp_entity_id
        if idp_single_logout_url is not None:
            data["idp-single-logout-url"] = idp_single_logout_url
        if idp_single_sign_on_url is not None:
            data["idp-single-sign-on-url"] = idp_single_sign_on_url
        if idp_status is not None:
            data["idp-status"] = idp_status
        
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
        fabric_idp: int | str | None = None,
        idp_status: Literal["disable", "enable"] | None = None,
        dev_id: str | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            fabric_idp: fabric-idp parameter
            dev_id: dev-id parameter
            idp_cert: idp-cert parameter
            idp_entity_id: idp-entity-id parameter
            idp_single_logout_url: idp-single-logout-url parameter
            idp_single_sign_on_url: idp-single-sign-on-url parameter
            idp_status: idp-status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if fabric_idp is not None:
            url = "/cli/global/system/saml/fabric-idp/{fabric-idp}"
            url = url.replace("{fabric-idp}", str(fabric_idp))
        else:
            url = "/cli/global/system/saml/fabric-idp"
        
        # Build data payload
        data = {}
        if dev_id is not None:
            data["dev-id"] = dev_id
        if idp_cert is not None:
            data["idp-cert"] = idp_cert
        if idp_entity_id is not None:
            data["idp-entity-id"] = idp_entity_id
        if idp_single_logout_url is not None:
            data["idp-single-logout-url"] = idp_single_logout_url
        if idp_single_sign_on_url is not None:
            data["idp-single-sign-on-url"] = idp_single_sign_on_url
        if idp_status is not None:
            data["idp-status"] = idp_status
        
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
        fabric_idp: int | str | None = None,
        idp_status: Literal["disable", "enable"] | None = None,
        dev_id: str | None = None,
        idp_cert: str | None = None,
        idp_entity_id: str | None = None,
        idp_single_logout_url: str | None = None,
        idp_single_sign_on_url: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            fabric_idp: fabric-idp parameter
            dev_id: dev-id parameter
            idp_cert: idp-cert parameter
            idp_entity_id: idp-entity-id parameter
            idp_single_logout_url: idp-single-logout-url parameter
            idp_single_sign_on_url: idp-single-sign-on-url parameter
            idp_status: idp-status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if fabric_idp is not None:
            url = "/cli/global/system/saml/fabric-idp/{fabric-idp}"
            url = url.replace("{fabric-idp}", str(fabric_idp))
        else:
            url = "/cli/global/system/saml/fabric-idp"
        
        # Build data payload
        data = {}
        if dev_id is not None:
            data["dev-id"] = dev_id
        if idp_cert is not None:
            data["idp-cert"] = idp_cert
        if idp_entity_id is not None:
            data["idp-entity-id"] = idp_entity_id
        if idp_single_logout_url is not None:
            data["idp-single-logout-url"] = idp_single_logout_url
        if idp_single_sign_on_url is not None:
            data["idp-single-sign-on-url"] = idp_single_sign_on_url
        if idp_status is not None:
            data["idp-status"] = idp_status
        
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

    def delete(self, fabric_idp: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            fabric_idp: fabric-idp parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if fabric_idp is not None:
            url = "/cli/global/system/saml/fabric-idp/{fabric-idp}"
            url = url.replace("{fabric-idp}", str(fabric_idp))
        else:
            url = "/cli/global/system/saml/fabric-idp"
        
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

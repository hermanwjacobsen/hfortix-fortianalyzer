"""
FortiAnalyzer API endpoint: cli.global.system.admin.tacacs

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminTacacs:
    """
    FortiAnalyzer endpoint: cli.global.system.admin.tacacs
    
    
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
        tacacs: int | str | None = None,
        fields: list[Literal["authen-type", "authorization", "key", "name", "port", "secondary-key", "secondary-server", "server", "src-ip", "tertiary-key", "tertiary-server"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            tacacs: tacacs parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if tacacs is not None:
            url = "/cli/global/system/admin/tacacs/{tacacs}"
            url = url.replace("{tacacs}", str(tacacs))
        else:
            url = "/cli/global/system/admin/tacacs"
        
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
        tacacs: int | str | None = None,
        authen_type: Literal["auto", "ascii", "pap", "chap", "mschap"] | None = None,
        authorization: Literal["disable", "enable"] | None = None,
        port: int | None = None,
        key: list[Any] | None = None,
        name: str | None = None,
        secondary_key: list[Any] | None = None,
        secondary_server: str | None = None,
        server: str | None = None,
        src_ip: str | None = None,
        tertiary_key: list[Any] | None = None,
        tertiary_server: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            tacacs: tacacs parameter
            authen_type: authen-type parameter
            authorization: authorization parameter
            key: key parameter
            name: name parameter
            port: port parameter
            secondary_key: secondary-key parameter
            secondary_server: secondary-server parameter
            server: server parameter
            src_ip: src-ip parameter
            tertiary_key: tertiary-key parameter
            ... (1 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/admin/tacacs"
        
        # Build data payload
        data = {}
        if authen_type is not None:
            data["authen-type"] = authen_type
        if authorization is not None:
            data["authorization"] = authorization
        if key is not None:
            data["key"] = key
        if name is not None:
            data["name"] = name
        if port is not None:
            data["port"] = port
        if secondary_key is not None:
            data["secondary-key"] = secondary_key
        if secondary_server is not None:
            data["secondary-server"] = secondary_server
        if server is not None:
            data["server"] = server
        if src_ip is not None:
            data["src-ip"] = src_ip
        if tertiary_key is not None:
            data["tertiary-key"] = tertiary_key
        if tertiary_server is not None:
            data["tertiary-server"] = tertiary_server
        
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
        tacacs: int | str | None = None,
        authen_type: Literal["auto", "ascii", "pap", "chap", "mschap"] | None = None,
        authorization: Literal["disable", "enable"] | None = None,
        port: int | None = None,
        key: list[Any] | None = None,
        name: str | None = None,
        secondary_key: list[Any] | None = None,
        secondary_server: str | None = None,
        server: str | None = None,
        src_ip: str | None = None,
        tertiary_key: list[Any] | None = None,
        tertiary_server: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            tacacs: tacacs parameter
            authen_type: authen-type parameter
            authorization: authorization parameter
            key: key parameter
            name: name parameter
            port: port parameter
            secondary_key: secondary-key parameter
            secondary_server: secondary-server parameter
            server: server parameter
            src_ip: src-ip parameter
            tertiary_key: tertiary-key parameter
            ... (1 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if tacacs is not None:
            url = "/cli/global/system/admin/tacacs/{tacacs}"
            url = url.replace("{tacacs}", str(tacacs))
        else:
            url = "/cli/global/system/admin/tacacs"
        
        # Build data payload
        data = {}
        if authen_type is not None:
            data["authen-type"] = authen_type
        if authorization is not None:
            data["authorization"] = authorization
        if key is not None:
            data["key"] = key
        if name is not None:
            data["name"] = name
        if port is not None:
            data["port"] = port
        if secondary_key is not None:
            data["secondary-key"] = secondary_key
        if secondary_server is not None:
            data["secondary-server"] = secondary_server
        if server is not None:
            data["server"] = server
        if src_ip is not None:
            data["src-ip"] = src_ip
        if tertiary_key is not None:
            data["tertiary-key"] = tertiary_key
        if tertiary_server is not None:
            data["tertiary-server"] = tertiary_server
        
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
        tacacs: int | str | None = None,
        authen_type: Literal["auto", "ascii", "pap", "chap", "mschap"] | None = None,
        authorization: Literal["disable", "enable"] | None = None,
        port: int | None = None,
        key: list[Any] | None = None,
        name: str | None = None,
        secondary_key: list[Any] | None = None,
        secondary_server: str | None = None,
        server: str | None = None,
        src_ip: str | None = None,
        tertiary_key: list[Any] | None = None,
        tertiary_server: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            tacacs: tacacs parameter
            authen_type: authen-type parameter
            authorization: authorization parameter
            key: key parameter
            name: name parameter
            port: port parameter
            secondary_key: secondary-key parameter
            secondary_server: secondary-server parameter
            server: server parameter
            src_ip: src-ip parameter
            tertiary_key: tertiary-key parameter
            ... (1 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if tacacs is not None:
            url = "/cli/global/system/admin/tacacs/{tacacs}"
            url = url.replace("{tacacs}", str(tacacs))
        else:
            url = "/cli/global/system/admin/tacacs"
        
        # Build data payload
        data = {}
        if authen_type is not None:
            data["authen-type"] = authen_type
        if authorization is not None:
            data["authorization"] = authorization
        if key is not None:
            data["key"] = key
        if name is not None:
            data["name"] = name
        if port is not None:
            data["port"] = port
        if secondary_key is not None:
            data["secondary-key"] = secondary_key
        if secondary_server is not None:
            data["secondary-server"] = secondary_server
        if server is not None:
            data["server"] = server
        if src_ip is not None:
            data["src-ip"] = src_ip
        if tertiary_key is not None:
            data["tertiary-key"] = tertiary_key
        if tertiary_server is not None:
            data["tertiary-server"] = tertiary_server
        
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

    def delete(self, tacacs: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            tacacs: tacacs parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if tacacs is not None:
            url = "/cli/global/system/admin/tacacs/{tacacs}"
            url = url.replace("{tacacs}", str(tacacs))
        else:
            url = "/cli/global/system/admin/tacacs"
        
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

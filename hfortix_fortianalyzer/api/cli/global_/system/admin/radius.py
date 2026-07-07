"""
FortiAnalyzer API endpoint: cli.global.system.admin.radius

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminRadius:
    """
    FortiAnalyzer endpoint: cli.global.system.admin.radius
    
    
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
        radius: int | str | None = None,
        fields: list[Literal["auth-type", "ca-cert", "client-cert", "message-authenticator", "name", "nas-ip", "port", "protocol", "secondary-secret", "secondary-server", "secret", "server"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            radius: radius parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if radius is not None:
            url = "/cli/global/system/admin/radius/{radius}"
            url = url.replace("{radius}", str(radius))
        else:
            url = "/cli/global/system/admin/radius"
        
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
        radius: int | str | None = None,
        auth_type: Literal["any", "pap", "chap", "mschap2"] | None = None,
        message_authenticator: Literal["optional", "require"] | None = None,
        nas_ip: str | None = None,
        port: int | None = None,
        protocol: Literal["udp", "tls"] | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        name: str | None = None,
        secondary_secret: list[Any] | None = None,
        secondary_server: str | None = None,
        secret: list[Any] | None = None,
        server: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            radius: radius parameter
            auth_type: auth-type parameter
            ca_cert: ca-cert parameter
            client_cert: client-cert parameter
            message_authenticator: message-authenticator parameter
            name: name parameter
            nas_ip: nas-ip parameter
            port: port parameter
            protocol: protocol parameter
            secondary_secret: secondary-secret parameter
            secondary_server: secondary-server parameter
            ... (2 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/admin/radius"
        
        # Build data payload
        data = {}
        if auth_type is not None:
            data["auth-type"] = auth_type
        if ca_cert is not None:
            data["ca-cert"] = ca_cert
        if client_cert is not None:
            data["client-cert"] = client_cert
        if message_authenticator is not None:
            data["message-authenticator"] = message_authenticator
        if name is not None:
            data["name"] = name
        if nas_ip is not None:
            data["nas-ip"] = nas_ip
        if port is not None:
            data["port"] = port
        if protocol is not None:
            data["protocol"] = protocol
        if secondary_secret is not None:
            data["secondary-secret"] = secondary_secret
        if secondary_server is not None:
            data["secondary-server"] = secondary_server
        if secret is not None:
            data["secret"] = secret
        if server is not None:
            data["server"] = server
        
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
        radius: int | str | None = None,
        auth_type: Literal["any", "pap", "chap", "mschap2"] | None = None,
        message_authenticator: Literal["optional", "require"] | None = None,
        nas_ip: str | None = None,
        port: int | None = None,
        protocol: Literal["udp", "tls"] | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        name: str | None = None,
        secondary_secret: list[Any] | None = None,
        secondary_server: str | None = None,
        secret: list[Any] | None = None,
        server: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            radius: radius parameter
            auth_type: auth-type parameter
            ca_cert: ca-cert parameter
            client_cert: client-cert parameter
            message_authenticator: message-authenticator parameter
            name: name parameter
            nas_ip: nas-ip parameter
            port: port parameter
            protocol: protocol parameter
            secondary_secret: secondary-secret parameter
            secondary_server: secondary-server parameter
            ... (2 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if radius is not None:
            url = "/cli/global/system/admin/radius/{radius}"
            url = url.replace("{radius}", str(radius))
        else:
            url = "/cli/global/system/admin/radius"
        
        # Build data payload
        data = {}
        if auth_type is not None:
            data["auth-type"] = auth_type
        if ca_cert is not None:
            data["ca-cert"] = ca_cert
        if client_cert is not None:
            data["client-cert"] = client_cert
        if message_authenticator is not None:
            data["message-authenticator"] = message_authenticator
        if name is not None:
            data["name"] = name
        if nas_ip is not None:
            data["nas-ip"] = nas_ip
        if port is not None:
            data["port"] = port
        if protocol is not None:
            data["protocol"] = protocol
        if secondary_secret is not None:
            data["secondary-secret"] = secondary_secret
        if secondary_server is not None:
            data["secondary-server"] = secondary_server
        if secret is not None:
            data["secret"] = secret
        if server is not None:
            data["server"] = server
        
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
        radius: int | str | None = None,
        auth_type: Literal["any", "pap", "chap", "mschap2"] | None = None,
        message_authenticator: Literal["optional", "require"] | None = None,
        nas_ip: str | None = None,
        port: int | None = None,
        protocol: Literal["udp", "tls"] | None = None,
        ca_cert: str | None = None,
        client_cert: str | None = None,
        name: str | None = None,
        secondary_secret: list[Any] | None = None,
        secondary_server: str | None = None,
        secret: list[Any] | None = None,
        server: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            radius: radius parameter
            auth_type: auth-type parameter
            ca_cert: ca-cert parameter
            client_cert: client-cert parameter
            message_authenticator: message-authenticator parameter
            name: name parameter
            nas_ip: nas-ip parameter
            port: port parameter
            protocol: protocol parameter
            secondary_secret: secondary-secret parameter
            secondary_server: secondary-server parameter
            ... (2 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if radius is not None:
            url = "/cli/global/system/admin/radius/{radius}"
            url = url.replace("{radius}", str(radius))
        else:
            url = "/cli/global/system/admin/radius"
        
        # Build data payload
        data = {}
        if auth_type is not None:
            data["auth-type"] = auth_type
        if ca_cert is not None:
            data["ca-cert"] = ca_cert
        if client_cert is not None:
            data["client-cert"] = client_cert
        if message_authenticator is not None:
            data["message-authenticator"] = message_authenticator
        if name is not None:
            data["name"] = name
        if nas_ip is not None:
            data["nas-ip"] = nas_ip
        if port is not None:
            data["port"] = port
        if protocol is not None:
            data["protocol"] = protocol
        if secondary_secret is not None:
            data["secondary-secret"] = secondary_secret
        if secondary_server is not None:
            data["secondary-server"] = secondary_server
        if secret is not None:
            data["secret"] = secret
        if server is not None:
            data["server"] = server
        
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

    def delete(self, radius: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            radius: radius parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if radius is not None:
            url = "/cli/global/system/admin/radius/{radius}"
            url = url.replace("{radius}", str(radius))
        else:
            url = "/cli/global/system/admin/radius"
        
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

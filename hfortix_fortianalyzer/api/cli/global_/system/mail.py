"""
FortiAnalyzer API endpoint: cli.global.system.mail

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemMail:
    """
    FortiAnalyzer endpoint: cli.global.system.mail
    
    
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
        mail: int | str | None = None,
        fields: list[Literal["auth", "auth-type", "from", "id", "local-cert", "oauth2-auth-scope", "oauth2-auth-server", "oauth2-client-id", "oauth2-client-secret", "passwd", "port", "secure-option", "server", "ssl-protocol", "user"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            mail: mail parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if mail is not None:
            url = "/cli/global/system/mail/{mail}"
            url = url.replace("{mail}", str(mail))
        else:
            url = "/cli/global/system/mail"
        
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
        mail: int | str | None = None,
        auth: Literal["disable", "enable"] | None = None,
        auth_type: Literal["psk", "certificate", "oauth2"] | None = None,
        port: int | None = None,
        secure_option: Literal["default", "none", "smtps", "starttls"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        from_: str | None = None,
        id: str | None = None,
        local_cert: str | None = None,
        oauth2_auth_scope: str | None = None,
        oauth2_auth_server: str | None = None,
        oauth2_client_id: str | None = None,
        oauth2_client_secret: list[Any] | None = None,
        passwd: list[Any] | None = None,
        server: str | None = None,
        user: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            mail: mail parameter
            auth: auth parameter
            auth_type: auth-type parameter
            from_: from parameter
            id: id parameter
            local_cert: local-cert parameter
            oauth2_auth_scope: oauth2-auth-scope parameter
            oauth2_auth_server: oauth2-auth-server parameter
            oauth2_client_id: oauth2-client-id parameter
            oauth2_client_secret: oauth2-client-secret parameter
            passwd: passwd parameter
            ... (5 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/mail"
        
        # Build data payload
        data = {}
        if auth is not None:
            data["auth"] = auth
        if auth_type is not None:
            data["auth-type"] = auth_type
        if from_ is not None:
            data["from"] = from_
        if id is not None:
            data["id"] = id
        if local_cert is not None:
            data["local-cert"] = local_cert
        if oauth2_auth_scope is not None:
            data["oauth2-auth-scope"] = oauth2_auth_scope
        if oauth2_auth_server is not None:
            data["oauth2-auth-server"] = oauth2_auth_server
        if oauth2_client_id is not None:
            data["oauth2-client-id"] = oauth2_client_id
        if oauth2_client_secret is not None:
            data["oauth2-client-secret"] = oauth2_client_secret
        if passwd is not None:
            data["passwd"] = passwd
        if port is not None:
            data["port"] = port
        if secure_option is not None:
            data["secure-option"] = secure_option
        if server is not None:
            data["server"] = server
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        if user is not None:
            data["user"] = user
        
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
        mail: int | str | None = None,
        auth: Literal["disable", "enable"] | None = None,
        auth_type: Literal["psk", "certificate", "oauth2"] | None = None,
        port: int | None = None,
        secure_option: Literal["default", "none", "smtps", "starttls"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        from_: str | None = None,
        id: str | None = None,
        local_cert: str | None = None,
        oauth2_auth_scope: str | None = None,
        oauth2_auth_server: str | None = None,
        oauth2_client_id: str | None = None,
        oauth2_client_secret: list[Any] | None = None,
        passwd: list[Any] | None = None,
        server: str | None = None,
        user: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            mail: mail parameter
            auth: auth parameter
            auth_type: auth-type parameter
            from_: from parameter
            id: id parameter
            local_cert: local-cert parameter
            oauth2_auth_scope: oauth2-auth-scope parameter
            oauth2_auth_server: oauth2-auth-server parameter
            oauth2_client_id: oauth2-client-id parameter
            oauth2_client_secret: oauth2-client-secret parameter
            passwd: passwd parameter
            ... (5 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if mail is not None:
            url = "/cli/global/system/mail/{mail}"
            url = url.replace("{mail}", str(mail))
        else:
            url = "/cli/global/system/mail"
        
        # Build data payload
        data = {}
        if auth is not None:
            data["auth"] = auth
        if auth_type is not None:
            data["auth-type"] = auth_type
        if from_ is not None:
            data["from"] = from_
        if id is not None:
            data["id"] = id
        if local_cert is not None:
            data["local-cert"] = local_cert
        if oauth2_auth_scope is not None:
            data["oauth2-auth-scope"] = oauth2_auth_scope
        if oauth2_auth_server is not None:
            data["oauth2-auth-server"] = oauth2_auth_server
        if oauth2_client_id is not None:
            data["oauth2-client-id"] = oauth2_client_id
        if oauth2_client_secret is not None:
            data["oauth2-client-secret"] = oauth2_client_secret
        if passwd is not None:
            data["passwd"] = passwd
        if port is not None:
            data["port"] = port
        if secure_option is not None:
            data["secure-option"] = secure_option
        if server is not None:
            data["server"] = server
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        if user is not None:
            data["user"] = user
        
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
        mail: int | str | None = None,
        auth: Literal["disable", "enable"] | None = None,
        auth_type: Literal["psk", "certificate", "oauth2"] | None = None,
        port: int | None = None,
        secure_option: Literal["default", "none", "smtps", "starttls"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        from_: str | None = None,
        id: str | None = None,
        local_cert: str | None = None,
        oauth2_auth_scope: str | None = None,
        oauth2_auth_server: str | None = None,
        oauth2_client_id: str | None = None,
        oauth2_client_secret: list[Any] | None = None,
        passwd: list[Any] | None = None,
        server: str | None = None,
        user: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            mail: mail parameter
            auth: auth parameter
            auth_type: auth-type parameter
            from_: from parameter
            id: id parameter
            local_cert: local-cert parameter
            oauth2_auth_scope: oauth2-auth-scope parameter
            oauth2_auth_server: oauth2-auth-server parameter
            oauth2_client_id: oauth2-client-id parameter
            oauth2_client_secret: oauth2-client-secret parameter
            passwd: passwd parameter
            ... (5 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if mail is not None:
            url = "/cli/global/system/mail/{mail}"
            url = url.replace("{mail}", str(mail))
        else:
            url = "/cli/global/system/mail"
        
        # Build data payload
        data = {}
        if auth is not None:
            data["auth"] = auth
        if auth_type is not None:
            data["auth-type"] = auth_type
        if from_ is not None:
            data["from"] = from_
        if id is not None:
            data["id"] = id
        if local_cert is not None:
            data["local-cert"] = local_cert
        if oauth2_auth_scope is not None:
            data["oauth2-auth-scope"] = oauth2_auth_scope
        if oauth2_auth_server is not None:
            data["oauth2-auth-server"] = oauth2_auth_server
        if oauth2_client_id is not None:
            data["oauth2-client-id"] = oauth2_client_id
        if oauth2_client_secret is not None:
            data["oauth2-client-secret"] = oauth2_client_secret
        if passwd is not None:
            data["passwd"] = passwd
        if port is not None:
            data["port"] = port
        if secure_option is not None:
            data["secure-option"] = secure_option
        if server is not None:
            data["server"] = server
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        if user is not None:
            data["user"] = user
        
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

    def delete(self, mail: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            mail: mail parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if mail is not None:
            url = "/cli/global/system/mail/{mail}"
            url = url.replace("{mail}", str(mail))
        else:
            url = "/cli/global/system/mail"
        
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

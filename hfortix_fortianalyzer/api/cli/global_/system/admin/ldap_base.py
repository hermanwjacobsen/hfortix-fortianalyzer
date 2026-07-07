"""
FortiAnalyzer API endpoint: cli.global.system.admin.ldap

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminLdap:
    """
    FortiAnalyzer endpoint: cli.global.system.admin.ldap
    
    
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
        ldap: int | str | None = None,
        fields: list[Literal["adom-access", "adom-attr", "attributes", "ca-cert", "cnid", "dn", "filter", "group", "memberof-attr", "name", "password", "port", "profile-attr", "secondary-server", "secure", "server", "ssl-protocol", "tertiary-server", "type", "username"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            ldap: ldap parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ldap is not None:
            url = "/cli/global/system/admin/ldap/{ldap}"
            url = url.replace("{ldap}", str(ldap))
        else:
            url = "/cli/global/system/admin/ldap"
        
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
        ldap: int | str | None = None,
        adom_access: Literal["all", "specify"] | None = None,
        attributes: str | None = None,
        cnid: str | None = None,
        filter: str | None = None,
        port: int | None = None,
        secure: Literal["disable", "starttls", "ldaps"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        type: Literal["simple", "anonymous", "regular"] | None = None,
        adom: list[Any] | None = None,
        adom_attr: str | None = None,
        ca_cert: str | None = None,
        dn: str | None = None,
        group: str | None = None,
        memberof_attr: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        profile_attr: str | None = None,
        secondary_server: str | None = None,
        server: str | None = None,
        tertiary_server: str | None = None,
        username: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            ldap: ldap parameter
            adom: adom parameter
            adom_access: adom-access parameter
            adom_attr: adom-attr parameter
            attributes: attributes parameter
            ca_cert: ca-cert parameter
            cnid: cnid parameter
            dn: dn parameter
            filter: filter parameter
            group: group parameter
            memberof_attr: memberof-attr parameter
            ... (11 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/admin/ldap"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if adom_access is not None:
            data["adom-access"] = adom_access
        if adom_attr is not None:
            data["adom-attr"] = adom_attr
        if attributes is not None:
            data["attributes"] = attributes
        if ca_cert is not None:
            data["ca-cert"] = ca_cert
        if cnid is not None:
            data["cnid"] = cnid
        if dn is not None:
            data["dn"] = dn
        if filter is not None:
            data["filter"] = filter
        if group is not None:
            data["group"] = group
        if memberof_attr is not None:
            data["memberof-attr"] = memberof_attr
        if name is not None:
            data["name"] = name
        if password is not None:
            data["password"] = password
        if port is not None:
            data["port"] = port
        if profile_attr is not None:
            data["profile-attr"] = profile_attr
        if secondary_server is not None:
            data["secondary-server"] = secondary_server
        if secure is not None:
            data["secure"] = secure
        if server is not None:
            data["server"] = server
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        if tertiary_server is not None:
            data["tertiary-server"] = tertiary_server
        if type is not None:
            data["type"] = type
        if username is not None:
            data["username"] = username
        
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
        ldap: int | str | None = None,
        adom_access: Literal["all", "specify"] | None = None,
        attributes: str | None = None,
        cnid: str | None = None,
        filter: str | None = None,
        port: int | None = None,
        secure: Literal["disable", "starttls", "ldaps"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        type: Literal["simple", "anonymous", "regular"] | None = None,
        adom: list[Any] | None = None,
        adom_attr: str | None = None,
        ca_cert: str | None = None,
        dn: str | None = None,
        group: str | None = None,
        memberof_attr: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        profile_attr: str | None = None,
        secondary_server: str | None = None,
        server: str | None = None,
        tertiary_server: str | None = None,
        username: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            ldap: ldap parameter
            adom: adom parameter
            adom_access: adom-access parameter
            adom_attr: adom-attr parameter
            attributes: attributes parameter
            ca_cert: ca-cert parameter
            cnid: cnid parameter
            dn: dn parameter
            filter: filter parameter
            group: group parameter
            memberof_attr: memberof-attr parameter
            ... (11 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ldap is not None:
            url = "/cli/global/system/admin/ldap/{ldap}"
            url = url.replace("{ldap}", str(ldap))
        else:
            url = "/cli/global/system/admin/ldap"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if adom_access is not None:
            data["adom-access"] = adom_access
        if adom_attr is not None:
            data["adom-attr"] = adom_attr
        if attributes is not None:
            data["attributes"] = attributes
        if ca_cert is not None:
            data["ca-cert"] = ca_cert
        if cnid is not None:
            data["cnid"] = cnid
        if dn is not None:
            data["dn"] = dn
        if filter is not None:
            data["filter"] = filter
        if group is not None:
            data["group"] = group
        if memberof_attr is not None:
            data["memberof-attr"] = memberof_attr
        if name is not None:
            data["name"] = name
        if password is not None:
            data["password"] = password
        if port is not None:
            data["port"] = port
        if profile_attr is not None:
            data["profile-attr"] = profile_attr
        if secondary_server is not None:
            data["secondary-server"] = secondary_server
        if secure is not None:
            data["secure"] = secure
        if server is not None:
            data["server"] = server
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        if tertiary_server is not None:
            data["tertiary-server"] = tertiary_server
        if type is not None:
            data["type"] = type
        if username is not None:
            data["username"] = username
        
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
        ldap: int | str | None = None,
        adom_access: Literal["all", "specify"] | None = None,
        attributes: str | None = None,
        cnid: str | None = None,
        filter: str | None = None,
        port: int | None = None,
        secure: Literal["disable", "starttls", "ldaps"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        type: Literal["simple", "anonymous", "regular"] | None = None,
        adom: list[Any] | None = None,
        adom_attr: str | None = None,
        ca_cert: str | None = None,
        dn: str | None = None,
        group: str | None = None,
        memberof_attr: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        profile_attr: str | None = None,
        secondary_server: str | None = None,
        server: str | None = None,
        tertiary_server: str | None = None,
        username: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            ldap: ldap parameter
            adom: adom parameter
            adom_access: adom-access parameter
            adom_attr: adom-attr parameter
            attributes: attributes parameter
            ca_cert: ca-cert parameter
            cnid: cnid parameter
            dn: dn parameter
            filter: filter parameter
            group: group parameter
            memberof_attr: memberof-attr parameter
            ... (11 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ldap is not None:
            url = "/cli/global/system/admin/ldap/{ldap}"
            url = url.replace("{ldap}", str(ldap))
        else:
            url = "/cli/global/system/admin/ldap"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if adom_access is not None:
            data["adom-access"] = adom_access
        if adom_attr is not None:
            data["adom-attr"] = adom_attr
        if attributes is not None:
            data["attributes"] = attributes
        if ca_cert is not None:
            data["ca-cert"] = ca_cert
        if cnid is not None:
            data["cnid"] = cnid
        if dn is not None:
            data["dn"] = dn
        if filter is not None:
            data["filter"] = filter
        if group is not None:
            data["group"] = group
        if memberof_attr is not None:
            data["memberof-attr"] = memberof_attr
        if name is not None:
            data["name"] = name
        if password is not None:
            data["password"] = password
        if port is not None:
            data["port"] = port
        if profile_attr is not None:
            data["profile-attr"] = profile_attr
        if secondary_server is not None:
            data["secondary-server"] = secondary_server
        if secure is not None:
            data["secure"] = secure
        if server is not None:
            data["server"] = server
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        if tertiary_server is not None:
            data["tertiary-server"] = tertiary_server
        if type is not None:
            data["type"] = type
        if username is not None:
            data["username"] = username
        
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

    def delete(self, ldap: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            ldap: ldap parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ldap is not None:
            url = "/cli/global/system/admin/ldap/{ldap}"
            url = url.replace("{ldap}", str(ldap))
        else:
            url = "/cli/global/system/admin/ldap"
        
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

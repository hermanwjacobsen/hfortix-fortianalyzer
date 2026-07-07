"""
FortiAnalyzer API endpoint: cli.global.system.snmp.user

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSnmpUser:
    """
    FortiAnalyzer endpoint: cli.global.system.snmp.user
    
    
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
        user: int | str | None = None,
        fields: list[Literal["auth-proto", "auth-pwd", "events", "name", "notify-hosts", "notify-hosts6", "notify-port", "priv-proto", "priv-pwd", "queries", "query-port", "security-level"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            user: user parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None:
            url = "/cli/global/system/snmp/user/{user}"
            url = url.replace("{user}", str(user))
        else:
            url = "/cli/global/system/snmp/user"
        
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
        user: int | str | None = None,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = None,
        notify_port: int | None = None,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = None,
        queries: Literal["disable", "enable"] | None = None,
        query_port: int | None = None,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = None,
        auth_pwd: list[Any] | None = None,
        events: list[Any] | None = None,
        name: str | None = None,
        notify_hosts: str | None = None,
        notify_hosts6: str | None = None,
        priv_pwd: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            user: user parameter
            auth_proto: auth-proto parameter
            auth_pwd: auth-pwd parameter
            events: events parameter
            name: name parameter
            notify_hosts: notify-hosts parameter
            notify_hosts6: notify-hosts6 parameter
            notify_port: notify-port parameter
            priv_proto: priv-proto parameter
            priv_pwd: priv-pwd parameter
            queries: queries parameter
            ... (2 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/snmp/user"
        
        # Build data payload
        data = {}
        if auth_proto is not None:
            data["auth-proto"] = auth_proto
        if auth_pwd is not None:
            data["auth-pwd"] = auth_pwd
        if events is not None:
            data["events"] = events
        if name is not None:
            data["name"] = name
        if notify_hosts is not None:
            data["notify-hosts"] = notify_hosts
        if notify_hosts6 is not None:
            data["notify-hosts6"] = notify_hosts6
        if notify_port is not None:
            data["notify-port"] = notify_port
        if priv_proto is not None:
            data["priv-proto"] = priv_proto
        if priv_pwd is not None:
            data["priv-pwd"] = priv_pwd
        if queries is not None:
            data["queries"] = queries
        if query_port is not None:
            data["query-port"] = query_port
        if security_level is not None:
            data["security-level"] = security_level
        
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
        user: int | str | None = None,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = None,
        notify_port: int | None = None,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = None,
        queries: Literal["disable", "enable"] | None = None,
        query_port: int | None = None,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = None,
        auth_pwd: list[Any] | None = None,
        events: list[Any] | None = None,
        name: str | None = None,
        notify_hosts: str | None = None,
        notify_hosts6: str | None = None,
        priv_pwd: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            user: user parameter
            auth_proto: auth-proto parameter
            auth_pwd: auth-pwd parameter
            events: events parameter
            name: name parameter
            notify_hosts: notify-hosts parameter
            notify_hosts6: notify-hosts6 parameter
            notify_port: notify-port parameter
            priv_proto: priv-proto parameter
            priv_pwd: priv-pwd parameter
            queries: queries parameter
            ... (2 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None:
            url = "/cli/global/system/snmp/user/{user}"
            url = url.replace("{user}", str(user))
        else:
            url = "/cli/global/system/snmp/user"
        
        # Build data payload
        data = {}
        if auth_proto is not None:
            data["auth-proto"] = auth_proto
        if auth_pwd is not None:
            data["auth-pwd"] = auth_pwd
        if events is not None:
            data["events"] = events
        if name is not None:
            data["name"] = name
        if notify_hosts is not None:
            data["notify-hosts"] = notify_hosts
        if notify_hosts6 is not None:
            data["notify-hosts6"] = notify_hosts6
        if notify_port is not None:
            data["notify-port"] = notify_port
        if priv_proto is not None:
            data["priv-proto"] = priv_proto
        if priv_pwd is not None:
            data["priv-pwd"] = priv_pwd
        if queries is not None:
            data["queries"] = queries
        if query_port is not None:
            data["query-port"] = query_port
        if security_level is not None:
            data["security-level"] = security_level
        
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
        user: int | str | None = None,
        auth_proto: Literal["md5", "sha", "sha224", "sha256", "sha384", "sha512"] | None = None,
        notify_port: int | None = None,
        priv_proto: Literal["aes", "des", "aes256", "aes256cisco"] | None = None,
        queries: Literal["disable", "enable"] | None = None,
        query_port: int | None = None,
        security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = None,
        auth_pwd: list[Any] | None = None,
        events: list[Any] | None = None,
        name: str | None = None,
        notify_hosts: str | None = None,
        notify_hosts6: str | None = None,
        priv_pwd: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            user: user parameter
            auth_proto: auth-proto parameter
            auth_pwd: auth-pwd parameter
            events: events parameter
            name: name parameter
            notify_hosts: notify-hosts parameter
            notify_hosts6: notify-hosts6 parameter
            notify_port: notify-port parameter
            priv_proto: priv-proto parameter
            priv_pwd: priv-pwd parameter
            queries: queries parameter
            ... (2 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None:
            url = "/cli/global/system/snmp/user/{user}"
            url = url.replace("{user}", str(user))
        else:
            url = "/cli/global/system/snmp/user"
        
        # Build data payload
        data = {}
        if auth_proto is not None:
            data["auth-proto"] = auth_proto
        if auth_pwd is not None:
            data["auth-pwd"] = auth_pwd
        if events is not None:
            data["events"] = events
        if name is not None:
            data["name"] = name
        if notify_hosts is not None:
            data["notify-hosts"] = notify_hosts
        if notify_hosts6 is not None:
            data["notify-hosts6"] = notify_hosts6
        if notify_port is not None:
            data["notify-port"] = notify_port
        if priv_proto is not None:
            data["priv-proto"] = priv_proto
        if priv_pwd is not None:
            data["priv-pwd"] = priv_pwd
        if queries is not None:
            data["queries"] = queries
        if query_port is not None:
            data["query-port"] = query_port
        if security_level is not None:
            data["security-level"] = security_level
        
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

    def delete(self, user: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            user: user parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None:
            url = "/cli/global/system/snmp/user/{user}"
            url = url.replace("{user}", str(user))
        else:
            url = "/cli/global/system/snmp/user"
        
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

"""
FortiAnalyzer API endpoint: cli.global.system.syslog

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSyslog:
    """
    FortiAnalyzer endpoint: cli.global.system.syslog
    
    
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
        syslog: int | str | None = None,
        fields: list[Literal["ip", "local-cert", "name", "peer-cert-cn", "port", "reliable", "secure-connection", "ssl-protocol"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            syslog: syslog parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if syslog is not None:
            url = "/cli/global/system/syslog/{syslog}"
            url = url.replace("{syslog}", str(syslog))
        else:
            url = "/cli/global/system/syslog"
        
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
        syslog: int | str | None = None,
        local_cert: str | None = None,
        port: int | None = None,
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        ip: str | None = None,
        name: str | None = None,
        peer_cert_cn: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            syslog: syslog parameter
            ip: ip parameter
            local_cert: local-cert parameter
            name: name parameter
            peer_cert_cn: peer-cert-cn parameter
            port: port parameter
            reliable: reliable parameter
            secure_connection: secure-connection parameter
            ssl_protocol: ssl-protocol parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/syslog"
        
        # Build data payload
        data = {}
        if ip is not None:
            data["ip"] = ip
        if local_cert is not None:
            data["local-cert"] = local_cert
        if name is not None:
            data["name"] = name
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if port is not None:
            data["port"] = port
        if reliable is not None:
            data["reliable"] = reliable
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        
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
        syslog: int | str | None = None,
        local_cert: str | None = None,
        port: int | None = None,
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        ip: str | None = None,
        name: str | None = None,
        peer_cert_cn: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            syslog: syslog parameter
            ip: ip parameter
            local_cert: local-cert parameter
            name: name parameter
            peer_cert_cn: peer-cert-cn parameter
            port: port parameter
            reliable: reliable parameter
            secure_connection: secure-connection parameter
            ssl_protocol: ssl-protocol parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if syslog is not None:
            url = "/cli/global/system/syslog/{syslog}"
            url = url.replace("{syslog}", str(syslog))
        else:
            url = "/cli/global/system/syslog"
        
        # Build data payload
        data = {}
        if ip is not None:
            data["ip"] = ip
        if local_cert is not None:
            data["local-cert"] = local_cert
        if name is not None:
            data["name"] = name
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if port is not None:
            data["port"] = port
        if reliable is not None:
            data["reliable"] = reliable
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        
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
        syslog: int | str | None = None,
        local_cert: str | None = None,
        port: int | None = None,
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        ip: str | None = None,
        name: str | None = None,
        peer_cert_cn: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            syslog: syslog parameter
            ip: ip parameter
            local_cert: local-cert parameter
            name: name parameter
            peer_cert_cn: peer-cert-cn parameter
            port: port parameter
            reliable: reliable parameter
            secure_connection: secure-connection parameter
            ssl_protocol: ssl-protocol parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if syslog is not None:
            url = "/cli/global/system/syslog/{syslog}"
            url = url.replace("{syslog}", str(syslog))
        else:
            url = "/cli/global/system/syslog"
        
        # Build data payload
        data = {}
        if ip is not None:
            data["ip"] = ip
        if local_cert is not None:
            data["local-cert"] = local_cert
        if name is not None:
            data["name"] = name
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if port is not None:
            data["port"] = port
        if reliable is not None:
            data["reliable"] = reliable
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        
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

    def delete(self, syslog: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            syslog: syslog parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if syslog is not None:
            url = "/cli/global/system/syslog/{syslog}"
            url = url.replace("{syslog}", str(syslog))
        else:
            url = "/cli/global/system/syslog"
        
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

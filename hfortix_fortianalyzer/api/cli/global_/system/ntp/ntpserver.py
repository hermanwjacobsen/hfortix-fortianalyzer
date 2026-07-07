"""
FortiAnalyzer API endpoint: cli.global.system.ntp.ntpserver

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemNtpNtpserver:
    """
    FortiAnalyzer endpoint: cli.global.system.ntp.ntpserver
    
    
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
        ntpserver: int | str | None = None,
        fields: list[Literal["authentication", "id", "key", "key-fmt", "key-id", "key-type", "maxpoll", "minpoll", "ntpv3", "server"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            ntpserver: ntpserver parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ntpserver is not None:
            url = "/cli/global/system/ntp/ntpserver/{ntpserver}"
            url = url.replace("{ntpserver}", str(ntpserver))
        else:
            url = "/cli/global/system/ntp/ntpserver"
        
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
        ntpserver: int | str | None = None,
        authentication: Literal["disable", "enable"] | None = None,
        id: int | None = None,
        key_fmt: Literal["ascii", "hex"] | None = None,
        key_id: int | None = None,
        key_type: Literal["md5", "sha256"] | None = None,
        maxpoll: int | None = None,
        minpoll: int | None = None,
        ntpv3: Literal["disable", "enable"] | None = None,
        key: list[Any] | None = None,
        server: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            ntpserver: ntpserver parameter
            authentication: authentication parameter
            id: id parameter
            key: key parameter
            key_fmt: key-fmt parameter
            key_id: key-id parameter
            key_type: key-type parameter
            maxpoll: maxpoll parameter
            minpoll: minpoll parameter
            ntpv3: ntpv3 parameter
            server: server parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/ntp/ntpserver"
        
        # Build data payload
        data = {}
        if authentication is not None:
            data["authentication"] = authentication
        if id is not None:
            data["id"] = id
        if key is not None:
            data["key"] = key
        if key_fmt is not None:
            data["key-fmt"] = key_fmt
        if key_id is not None:
            data["key-id"] = key_id
        if key_type is not None:
            data["key-type"] = key_type
        if maxpoll is not None:
            data["maxpoll"] = maxpoll
        if minpoll is not None:
            data["minpoll"] = minpoll
        if ntpv3 is not None:
            data["ntpv3"] = ntpv3
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
        ntpserver: int | str | None = None,
        authentication: Literal["disable", "enable"] | None = None,
        id: int | None = None,
        key_fmt: Literal["ascii", "hex"] | None = None,
        key_id: int | None = None,
        key_type: Literal["md5", "sha256"] | None = None,
        maxpoll: int | None = None,
        minpoll: int | None = None,
        ntpv3: Literal["disable", "enable"] | None = None,
        key: list[Any] | None = None,
        server: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            ntpserver: ntpserver parameter
            authentication: authentication parameter
            id: id parameter
            key: key parameter
            key_fmt: key-fmt parameter
            key_id: key-id parameter
            key_type: key-type parameter
            maxpoll: maxpoll parameter
            minpoll: minpoll parameter
            ntpv3: ntpv3 parameter
            server: server parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ntpserver is not None:
            url = "/cli/global/system/ntp/ntpserver/{ntpserver}"
            url = url.replace("{ntpserver}", str(ntpserver))
        else:
            url = "/cli/global/system/ntp/ntpserver"
        
        # Build data payload
        data = {}
        if authentication is not None:
            data["authentication"] = authentication
        if id is not None:
            data["id"] = id
        if key is not None:
            data["key"] = key
        if key_fmt is not None:
            data["key-fmt"] = key_fmt
        if key_id is not None:
            data["key-id"] = key_id
        if key_type is not None:
            data["key-type"] = key_type
        if maxpoll is not None:
            data["maxpoll"] = maxpoll
        if minpoll is not None:
            data["minpoll"] = minpoll
        if ntpv3 is not None:
            data["ntpv3"] = ntpv3
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
        ntpserver: int | str | None = None,
        authentication: Literal["disable", "enable"] | None = None,
        id: int | None = None,
        key_fmt: Literal["ascii", "hex"] | None = None,
        key_id: int | None = None,
        key_type: Literal["md5", "sha256"] | None = None,
        maxpoll: int | None = None,
        minpoll: int | None = None,
        ntpv3: Literal["disable", "enable"] | None = None,
        key: list[Any] | None = None,
        server: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            ntpserver: ntpserver parameter
            authentication: authentication parameter
            id: id parameter
            key: key parameter
            key_fmt: key-fmt parameter
            key_id: key-id parameter
            key_type: key-type parameter
            maxpoll: maxpoll parameter
            minpoll: minpoll parameter
            ntpv3: ntpv3 parameter
            server: server parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ntpserver is not None:
            url = "/cli/global/system/ntp/ntpserver/{ntpserver}"
            url = url.replace("{ntpserver}", str(ntpserver))
        else:
            url = "/cli/global/system/ntp/ntpserver"
        
        # Build data payload
        data = {}
        if authentication is not None:
            data["authentication"] = authentication
        if id is not None:
            data["id"] = id
        if key is not None:
            data["key"] = key
        if key_fmt is not None:
            data["key-fmt"] = key_fmt
        if key_id is not None:
            data["key-id"] = key_id
        if key_type is not None:
            data["key-type"] = key_type
        if maxpoll is not None:
            data["maxpoll"] = maxpoll
        if minpoll is not None:
            data["minpoll"] = minpoll
        if ntpv3 is not None:
            data["ntpv3"] = ntpv3
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

    def delete(self, ntpserver: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            ntpserver: ntpserver parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ntpserver is not None:
            url = "/cli/global/system/ntp/ntpserver/{ntpserver}"
            url = url.replace("{ntpserver}", str(ntpserver))
        else:
            url = "/cli/global/system/ntp/ntpserver"
        
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

"""
FortiAnalyzer API endpoint: cli.global.system.ha.peer

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemHaPeer:
    """
    FortiAnalyzer endpoint: cli.global.system.ha.peer
    
    
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
        peer: int | str | None = None,
        fields: list[Literal["addr", "addr-hb", "id", "serial-number", "status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            peer: peer parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if peer is not None:
            url = "/cli/global/system/ha/peer/{peer}"
            url = url.replace("{peer}", str(peer))
        else:
            url = "/cli/global/system/ha/peer"
        
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
        peer: int | str | None = None,
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        addr: str | None = None,
        addr_hb: str | None = None,
        serial_number: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            peer: peer parameter
            addr: addr parameter
            addr_hb: addr-hb parameter
            id: id parameter
            serial_number: serial-number parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/ha/peer"
        
        # Build data payload
        data = {}
        if addr is not None:
            data["addr"] = addr
        if addr_hb is not None:
            data["addr-hb"] = addr_hb
        if id is not None:
            data["id"] = id
        if serial_number is not None:
            data["serial-number"] = serial_number
        if status is not None:
            data["status"] = status
        
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
        peer: int | str | None = None,
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        addr: str | None = None,
        addr_hb: str | None = None,
        serial_number: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            peer: peer parameter
            addr: addr parameter
            addr_hb: addr-hb parameter
            id: id parameter
            serial_number: serial-number parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if peer is not None:
            url = "/cli/global/system/ha/peer/{peer}"
            url = url.replace("{peer}", str(peer))
        else:
            url = "/cli/global/system/ha/peer"
        
        # Build data payload
        data = {}
        if addr is not None:
            data["addr"] = addr
        if addr_hb is not None:
            data["addr-hb"] = addr_hb
        if id is not None:
            data["id"] = id
        if serial_number is not None:
            data["serial-number"] = serial_number
        if status is not None:
            data["status"] = status
        
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
        peer: int | str | None = None,
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        addr: str | None = None,
        addr_hb: str | None = None,
        serial_number: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            peer: peer parameter
            addr: addr parameter
            addr_hb: addr-hb parameter
            id: id parameter
            serial_number: serial-number parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if peer is not None:
            url = "/cli/global/system/ha/peer/{peer}"
            url = url.replace("{peer}", str(peer))
        else:
            url = "/cli/global/system/ha/peer"
        
        # Build data payload
        data = {}
        if addr is not None:
            data["addr"] = addr
        if addr_hb is not None:
            data["addr-hb"] = addr_hb
        if id is not None:
            data["id"] = id
        if serial_number is not None:
            data["serial-number"] = serial_number
        if status is not None:
            data["status"] = status
        
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

    def delete(self, peer: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            peer: peer parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if peer is not None:
            url = "/cli/global/system/ha/peer/{peer}"
            url = url.replace("{peer}", str(peer))
        else:
            url = "/cli/global/system/ha/peer"
        
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

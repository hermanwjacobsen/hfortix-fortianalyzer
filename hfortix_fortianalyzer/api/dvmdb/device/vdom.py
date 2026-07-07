"""
FortiAnalyzer API endpoint: dvmdb.device.vdom

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbDeviceVdom:
    """
    FortiAnalyzer endpoint: dvmdb.device.vdom
    
    
    Available methods: add, get, set, update, delete
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def add(
        self,
        device: str,
        vdom: int | str | None = None,
        opmode: Literal["nat", "transparent"] | None = None,
        vdom_type: Literal["traffic", "admin"] | None = None,
        comments: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        rtm_prof_id: int | None = None,
        status: str | None = None,
        vpn_id: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            device: Unique name for the device.
            vdom: vdom parameter
            comments: comments parameter
            meta_fields: meta fields parameter
            name: name parameter
            opmode: opmode parameter
            rtm_prof_id: rtm_prof_id parameter
            status: status parameter
            vdom_type: vdom_type parameter
            vpn_id: vpn_id parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvmdb/device/{device}/vdom"
        url = url.replace("{device}", device)
        
        # Build data payload
        data = {}
        if comments is not None:
            data["comments"] = comments
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if name is not None:
            data["name"] = name
        if opmode is not None:
            data["opmode"] = opmode
        if rtm_prof_id is not None:
            data["rtm_prof_id"] = rtm_prof_id
        if status is not None:
            data["status"] = status
        if vdom_type is not None:
            data["vdom_type"] = vdom_type
        if vpn_id is not None:
            data["vpn_id"] = vpn_id
        
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

    def get(
        self,
        device: str,
        vdom: int | str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["comments", "name", "opmode", "rtm_prof_id", "status", "vdom_type", "vpn_id"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        meta_fields: list[str] | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            device: Unique name for the device.
            vdom: vdom parameter
            expand_member: Fetch all or selected attributes of object members.
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            meta_fields: Specify the meta field attributes to be returned in the result. If none specified, no meta field attribute will be returned.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>object member</b> - Return a list of object members along with other attributes.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
            range: Limit the number of output. For a range of [a, n], the output will contain <i>n</i> elements, starting from the <i>a<sup>th</sup></i> matching result.
            sortings: Specify the sorting of the returned result.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if device is not None and vdom is not None:
            url = "/dvmdb/device/{device}/vdom/{vdom}"
            url = url.replace("{device}", device)
            url = url.replace("{vdom}", str(vdom))
        else:
            url = "/dvmdb/device/{device}/vdom"
            url = url.replace("{device}", device)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        if fields is not None and fields and not isinstance(fields[0], list):
            fields = [fields]
        
        request_params = {}
        if expand_member is not None:
            request_params["expand member"] = expand_member
        if fields is not None:
            request_params["fields"] = fields
        if filter is not None:
            request_params["filter"] = filter
        if loadsub is not None:
            request_params["loadsub"] = loadsub
        if meta_fields is not None:
            request_params["meta fields"] = meta_fields
        if option is not None:
            request_params["option"] = option
        if range is not None:
            request_params["range"] = range
        if sortings is not None:
            request_params["sortings"] = sortings
        
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

    def set(
        self,
        device: str,
        vdom: int | str | None = None,
        opmode: Literal["nat", "transparent"] | None = None,
        vdom_type: Literal["traffic", "admin"] | None = None,
        comments: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        rtm_prof_id: int | None = None,
        status: str | None = None,
        vpn_id: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            device: Unique name for the device.
            vdom: vdom parameter
            comments: comments parameter
            meta_fields: meta fields parameter
            name: name parameter
            opmode: opmode parameter
            rtm_prof_id: rtm_prof_id parameter
            status: status parameter
            vdom_type: vdom_type parameter
            vpn_id: vpn_id parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if device is not None and vdom is not None:
            url = "/dvmdb/device/{device}/vdom/{vdom}"
            url = url.replace("{device}", device)
            url = url.replace("{vdom}", str(vdom))
        else:
            url = "/dvmdb/device/{device}/vdom"
            url = url.replace("{device}", device)
        
        # Build data payload
        data = {}
        if comments is not None:
            data["comments"] = comments
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if name is not None:
            data["name"] = name
        if opmode is not None:
            data["opmode"] = opmode
        if rtm_prof_id is not None:
            data["rtm_prof_id"] = rtm_prof_id
        if status is not None:
            data["status"] = status
        if vdom_type is not None:
            data["vdom_type"] = vdom_type
        if vpn_id is not None:
            data["vpn_id"] = vpn_id
        
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
        device: str,
        vdom: int | str | None = None,
        opmode: Literal["nat", "transparent"] | None = None,
        vdom_type: Literal["traffic", "admin"] | None = None,
        comments: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None,
        rtm_prof_id: int | None = None,
        status: str | None = None,
        vpn_id: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            device: Unique name for the device.
            vdom: vdom parameter
            comments: comments parameter
            meta_fields: meta fields parameter
            name: name parameter
            opmode: opmode parameter
            rtm_prof_id: rtm_prof_id parameter
            status: status parameter
            vdom_type: vdom_type parameter
            vpn_id: vpn_id parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if device is not None and vdom is not None:
            url = "/dvmdb/device/{device}/vdom/{vdom}"
            url = url.replace("{device}", device)
            url = url.replace("{vdom}", str(vdom))
        else:
            url = "/dvmdb/device/{device}/vdom"
            url = url.replace("{device}", device)
        
        # Build data payload
        data = {}
        if comments is not None:
            data["comments"] = comments
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if name is not None:
            data["name"] = name
        if opmode is not None:
            data["opmode"] = opmode
        if rtm_prof_id is not None:
            data["rtm_prof_id"] = rtm_prof_id
        if status is not None:
            data["status"] = status
        if vdom_type is not None:
            data["vdom_type"] = vdom_type
        if vpn_id is not None:
            data["vpn_id"] = vpn_id
        
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

    def delete(self, device: str, vdom: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            device: Unique name for the device.
            vdom: vdom parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if device is not None and vdom is not None:
            url = "/dvmdb/device/{device}/vdom/{vdom}"
            url = url.replace("{device}", device)
            url = url.replace("{vdom}", str(vdom))
        else:
            url = "/dvmdb/device/{device}/vdom"
            url = url.replace("{device}", device)
        
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

"""
FortiAnalyzer API endpoint: cli.global.system.log.device-selector

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogDeviceSelector:
    """
    FortiAnalyzer endpoint: cli.global.system.log.device-selector
    
    
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
        device_selector: int | str | None = None,
        fields: list[Literal["action", "comment", "devid", "expire", "id", "srcip", "srcip-mode", "type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            device_selector: device-selector parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if device_selector is not None:
            url = "/cli/global/system/log/device-selector/{device-selector}"
            url = url.replace("{device-selector}", str(device_selector))
        else:
            url = "/cli/global/system/log/device-selector"
        
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
        device_selector: int | str | None = None,
        action: Literal["include", "exclude"] | None = None,
        id: int | None = None,
        srcip_mode: Literal["UDP514", "TCP514", "any"] | None = None,
        type: Literal["unspecified", "devid", "srcip"] | None = None,
        comment: str | None = None,
        devid: str | None = None,
        expire: str | None = None,
        srcip: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            device_selector: device-selector parameter
            action: action parameter
            comment: comment parameter
            devid: devid parameter
            expire: expire parameter
            id: id parameter
            srcip: srcip parameter
            srcip_mode: srcip-mode parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/device-selector"
        
        # Build data payload
        data = {}
        if action is not None:
            data["action"] = action
        if comment is not None:
            data["comment"] = comment
        if devid is not None:
            data["devid"] = devid
        if expire is not None:
            data["expire"] = expire
        if id is not None:
            data["id"] = id
        if srcip is not None:
            data["srcip"] = srcip
        if srcip_mode is not None:
            data["srcip-mode"] = srcip_mode
        if type is not None:
            data["type"] = type
        
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
        device_selector: int | str | None = None,
        action: Literal["include", "exclude"] | None = None,
        id: int | None = None,
        srcip_mode: Literal["UDP514", "TCP514", "any"] | None = None,
        type: Literal["unspecified", "devid", "srcip"] | None = None,
        comment: str | None = None,
        devid: str | None = None,
        expire: str | None = None,
        srcip: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            device_selector: device-selector parameter
            action: action parameter
            comment: comment parameter
            devid: devid parameter
            expire: expire parameter
            id: id parameter
            srcip: srcip parameter
            srcip_mode: srcip-mode parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if device_selector is not None:
            url = "/cli/global/system/log/device-selector/{device-selector}"
            url = url.replace("{device-selector}", str(device_selector))
        else:
            url = "/cli/global/system/log/device-selector"
        
        # Build data payload
        data = {}
        if action is not None:
            data["action"] = action
        if comment is not None:
            data["comment"] = comment
        if devid is not None:
            data["devid"] = devid
        if expire is not None:
            data["expire"] = expire
        if id is not None:
            data["id"] = id
        if srcip is not None:
            data["srcip"] = srcip
        if srcip_mode is not None:
            data["srcip-mode"] = srcip_mode
        if type is not None:
            data["type"] = type
        
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
        device_selector: int | str | None = None,
        action: Literal["include", "exclude"] | None = None,
        id: int | None = None,
        srcip_mode: Literal["UDP514", "TCP514", "any"] | None = None,
        type: Literal["unspecified", "devid", "srcip"] | None = None,
        comment: str | None = None,
        devid: str | None = None,
        expire: str | None = None,
        srcip: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            device_selector: device-selector parameter
            action: action parameter
            comment: comment parameter
            devid: devid parameter
            expire: expire parameter
            id: id parameter
            srcip: srcip parameter
            srcip_mode: srcip-mode parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if device_selector is not None:
            url = "/cli/global/system/log/device-selector/{device-selector}"
            url = url.replace("{device-selector}", str(device_selector))
        else:
            url = "/cli/global/system/log/device-selector"
        
        # Build data payload
        data = {}
        if action is not None:
            data["action"] = action
        if comment is not None:
            data["comment"] = comment
        if devid is not None:
            data["devid"] = devid
        if expire is not None:
            data["expire"] = expire
        if id is not None:
            data["id"] = id
        if srcip is not None:
            data["srcip"] = srcip
        if srcip_mode is not None:
            data["srcip-mode"] = srcip_mode
        if type is not None:
            data["type"] = type
        
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

    def delete(self, device_selector: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            device_selector: device-selector parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if device_selector is not None:
            url = "/cli/global/system/log/device-selector/{device-selector}"
            url = url.replace("{device-selector}", str(device_selector))
        else:
            url = "/cli/global/system/log/device-selector"
        
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

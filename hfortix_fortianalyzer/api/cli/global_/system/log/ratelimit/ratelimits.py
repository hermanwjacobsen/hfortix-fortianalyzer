"""
FortiAnalyzer API endpoint: cli.global.system.log.ratelimit.ratelimits

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogRatelimitRatelimits:
    """
    FortiAnalyzer endpoint: cli.global.system.log.ratelimit.ratelimits
    
    
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
        ratelimits: int | str | None = None,
        fields: list[Literal["filter", "filter-type", "id", "ratelimit"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            ratelimits: ratelimits parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ratelimits is not None:
            url = "/cli/global/system/log/ratelimit/ratelimits/{ratelimits}"
            url = url.replace("{ratelimits}", str(ratelimits))
        else:
            url = "/cli/global/system/log/ratelimit/ratelimits"
        
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
        ratelimits: int | str | None = None,
        filter_type: Literal["devid", "adom"] | None = None,
        id: int | None = None,
        ratelimit: int | None = None,
        filter: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            ratelimits: ratelimits parameter
            filter: filter parameter
            filter_type: filter-type parameter
            id: id parameter
            ratelimit: ratelimit parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/ratelimit/ratelimits"
        
        # Build data payload
        data = {}
        if filter is not None:
            data["filter"] = filter
        if filter_type is not None:
            data["filter-type"] = filter_type
        if id is not None:
            data["id"] = id
        if ratelimit is not None:
            data["ratelimit"] = ratelimit
        
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
        ratelimits: int | str | None = None,
        filter_type: Literal["devid", "adom"] | None = None,
        id: int | None = None,
        ratelimit: int | None = None,
        filter: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            ratelimits: ratelimits parameter
            filter: filter parameter
            filter_type: filter-type parameter
            id: id parameter
            ratelimit: ratelimit parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ratelimits is not None:
            url = "/cli/global/system/log/ratelimit/ratelimits/{ratelimits}"
            url = url.replace("{ratelimits}", str(ratelimits))
        else:
            url = "/cli/global/system/log/ratelimit/ratelimits"
        
        # Build data payload
        data = {}
        if filter is not None:
            data["filter"] = filter
        if filter_type is not None:
            data["filter-type"] = filter_type
        if id is not None:
            data["id"] = id
        if ratelimit is not None:
            data["ratelimit"] = ratelimit
        
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
        ratelimits: int | str | None = None,
        filter_type: Literal["devid", "adom"] | None = None,
        id: int | None = None,
        ratelimit: int | None = None,
        filter: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            ratelimits: ratelimits parameter
            filter: filter parameter
            filter_type: filter-type parameter
            id: id parameter
            ratelimit: ratelimit parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ratelimits is not None:
            url = "/cli/global/system/log/ratelimit/ratelimits/{ratelimits}"
            url = url.replace("{ratelimits}", str(ratelimits))
        else:
            url = "/cli/global/system/log/ratelimit/ratelimits"
        
        # Build data payload
        data = {}
        if filter is not None:
            data["filter"] = filter
        if filter_type is not None:
            data["filter-type"] = filter_type
        if id is not None:
            data["id"] = id
        if ratelimit is not None:
            data["ratelimit"] = ratelimit
        
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

    def delete(self, ratelimits: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            ratelimits: ratelimits parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ratelimits is not None:
            url = "/cli/global/system/log/ratelimit/ratelimits/{ratelimits}"
            url = url.replace("{ratelimits}", str(ratelimits))
        else:
            url = "/cli/global/system/log/ratelimit/ratelimits"
        
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

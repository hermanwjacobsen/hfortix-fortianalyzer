"""
FortiAnalyzer API endpoint: dvmdb.adom.folder

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbAdomFolder:
    """
    FortiAnalyzer endpoint: dvmdb.adom.folder
    
    
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
        adom: str,
        folder: int | str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            adom: ADOM name.
            folder: folder parameter
            desc: desc parameter
            name: name parameter
            parent: parent parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvmdb/adom/{adom}/folder"
        url = url.replace("{adom}", adom)
        
        # Build data payload
        data = {}
        if desc is not None:
            data["desc"] = desc
        if name is not None:
            data["name"] = name
        if parent is not None:
            data["parent"] = parent
        
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
        adom: str,
        folder: int | str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["desc", "name", "parent"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            adom: ADOM name.
            folder: folder parameter
            expand_member: Fetch all or selected attributes of object members.
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>object member</b> - Return a list of object members along with other attributes.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
            range: Limit the number of output. For a range of [a, n], the output will contain <i>n</i> elements, starting from the <i>a<sup>th</sup></i> matching result.
            sortings: Specify the sorting of the returned result.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and folder is not None:
            url = "/dvmdb/adom/{adom}/folder/{folder}"
            url = url.replace("{adom}", adom)
            url = url.replace("{folder}", str(folder))
        else:
            url = "/dvmdb/adom/{adom}/folder"
            url = url.replace("{adom}", adom)
        
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
        adom: str,
        folder: int | str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            adom: ADOM name.
            folder: folder parameter
            desc: desc parameter
            name: name parameter
            parent: parent parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and folder is not None:
            url = "/dvmdb/adom/{adom}/folder/{folder}"
            url = url.replace("{adom}", adom)
            url = url.replace("{folder}", str(folder))
        else:
            url = "/dvmdb/adom/{adom}/folder"
            url = url.replace("{adom}", adom)
        
        # Build data payload
        data = {}
        if desc is not None:
            data["desc"] = desc
        if name is not None:
            data["name"] = name
        if parent is not None:
            data["parent"] = parent
        
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
        adom: str,
        folder: int | str | None = None,
        desc: str | None = None,
        name: str | None = None,
        parent: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            adom: ADOM name.
            folder: folder parameter
            desc: desc parameter
            name: name parameter
            parent: parent parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and folder is not None:
            url = "/dvmdb/adom/{adom}/folder/{folder}"
            url = url.replace("{adom}", adom)
            url = url.replace("{folder}", str(folder))
        else:
            url = "/dvmdb/adom/{adom}/folder"
            url = url.replace("{adom}", adom)
        
        # Build data payload
        data = {}
        if desc is not None:
            data["desc"] = desc
        if name is not None:
            data["name"] = name
        if parent is not None:
            data["parent"] = parent
        
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

    def delete(self, adom: str, folder: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            adom: ADOM name.
            folder: folder parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and folder is not None:
            url = "/dvmdb/adom/{adom}/folder/{folder}"
            url = url.replace("{adom}", adom)
            url = url.replace("{folder}", str(folder))
        else:
            url = "/dvmdb/adom/{adom}/folder"
            url = url.replace("{adom}", adom)
        
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

"""
FortiAnalyzer API endpoint: dvmdb.group

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbGroup:
    """
    FortiAnalyzer endpoint: dvmdb.group
    
    
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
        group: int | str | None = None,
        cluster_type: Literal["unknown", "vwan", "ums_aws", "ums_azure", "ums_gcp"] | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        type: Literal["normal", "default", "auto", "cluster", "fabric"] | None = None,
        desc: str | None = None,
        id: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            group: group parameter
            cluster_type: cluster_type parameter
            desc: desc parameter
            id: id parameter
            meta_fields: Default metafields: none.
            name: name parameter
            os_type: os_type parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvmdb/group"
        
        # Build data payload
        data = {}
        if cluster_type is not None:
            data["cluster_type"] = cluster_type
        if desc is not None:
            data["desc"] = desc
        if id is not None:
            data["id"] = id
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if name is not None:
            data["name"] = name
        if os_type is not None:
            data["os_type"] = os_type
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

    def get(
        self,
        group: int | str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["cluster_type", "desc", "id", "name", "os_type", "type"]] | None = None,
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
            group: group parameter
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
        if group is not None:
            url = "/dvmdb/group/{group}"
            url = url.replace("{group}", str(group))
        else:
            url = "/dvmdb/group"
        
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
        group: int | str | None = None,
        cluster_type: Literal["unknown", "vwan", "ums_aws", "ums_azure", "ums_gcp"] | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        type: Literal["normal", "default", "auto", "cluster", "fabric"] | None = None,
        desc: str | None = None,
        id: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            group: group parameter
            cluster_type: cluster_type parameter
            desc: desc parameter
            id: id parameter
            meta_fields: Default metafields: none.
            name: name parameter
            os_type: os_type parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None:
            url = "/dvmdb/group/{group}"
            url = url.replace("{group}", str(group))
        else:
            url = "/dvmdb/group"
        
        # Build data payload
        data = {}
        if cluster_type is not None:
            data["cluster_type"] = cluster_type
        if desc is not None:
            data["desc"] = desc
        if id is not None:
            data["id"] = id
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if name is not None:
            data["name"] = name
        if os_type is not None:
            data["os_type"] = os_type
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
        group: int | str | None = None,
        cluster_type: Literal["unknown", "vwan", "ums_aws", "ums_azure", "ums_gcp"] | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        type: Literal["normal", "default", "auto", "cluster", "fabric"] | None = None,
        desc: str | None = None,
        id: str | None = None,
        meta_fields: dict[str, Any] | None = None,
        name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            group: group parameter
            cluster_type: cluster_type parameter
            desc: desc parameter
            id: id parameter
            meta_fields: Default metafields: none.
            name: name parameter
            os_type: os_type parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None:
            url = "/dvmdb/group/{group}"
            url = url.replace("{group}", str(group))
        else:
            url = "/dvmdb/group"
        
        # Build data payload
        data = {}
        if cluster_type is not None:
            data["cluster_type"] = cluster_type
        if desc is not None:
            data["desc"] = desc
        if id is not None:
            data["id"] = id
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if name is not None:
            data["name"] = name
        if os_type is not None:
            data["os_type"] = os_type
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

    def delete(self, group: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            group: group parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if group is not None:
            url = "/dvmdb/group/{group}"
            url = url.replace("{group}", str(group))
        else:
            url = "/dvmdb/group"
        
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

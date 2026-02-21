"""
FortiAnalyzer API endpoint: dvmdb.group.object member

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbGroupObjectMember:
    """
    FortiAnalyzer endpoint: dvmdb.group.object member
    
    
    Available methods: add, delete, set, update
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
        adom: str | None = None,
        group: str | None = None,
        name: str | None = None,
        vdom: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            adom: ADOM name.
            group: group parameter
            name: name parameter
            vdom: vdom parameter
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and group is not None:
            url = "/dvmdb/adom/{adom}/group/{group}/object member"
            url = url.replace("{adom}", adom)
            url = url.replace("{group}", group)
        else:
            url = "/dvmdb/adom/group/object member"
        
        # Build data payload
        data = {}
        if name is not None:
            data["name"] = name
        if vdom is not None:
            data["vdom"] = vdom
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str | None = None,
        group: str | None = None,
        name: str | None = None,
        vdom: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            adom: ADOM name.
            group: group parameter
            name: name parameter
            vdom: vdom parameter
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and group is not None:
            url = "/dvmdb/adom/{adom}/group/{group}/object member"
            url = url.replace("{adom}", adom)
            url = url.replace("{group}", group)
        else:
            url = "/dvmdb/adom/group/object member"
        
        # Build data payload
        data = {}
        if name is not None:
            data["name"] = name
        if vdom is not None:
            data["vdom"] = vdom
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        return FortiAnalyzerResponse(response)

    def set(
        self,
        adom: str | None = None,
        group: str | None = None,
        name: str | None = None,
        vdom: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            adom: ADOM name.
            group: group parameter
            name: name parameter
            vdom: vdom parameter
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and group is not None:
            url = "/dvmdb/adom/{adom}/group/{group}/object member"
            url = url.replace("{adom}", adom)
            url = url.replace("{group}", group)
        else:
            url = "/dvmdb/adom/group/object member"
        
        # Build data payload
        data = {}
        if name is not None:
            data["name"] = name
        if vdom is not None:
            data["vdom"] = vdom
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        return FortiAnalyzerResponse(response)

    def update(
        self,
        adom: str | None = None,
        group: str | None = None,
        name: str | None = None,
        vdom: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            adom: ADOM name.
            group: group parameter
            name: name parameter
            vdom: vdom parameter
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and group is not None:
            url = "/dvmdb/adom/{adom}/group/{group}/object member"
            url = url.replace("{adom}", adom)
            url = url.replace("{group}", group)
        else:
            url = "/dvmdb/adom/group/object member"
        
        # Build data payload
        data = {}
        if name is not None:
            data["name"] = name
        if vdom is not None:
            data["vdom"] = vdom
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        return FortiAnalyzerResponse(response)

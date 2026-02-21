"""
FortiAnalyzer API endpoint: dvmdb.object member

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbObjectMember:
    """
    FortiAnalyzer endpoint: dvmdb.object member
    
    
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
        name: str | None = None,
        vdom: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            adom: adom parameter
            name: name parameter
            vdom: vdom parameter
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None:
            url = "/dvmdb/adom/{adom}/object member"
            url = url.replace("{adom}", adom)
        else:
            url = "/dvmdb/adom/object member"
        
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
        name: str | None = None,
        vdom: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            adom: adom parameter
            name: name parameter
            vdom: vdom parameter
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None:
            url = "/dvmdb/adom/{adom}/object member"
            url = url.replace("{adom}", adom)
        else:
            url = "/dvmdb/adom/object member"
        
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
        name: str | None = None,
        vdom: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            adom: adom parameter
            name: name parameter
            vdom: vdom parameter
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None:
            url = "/dvmdb/adom/{adom}/object member"
            url = url.replace("{adom}", adom)
        else:
            url = "/dvmdb/adom/object member"
        
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
        name: str | None = None,
        vdom: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            adom: adom parameter
            name: name parameter
            vdom: vdom parameter
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None:
            url = "/dvmdb/adom/{adom}/object member"
            url = url.replace("{adom}", adom)
        else:
            url = "/dvmdb/adom/object member"
        
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

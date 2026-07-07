"""
FortiAnalyzer API endpoint: dvmdb.adom.group.object member

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbAdomGroupObjectMember:
    """
    FortiAnalyzer endpoint: dvmdb.adom.group.object member
    
    
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
        adom: str,
        group: str,
        object_member: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            adom: ADOM name.
            group: group parameter
            object_member: List of objects (schema: common.scope.object). Each object has keys: name, vdom.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvmdb/adom/{adom}/group/{group}/object member"
        url = url.replace("{adom}", adom)
        url = url.replace("{group}", group)
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": object_member if object_member is not None else []
        }]
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str,
        group: str,
        object_member: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            adom: ADOM name.
            group: group parameter
            object_member: List of objects (schema: common.scope.object). Each object has keys: name, vdom.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvmdb/adom/{adom}/group/{group}/object member"
        url = url.replace("{adom}", adom)
        url = url.replace("{group}", group)
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": object_member if object_member is not None else []
        }]
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        adom: str,
        group: str,
        object_member: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            adom: ADOM name.
            group: group parameter
            object_member: List of objects (schema: common.scope.object). Each object has keys: name, vdom.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvmdb/adom/{adom}/group/{group}/object member"
        url = url.replace("{adom}", adom)
        url = url.replace("{group}", group)
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": object_member if object_member is not None else []
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
        group: str,
        object_member: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            adom: ADOM name.
            group: group parameter
            object_member: List of objects (schema: common.scope.object). Each object has keys: name, vdom.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvmdb/adom/{adom}/group/{group}/object member"
        url = url.replace("{adom}", adom)
        url = url.replace("{group}", group)
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": object_member if object_member is not None else []
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

"""
FortiAnalyzer API endpoint: cli.global._meta_fields.system.admin.user

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalMetaFieldsSystemAdminUser:
    """
    FortiAnalyzer endpoint: cli.global._meta_fields.system.admin.user
    
    
    Available methods: get, add, set, update, delete
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/_meta_fields/system/admin/user"
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def add(
        self,
        importance: Literal["optional", "required"] | None = None,
        length: int | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            importance: importance parameter
            length: length parameter
            name: name parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/_meta_fields/system/admin/user"
        
        # Build data payload
        data = {}
        if importance is not None:
            data["importance"] = importance
        if length is not None:
            data["length"] = length
        if name is not None:
            data["name"] = name
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
        importance: Literal["optional", "required"] | None = None,
        length: int | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            importance: importance parameter
            length: length parameter
            name: name parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/_meta_fields/system/admin/user"
        
        # Build data payload
        data = {}
        if importance is not None:
            data["importance"] = importance
        if length is not None:
            data["length"] = length
        if name is not None:
            data["name"] = name
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
        importance: Literal["optional", "required"] | None = None,
        length: int | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            importance: importance parameter
            length: length parameter
            name: name parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/_meta_fields/system/admin/user"
        
        # Build data payload
        data = {}
        if importance is not None:
            data["importance"] = importance
        if length is not None:
            data["length"] = length
        if name is not None:
            data["name"] = name
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

    def delete(
        self,
        importance: Literal["optional", "required"] | None = None,
        length: int | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            importance: importance parameter
            length: length parameter
            name: name parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/_meta_fields/system/admin/user"
        
        # Build data payload
        data = {}
        if importance is not None:
            data["importance"] = importance
        if length is not None:
            data["length"] = length
        if name is not None:
            data["name"] = name
        if status is not None:
            data["status"] = status
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

"""
FortiAnalyzer API endpoint: soar.adom.config.connectors

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomConfigConnectors:
    """
    FortiAnalyzer endpoint: soar.adom.config.connectors
    
    Add connectors configuration.
    
    Available methods: add, update, delete, get
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
        data: list[dict[str, Any]],
        connector_uuid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Add connectors configuration.
        
        Args:
            adom: adom path parameter.
            connector_uuid: connector-uuid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/config/connectors"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "data": data
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def update(
        self,
        adom: str,
        data: list[dict[str, Any]],
        connector_uuid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Add connectors configuration.
        
        Args:
            adom: adom path parameter.
            connector_uuid: connector-uuid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/config/connectors"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "data": data
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str,
        connector_uuid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Add connectors configuration.
        
        Args:
            adom: adom path parameter.
            connector_uuid: connector-uuid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and connector_uuid is not None:
            url = "/soar/adom/{adom}/config/connectors/{connector-uuid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{connector-uuid}", str(connector_uuid))
        else:
            url = "/soar/adom/{adom}/config/connectors"
            url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def get(
        self,
        adom: str,
        connector_uuid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Add connectors configuration.
        
        Args:
            adom: adom path parameter.
            connector_uuid: connector-uuid parameter
            apiver: Current API version.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and connector_uuid is not None:
            url = "/soar/adom/{adom}/config/connectors/{connector-uuid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{connector-uuid}", str(connector_uuid))
        else:
            url = "/soar/adom/{adom}/config/connectors"
            url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        
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

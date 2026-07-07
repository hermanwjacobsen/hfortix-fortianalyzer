"""
FortiAnalyzer API endpoint: soar.adom.config.playbooks

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomConfigPlaybooks:
    """
    FortiAnalyzer endpoint: soar.adom.config.playbooks
    
    Add playbooks configuration.
    
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
        playbook_uuid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Add playbooks configuration.
        
        Args:
            adom: adom path parameter.
            playbook_uuid: playbook-uuid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/config/playbooks"
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
        playbook_uuid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Add playbooks configuration.
        
        Args:
            adom: adom path parameter.
            playbook_uuid: playbook-uuid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/config/playbooks"
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
        playbook_uuid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Add playbooks configuration.
        
        Args:
            adom: adom path parameter.
            playbook_uuid: playbook-uuid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and playbook_uuid is not None:
            url = "/soar/adom/{adom}/config/playbooks/{playbook-uuid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{playbook-uuid}", str(playbook_uuid))
        else:
            url = "/soar/adom/{adom}/config/playbooks"
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
        playbook_uuid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Add playbooks configuration.
        
        Args:
            adom: adom path parameter.
            playbook_uuid: playbook-uuid parameter
            apiver: Current API version.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and playbook_uuid is not None:
            url = "/soar/adom/{adom}/config/playbooks/{playbook-uuid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{playbook-uuid}", str(playbook_uuid))
        else:
            url = "/soar/adom/{adom}/config/playbooks"
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

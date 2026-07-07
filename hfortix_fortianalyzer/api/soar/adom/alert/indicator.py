"""
FortiAnalyzer API endpoint: soar.adom.alert.indicator

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomAlertIndicator:
    """
    FortiAnalyzer endpoint: soar.adom.alert.indicator
    
    Add indicator and its associated enrichment for the specific alert. If no enrichment-uuid is specified, the latest associated enrichment will be used.
    
    Available methods: add, delete, get, update
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
        alert_id: str,
        indicator_uuid: str,
        apiver: int = 3,
        enrichment_uuid: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Add indicator and its associated enrichment for the specific alert. If no enrichment-uuid is specified, the latest associated enrichment will be used.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/alert/indicator"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "alert-id": alert_id,
            "indicator-uuid": indicator_uuid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if enrichment_uuid is not None:
            params[0]["enrichment-uuid"] = enrichment_uuid
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str,
        alert_id: str | None = None,
        apiver: int = 3,
        enrichment_uuid: str | None = None,
        indicator_uuid: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Add indicator and its associated enrichment for the specific alert. If no enrichment-uuid is specified, the latest associated enrichment will be used.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/alert/indicator"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if alert_id is not None:
            params[0]["alert-id"] = alert_id
        if apiver is not None:
            params[0]["apiver"] = apiver
        if enrichment_uuid is not None:
            params[0]["enrichment-uuid"] = enrichment_uuid
        if indicator_uuid is not None:
            params[0]["indicator-uuid"] = indicator_uuid
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def get(
        self,
        adom: str,
        alert_id: str,
        apiver: int = 3,
        filter: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Add indicator and its associated enrichment for the specific alert. If no enrichment-uuid is specified, the latest associated enrichment will be used.
        
        Args:
            adom: adom path parameter.
            alert_id: The alert ID.
            apiver: Current API version.
            filter: Filter expression. 'indicator-uuid', 'type', 'value', 'status', 'enrichment-uuid', 'enrichment-status' and 'enrichment-reputation' are supported. i.e.: indicator-uuid='8a409a0f-e4b7-4c71-8e42-a03748496b13' and value = '8.8.8.8'
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/alert/indicator"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        if alert_id is not None:
            request_params["alert-id"] = alert_id
        request_params["apiver"] = apiver
        if filter is not None:
            request_params["filter"] = filter
        
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

    def update(
        self,
        adom: str,
        alert_id: str,
        indicator_uuid: str,
        apiver: int = 3,
        enrichment_uuid: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Add indicator and its associated enrichment for the specific alert. If no enrichment-uuid is specified, the latest associated enrichment will be used.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/alert/indicator"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "alert-id": alert_id,
            "indicator-uuid": indicator_uuid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if enrichment_uuid is not None:
            params[0]["enrichment-uuid"] = enrichment_uuid
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

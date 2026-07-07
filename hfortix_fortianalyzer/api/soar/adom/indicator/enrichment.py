"""
FortiAnalyzer API endpoint: soar.adom.indicator.enrichment

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomIndicatorEnrichment:
    """
    FortiAnalyzer endpoint: soar.adom.indicator.enrichment
    
    Add enrichment data for the specific indicator.
    
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
        enrichment: list[dict[str, Any]],
        enrichment_uuid: int | str | None = None,
        apiver: int = 3,
        indicator_type: Literal["IP", "URL", "Domain"] | None = None,
        indicator_uuid: str | None = None,
        indicator_value: str | None = None,
        referenced_by: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Add enrichment data for the specific indicator.
        
        Args:
            adom: adom path parameter.
            enrichment_uuid: enrichment_uuid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/indicator/enrichment"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "enrichment": enrichment
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if indicator_type is not None:
            params[0]["indicator-type"] = indicator_type
        if indicator_uuid is not None:
            params[0]["indicator-uuid"] = indicator_uuid
        if indicator_value is not None:
            params[0]["indicator-value"] = indicator_value
        if referenced_by is not None:
            params[0]["referenced-by"] = referenced_by
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str,
        enrichment_uuid: int | str | None = None,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Add enrichment data for the specific indicator.
        
        Args:
            adom: adom path parameter.
            enrichment_uuid: enrichment_uuid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and enrichment_uuid is not None:
            url = "/soar/adom/{adom}/indicator/enrichment/{enrichment_uuid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{enrichment_uuid}", str(enrichment_uuid))
        else:
            url = "/soar/adom/{adom}/indicator/enrichment"
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
        enrichment_uuid: int | str | None = None,
        apiver: int = 3,
        detail_level: Literal["standard", "extended"] | None = None,
        indicator_type: Literal["IP", "URL", "Domain"] | None = None,
        indicator_uuid: str | None = None,
        indicator_value: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Add enrichment data for the specific indicator.
        
        Args:
            adom: adom path parameter.
            enrichment_uuid: enrichment_uuid parameter
            apiver: Current API version.
            detail_level: Specify whether include enrichment-detail in response data. 'standard' not included, 'extended' included. Leaving this parameter empty or omitting it entirely will default to 'standard' details.
            indicator_type: The indicator type.
            indicator_uuid: The indicator UUID.
            indicator_value: The indicator value.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and enrichment_uuid is not None:
            url = "/soar/adom/{adom}/indicator/enrichment/{enrichment_uuid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{enrichment_uuid}", str(enrichment_uuid))
        else:
            url = "/soar/adom/{adom}/indicator/enrichment"
            url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if detail_level is not None:
            request_params["detail-level"] = detail_level
        if indicator_type is not None:
            request_params["indicator-type"] = indicator_type
        if indicator_uuid is not None:
            request_params["indicator-uuid"] = indicator_uuid
        if indicator_value is not None:
            request_params["indicator-value"] = indicator_value
        
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
        enrichment_uuid: int | str | None = None,
        apiver: int = 3,
        enrichment_confidence: float | None = None,
        enrichment_expired: Literal["Yes", "No"] | None = None,
        enrichment_reputation: Literal["Suspicious", "Malicious", "NoReputationAvailable", "TBD", "Good"] | None = None,
        enrichment_status: Literal["InProcess", "Completed", "Failed"] | None = None,
        enrichment_tlp: Literal["Red", "Amber", "Green", "White"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Add enrichment data for the specific indicator.
        
        Args:
            adom: adom path parameter.
            enrichment_uuid: enrichment_uuid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and enrichment_uuid is not None:
            url = "/soar/adom/{adom}/indicator/enrichment/{enrichment_uuid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{enrichment_uuid}", str(enrichment_uuid))
        else:
            url = "/soar/adom/{adom}/indicator/enrichment"
            url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if enrichment_confidence is not None:
            params[0]["enrichment-confidence"] = enrichment_confidence
        if enrichment_expired is not None:
            params[0]["enrichment-expired"] = enrichment_expired
        if enrichment_reputation is not None:
            params[0]["enrichment-reputation"] = enrichment_reputation
        if enrichment_status is not None:
            params[0]["enrichment-status"] = enrichment_status
        if enrichment_tlp is not None:
            params[0]["enrichment-tlp"] = enrichment_tlp
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

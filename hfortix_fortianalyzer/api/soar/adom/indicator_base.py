"""
FortiAnalyzer API endpoint: soar.adom.indicator

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomIndicator:
    """
    FortiAnalyzer endpoint: soar.adom.indicator
    
    An indicator for the input type and value will be added. The system will persist the complete indicator data set, encompassing both basic indicator attributes and associated enrichment information. The UUIDs for the indicator and its associated enrichment will be returned. If an indicator already exists, the existing one will be returned.
    
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
        indicator_type: Literal["IP", "URL", "Domain"],
        indicator_value: str,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        An indicator for the input type and value will be added. The system will persist the complete indicator data set, encompassing both basic indicator attributes and associated enrichment information. The UUIDs for the indicator and its associated enrichment will be returned. If an indicator already exists, the existing one will be returned.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/indicator"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "indicator-type": indicator_type,
            "indicator-value": indicator_value
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str,
        indicator_uuid: str,
        apiver: int = 3
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        An indicator for the input type and value will be added. The system will persist the complete indicator data set, encompassing both basic indicator attributes and associated enrichment information. The UUIDs for the indicator and its associated enrichment will be returned. If an indicator already exists, the existing one will be returned.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/indicator"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "indicator-uuid": indicator_uuid
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
        apiver: int = 3,
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None,
        option: list[Literal["referenced-by-incident", "referenced-by-alert"]] | None = None,
        time_range: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        An indicator for the input type and value will be added. The system will persist the complete indicator data set, encompassing both basic indicator attributes and associated enrichment information. The UUIDs for the indicator and its associated enrichment will be returned. If an indicator already exists, the existing one will be returned.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            filter: Filter expression. 'indicator-uuid', 'type', 'value', 'status', 'enrichment-uuid', 'enrichment-status' and 'enrichment-reputation' are supported. i.e.: indicator-uuid='8a409a0f-e4b7-4c71-8e42-a03748496b13,2828ad45-82a7-4173-844e-40b2259ab556' and value = '8.8.8.8'
            limit: The max number of records to get.
            offset: offset of records to get.
            option: This option defines whether the response should include a array of incident_ids and alert_ids associated with the indicator. Leaving this option empty or omitting it entirely will exclude incident and alert ID data from the response.
            time_range: Time range for data selection. If not exist, default time-range is 7 days from current time.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/indicator"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if filter is not None:
            request_params["filter"] = filter
        if limit is not None:
            request_params["limit"] = limit
        if offset is not None:
            request_params["offset"] = offset
        if option is not None:
            request_params["option"] = option
        if time_range is not None:
            request_params["time-range"] = time_range
        
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
        indicator_uuid: str,
        apiver: int = 3,
        country: str | None = None,
        description: str | None = None,
        status: Literal["TBD", "Unblocked", "Excluded", "Blocked", "Isolated"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        An indicator for the input type and value will be added. The system will persist the complete indicator data set, encompassing both basic indicator attributes and associated enrichment information. The UUIDs for the indicator and its associated enrichment will be returned. If an indicator already exists, the existing one will be returned.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/indicator"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "indicator-uuid": indicator_uuid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if country is not None:
            params[0]["country"] = country
        if description is not None:
            params[0]["description"] = description
        if status is not None:
            params[0]["status"] = status
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

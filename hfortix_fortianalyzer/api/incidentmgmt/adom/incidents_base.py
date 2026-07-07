"""
FortiAnalyzer API endpoint: incidentmgmt.adom.incidents

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomIncidents:
    """
    FortiAnalyzer endpoint: incidentmgmt.adom.incidents
    
    Delete some incidents.
    
    Available methods: delete, get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def delete(
        self,
        adom: str,
        apiver: int = 3,
        incids: list[str] | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Delete some incidents.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/incidents"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if incids is not None:
            params[0]["incids"] = incids
        
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
        detail_level: str | None = None,
        filter: str | None = None,
        incids: list[str] | None = None,
        limit: float | None = None,
        offset: float | None = None,
        sort_by: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Delete some incidents.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            detail_level: The detail level of return data, basic, standard(default) or extended.
            filter: The query filter.
            incids: The incident ID list.
            limit: The maximun number of records to get.
            offset: The offset of records to get.
            sort_by: Sort by field.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/incidents"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if detail_level is not None:
            request_params["detail-level"] = detail_level
        if filter is not None:
            request_params["filter"] = filter
        if incids is not None:
            request_params["incids"] = incids
        if limit is not None:
            request_params["limit"] = limit
        if offset is not None:
            request_params["offset"] = offset
        if sort_by is not None:
            request_params["sort-by"] = sort_by
        
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

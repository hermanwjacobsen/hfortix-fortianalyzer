"""
FortiAnalyzer API endpoint: incidentmgmt.adom.incidents.count

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomIncidentsCount:
    """
    FortiAnalyzer endpoint: incidentmgmt.adom.incidents.count
    
    Get a count number of incidents.
    
    Available methods: get
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(
        self,
        adom: str,
        apiver: int = 3,
        filter: str | None = None,
        incids: list[str] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get a count number of incidents.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            filter: The query filter.
            incids: The incident ID list.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/incidents/count"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if filter is not None:
            request_params["filter"] = filter
        if incids is not None:
            request_params["incids"] = incids
        
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

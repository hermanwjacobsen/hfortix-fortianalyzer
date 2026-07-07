"""
FortiAnalyzer API endpoint: incidentmgmt.adom.attachments.count

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomAttachmentsCount:
    """
    FortiAnalyzer endpoint: incidentmgmt.adom.attachments.count
    
    Get a count number of attachments.
    
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
        incid: str,
        apiver: int = 3,
        attachtype: Literal["alertevent", "log", "note", "logsearchfilter", "file", "report", "history", "sysnote", "enrichment"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get a count number of attachments.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            attachtype: The attachment type.
            incid: The incident ID.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/attachments/count"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if attachtype is not None:
            request_params["attachtype"] = attachtype
        if incid is not None:
            request_params["incid"] = incid
        
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

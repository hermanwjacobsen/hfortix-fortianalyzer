"""
FortiAnalyzer API endpoint: incidentmgmt.adom.attachments

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomAttachments:
    """
    FortiAnalyzer endpoint: incidentmgmt.adom.attachments
    
    Add new incident attachments.
    
    Available methods: add, delete, get
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
        attachments: list[dict[str, Any]],
        incid: str,
        apiver: int = 3,
        lastuser: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Add new incident attachments.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/attachments"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "attachments": attachments,
            "incid": incid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if lastuser is not None:
            params[0]["lastuser"] = lastuser
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        attachids: list[float] | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Add new incident attachments.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/attachments"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "incid": incid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if attachids is not None:
            params[0]["attachids"] = attachids
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def get(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        attachtype: Literal["alertevent", "log", "note", "logsearchfilter", "file", "report", "history", "sysnote", "enrichment"] | None = None,
        limit: float | None = None,
        offset: float | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Add new incident attachments.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            attachtype: The attachment type.
            incid: The incident ID.
            limit: The maximun number of records to get.
            offset: The offset of records to get.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/attachments"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if attachtype is not None:
            request_params["attachtype"] = attachtype
        if incid is not None:
            request_params["incid"] = incid
        if limit is not None:
            request_params["limit"] = limit
        if offset is not None:
            request_params["offset"] = offset
        
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

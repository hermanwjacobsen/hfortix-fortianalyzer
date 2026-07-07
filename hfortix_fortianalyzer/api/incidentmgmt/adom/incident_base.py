"""
FortiAnalyzer API endpoint: incidentmgmt.adom.incident

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomIncident:
    """
    FortiAnalyzer endpoint: incidentmgmt.adom.incident
    
    Add a new incident.
    
    Available methods: add, update
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
        category: str,
        endpoint: str,
        reporter: str,
        incid: int | str | None = None,
        apiver: int = 3,
        description: str | None = None,
        epid: float | None = None,
        euid: float | None = None,
        severity: Literal["high", "medium", "low"] | None = None,
        status: Literal["draft", "analysis", "response", "closed", "cancelled"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Add a new incident.
        
        Args:
            adom: adom path parameter.
            incid: incid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/incident"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "category": category,
            "endpoint": endpoint,
            "reporter": reporter
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if description is not None:
            params[0]["description"] = description
        if epid is not None:
            params[0]["epid"] = epid
        if euid is not None:
            params[0]["euid"] = euid
        if severity is not None:
            params[0]["severity"] = severity
        if status is not None:
            params[0]["status"] = status
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def update(
        self,
        adom: str,
        incid: int | str | None = None,
        apiver: int = 3,
        category: str | None = None,
        description: str | None = None,
        endpoint: str | None = None,
        epid: float | None = None,
        euid: float | None = None,
        lastrevision: float | None = None,
        lastuser: str | None = None,
        severity: Literal["high", "medium", "low"] | None = None,
        status: Literal["draft", "analysis", "response", "closed", "cancelled"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Add a new incident.
        
        Args:
            adom: adom path parameter.
            incid: incid parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and incid is not None:
            url = "/incidentmgmt/adom/{adom}/incident/{incid}"
            url = url.replace("{adom}", adom)
            url = url.replace("{incid}", str(incid))
        else:
            url = "/incidentmgmt/adom/{adom}/incident"
            url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if category is not None:
            params[0]["category"] = category
        if description is not None:
            params[0]["description"] = description
        if endpoint is not None:
            params[0]["endpoint"] = endpoint
        if epid is not None:
            params[0]["epid"] = epid
        if euid is not None:
            params[0]["euid"] = euid
        if lastrevision is not None:
            params[0]["lastrevision"] = lastrevision
        if lastuser is not None:
            params[0]["lastuser"] = lastuser
        if severity is not None:
            params[0]["severity"] = severity
        if status is not None:
            params[0]["status"] = status
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

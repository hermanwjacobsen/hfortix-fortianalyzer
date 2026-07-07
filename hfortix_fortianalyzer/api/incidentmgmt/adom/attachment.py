"""
FortiAnalyzer API endpoint: incidentmgmt.adom.attachment

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomAttachment:
    """
    FortiAnalyzer endpoint: incidentmgmt.adom.attachment
    
    Update an incident attachment.
    
    Available methods: update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def update(
        self,
        attachid: str,
        adom: str,
        data: str,
        apiver: int = 3,
        attachsrc: Literal["manual", "playbook"] | None = None,
        attachsrcid: str | None = None,
        attachsrctrigger: str | None = None,
        lastrevision: float | None = None,
        lastuser: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Update an incident attachment.
        
        Args:
            attachid: attachid parameter
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/attachment/{attachid}"
        url = url.replace("{attachid}", attachid)
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "data": data
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if attachsrc is not None:
            params[0]["attachsrc"] = attachsrc
        if attachsrcid is not None:
            params[0]["attachsrcid"] = attachsrcid
        if attachsrctrigger is not None:
            params[0]["attachsrctrigger"] = attachsrctrigger
        if lastrevision is not None:
            params[0]["lastrevision"] = lastrevision
        if lastuser is not None:
            params[0]["lastuser"] = lastuser
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

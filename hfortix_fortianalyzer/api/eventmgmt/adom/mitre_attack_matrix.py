"""
FortiAnalyzer API endpoint: eventmgmt.adom.mitre-attack-matrix

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomMitreAttackMatrix:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.mitre-attack-matrix
    
    Request of getting Mitre Attack Matrix.
    
    Available methods: add
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
        mitre_domain: str,
        apiver: int = 3,
        option: Literal["metadata", "event-count", "incident-count", "handler-count"] | None = None,
        time_range: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Request of getting Mitre Attack Matrix.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/mitre-attack-matrix"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "mitre-domain": mitre_domain
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if option is not None:
            params[0]["option"] = option
        if time_range is not None:
            params[0]["time-range"] = time_range
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

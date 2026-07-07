"""
FortiAnalyzer API endpoint: ioc.adom.events.ack

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IocAdomEventsAck:
    """
    FortiAnalyzer endpoint: ioc.adom.events.ack
    
    Acknowledge a specific IOC event.
    
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
        adom: str,
        events: list[dict[str, Any]],
        apiver: int = 3,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Acknowledge a specific IOC event.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/ioc/adom/{adom}/events/ack"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "events": events
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if time_range is not None:
            params[0]["time-range"] = time_range
        if timezone is not None:
            params[0]["timezone"] = timezone
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

"""
FortiAnalyzer API endpoint: eventmgmt.adom.config.basic-handler

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomConfigBasicHandler:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.config.basic-handler
    
    support method: add, set, get, update, delete<br>table: /eventmgmt/adom/&lt;adom-name&gt;/config/basic-handler<br>object: /eventmgmt/adom/&lt;adom-name&gt;/config/basic-handler/&lt;handler-id&gt;
    
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
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        support method: add, set, get, update, delete<br>table: /eventmgmt/adom/&lt;adom-name&gt;/config/basic-handler<br>object: /eventmgmt/adom/&lt;adom-name&gt;/config/basic-handler/&lt;handler-id&gt;
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/config/basic-handler"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if data is not None:
            params[0]["data"] = data
        if filter is not None:
            params[0]["filter"] = filter
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

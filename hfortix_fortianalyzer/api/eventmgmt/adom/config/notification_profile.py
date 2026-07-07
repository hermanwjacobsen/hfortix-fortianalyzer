"""
FortiAnalyzer API endpoint: eventmgmt.adom.config.notification-profile

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomConfigNotificationProfile:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.config.notification-profile
    
    support method: add, set, get, update, delete<br>table: /eventmgmt/adom/&lt;adom-name&gt;/config/notification-profile<br>object: /eventmgmt/adom/&lt;adom-name&gt;/config/notification-profile/&lt;profile-id&gt;
    
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
        
        support method: add, set, get, update, delete<br>table: /eventmgmt/adom/&lt;adom-name&gt;/config/notification-profile<br>object: /eventmgmt/adom/&lt;adom-name&gt;/config/notification-profile/&lt;profile-id&gt;
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/config/notification-profile"
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

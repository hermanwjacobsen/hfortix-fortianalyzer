"""
FortiAnalyzer API endpoint: eventmgmt.adom.alertlogs

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomAlertlogs:
    """
    FortiAnalyzer endpoint: eventmgmt.adom.alertlogs
    
    List logs associated with the specific alert.
    
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
        alertid: list[str],
        apiver: int = 3,
        limit: float | None = None,
        offset: float | None = None,
        rulename: str | None = None,
        time_order: Literal["desc", "asc"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        List logs associated with the specific alert.
        
        Args:
            adom: adom path parameter.
            alertid: Alert IDs.
            apiver: Current API version.
            limit: The max number of records to get.
            offset: offset of records to get.
            rulename: The rule name of the rule configured in correlated typed handler.
            time_order: Sort result in descending or ascending order by time
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/eventmgmt/adom/{adom}/alertlogs"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        if alertid is not None:
            request_params["alertid"] = alertid
        request_params["apiver"] = apiver
        if limit is not None:
            request_params["limit"] = limit
        if offset is not None:
            request_params["offset"] = offset
        if rulename is not None:
            request_params["rulename"] = rulename
        if time_order is not None:
            request_params["time-order"] = time_order
        
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

"""
FortiAnalyzer API endpoint: soar.adom.playbook.run-log

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomPlaybookRunLog:
    """
    FortiAnalyzer endpoint: soar.adom.playbook.run-log
    
    Get Run-log for an playbook run instance.
    
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
        run_id: str,
        adom: str,
        apiver: int = 3,
        detail_on_error: Literal["true", "false"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get Run-log for an playbook run instance.
        
        Args:
            run_id: run-id parameter
            adom: adom path parameter.
            apiver: Current API version.
            detail_on_error: Specify whether include detail in log if error happened. missing or empty is 'true'
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/playbook/run-log/{run-id}"
        url = url.replace("{run-id}", run_id)
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if detail_on_error is not None:
            request_params["detail-on-error"] = detail_on_error
        
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

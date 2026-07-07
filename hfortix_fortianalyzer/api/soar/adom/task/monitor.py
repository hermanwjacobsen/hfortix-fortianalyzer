"""
FortiAnalyzer API endpoint: soar.adom.task.monitor

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomTaskMonitor:
    """
    FortiAnalyzer endpoint: soar.adom.task.monitor
    
    Get task-level Playbook execution status.
    
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
        playbook_uuid: str,
        apiver: int = 3,
        filter: str | None = None,
        instance_id: str | None = None,
        run_id: str | None = None,
        sort_by: list[dict[str, Any]] | None = None,
        time_range: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Get task-level Playbook execution status.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            filter: Filtering expression.
            instance_id: Instance ID to get.
            playbook_uuid: Playbook UUID to get. An unique identifier of a playbook. 32 hexadecimal digits is displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters
            run_id: Run ID to track specific playbook run
            sort_by: Sort by field.
            time_range: Time range for source data selection.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/task/monitor"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if filter is not None:
            request_params["filter"] = filter
        if instance_id is not None:
            request_params["instance-id"] = instance_id
        if playbook_uuid is not None:
            request_params["playbook-uuid"] = playbook_uuid
        if run_id is not None:
            request_params["run-id"] = run_id
        if sort_by is not None:
            request_params["sort-by"] = sort_by
        if time_range is not None:
            request_params["time-range"] = time_range
        
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

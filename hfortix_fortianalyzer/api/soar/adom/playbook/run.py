"""
FortiAnalyzer API endpoint: soar.adom.playbook.run

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomPlaybookRun:
    """
    FortiAnalyzer endpoint: soar.adom.playbook.run
    
    Start a task to run a playbook.
    
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
        playbook_uuid: str,
        apiver: int = 3,
        incident_id: str | None = None,
        playbook_input: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Start a task to run a playbook.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/playbook/run"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "playbook-uuid": playbook_uuid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if incident_id is not None:
            params[0]["incident-id"] = incident_id
        if playbook_input is not None:
            params[0]["playbook-input"] = playbook_input
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str,
        apiver: int = 3,
        playbook_runs: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Start a task to run a playbook.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/playbook/run"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if playbook_runs is not None:
            params[0]["playbook-runs"] = playbook_runs
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def get(
        self,
        adom: str,
        apiver: int = 3,
        filter: str | None = None,
        playbook_uuid: str | None = None,
        sort_by: list[dict[str, Any]] | None = None,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Start a task to run a playbook.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            filter: Filtering expresion.
            playbook_uuid: An unique identifier of a playbook. 32 hexadecimal digits is displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters.
            sort_by: Sort by field.
            time_range: Time range for source data selection.
            timezone: The timezone index or name. Time range in request and date/time if any in response will follow this timezone. See Appendix
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/playbook/run"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if filter is not None:
            request_params["filter"] = filter
        if playbook_uuid is not None:
            request_params["playbook-uuid"] = playbook_uuid
        if sort_by is not None:
            request_params["sort-by"] = sort_by
        if time_range is not None:
            request_params["time-range"] = time_range
        if timezone is not None:
            request_params["timezone"] = timezone
        
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

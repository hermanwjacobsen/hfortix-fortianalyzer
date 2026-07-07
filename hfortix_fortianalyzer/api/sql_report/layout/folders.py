"""
FortiAnalyzer API endpoint: sql-report.layout.folders

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SqlReportLayoutFolders:
    """
    FortiAnalyzer endpoint: sql-report.layout.folders
    
    support method: add, set, get, update, delete<br>table: /sql-report/layout/folders<br>object: /sql-report/layout/folders/&lt;folder-id&gt;
    
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
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        support method: add, set, get, update, delete<br>table: /sql-report/layout/folders<br>object: /sql-report/layout/folders/&lt;folder-id&gt;
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/sql-report/layout/folders"
        
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

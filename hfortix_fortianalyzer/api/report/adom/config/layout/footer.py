"""
FortiAnalyzer API endpoint: report.adom.config.layout.footer

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class ReportAdomConfigLayoutFooter:
    """
    FortiAnalyzer endpoint: report.adom.config.layout.footer
    
    support method: add, set, get, update, delete<br>table: /report/config/layout/&lt;layout-id&gt;/footer<br>object: /report/config/layout/&lt;layout-id&gt;/footer/&lt;footer-id&gt;
    
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
        layout_id: str,
        adom: str,
        apiver: int = 3,
        data: dict[str, Any] | None = None,
        filter: list[str] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        support method: add, set, get, update, delete<br>table: /report/config/layout/&lt;layout-id&gt;/footer<br>object: /report/config/layout/&lt;layout-id&gt;/footer/&lt;footer-id&gt;
        
        Args:
            layout_id: layout-id parameter
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/report/adom/{adom}/config/layout/{layout-id}/footer"
        url = url.replace("{layout-id}", layout_id)
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

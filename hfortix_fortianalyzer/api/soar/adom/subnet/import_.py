"""
FortiAnalyzer API endpoint: soar.adom.subnet.import

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomSubnetImport:
    """
    FortiAnalyzer endpoint: soar.adom.subnet.import
    
    Request of importing subnet and subnet groups.
    
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
        data: dict[str, Any],
        apiver: int = 3,
        conflict_option: Literal["rename", "replace", "skip"] | None = None,
        data_type: Literal["zip/base64", "txt"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Request of importing subnet and subnet groups.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/soar/adom/{adom}/subnet/import"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "data": data
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if conflict_option is not None:
            params[0]["conflict-option"] = conflict_option
        if data_type is not None:
            params[0]["data-type"] = data_type
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

"""
FortiAnalyzer API endpoint: sys.proxy.json

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysProxyJson:
    """
    FortiAnalyzer endpoint: sys.proxy.json
    
    
    Available methods: exec
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def exec(
        self,
        timeout: int | None = None,
        action: Literal["get", "post", "put", "delete"] | None = None,
        payload: dict[str, Any] | None = None,
        resource: str | None = None,
        target: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            action: Specify HTTP action for the request.
            payload: Nested object (schema: sys.proxy.json.payload).
            resource: URL on the remote device to be accessed.
            target: target parameter
            timeout: Maximum time in seconds to wait for response from remote device.  If no response recieved from remote device before timeout expires, the proxy will return with error.  If the proxy request is sent to multiple devices, it will not affect the response for other devices that already returned a result.  Valid range: 10 to 28800.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/sys/proxy/json"
        
        # Build data payload
        data = {}
        if action is not None:
            data["action"] = action
        if payload is not None:
            data["payload"] = payload
        if resource is not None:
            data["resource"] = resource
        if target is not None:
            data["target"] = target
        if timeout is not None:
            data["timeout"] = timeout
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="exec",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

"""
FortiAnalyzer API endpoint: dvm.cmd.add.device

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmCmdAddDevice:
    """
    FortiAnalyzer endpoint: dvm.cmd.add.device
    
    
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
        adom: list[Any] | None = None,
        device: dict[str, Any] | None = None,
        flags: list[Any] | None = None,
        groups: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            adom: Name or ID of the ADOM where the command is to be executed on.
            device: Nested object (schema: dvm.cmd.add.device.device).
            flags: <b>create_task</b> - Create a new task in task manager database.<br/><b>nonblocking</b> - The API will return immediately in for non-blocking call. This flag will be set automatically when the adding, importing, updating, and deleting a list of devices.
            groups: groups parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvm/cmd/add/device"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if device is not None:
            data["device"] = device
        if flags is not None:
            data["flags"] = flags
        if groups is not None:
            data["groups"] = groups
        
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

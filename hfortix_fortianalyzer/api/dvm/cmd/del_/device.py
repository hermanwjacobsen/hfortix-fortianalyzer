"""
FortiAnalyzer API endpoint: dvm.cmd.del.device

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmCmdDelDevice:
    """
    FortiAnalyzer endpoint: dvm.cmd.del.device
    
    
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
        device: list[Any] | None = None,
        flags: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            adom: Name or ID of the ADOM where the command is to be executed on.
            device: Name or ID of the target device.
            flags: <b>create_task</b> - Create a new task in task manager database.<br/><b>nonblocking</b> - The API will return immediately in for non-blocking call. This flag will be set automatically when the adding, importing, updating, and deleting a list of devices.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvm/cmd/del/device"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if device is not None:
            data["device"] = device
        if flags is not None:
            data["flags"] = flags
        
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

"""
FortiAnalyzer API endpoint: dvm.cmd.import.dev-list

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmCmdImportDevList:
    """
    FortiAnalyzer endpoint: dvm.cmd.import.dev-list
    
    
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
        flags: list[Any] | None = None,
        import_adom_members: list[Any] | None = None,
        import_adoms: list[Any] | None = None,
        import_devices: list[Any] | None = None,
        import_group_members: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            adom: Name or ID of the ADOM where the command is to be executed on.
            flags: <b>create_task</b> - Create a new task in task manager database.<br/><b>nonblocking</b> - The API will return immediately in for non-blocking call. This flag will be set automatically when the adding, importing, updating, and deleting a list of devices.
            import_adom_members: Associations between devices and ADOMs.
            import_adoms: A list of ADOM and device group objects to be imported.
            import_devices: A list of device objects to be imported.
            import_group_members: Associations between devices and device groups.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/dvm/cmd/import/dev-list"
        
        # Build data payload
        data = {}
        if adom is not None:
            data["adom"] = adom
        if flags is not None:
            data["flags"] = flags
        if import_adom_members is not None:
            data["import-adom-members"] = import_adom_members
        if import_adoms is not None:
            data["import-adoms"] = import_adoms
        if import_devices is not None:
            data["import-devices"] = import_devices
        if import_group_members is not None:
            data["import-group-members"] = import_group_members
        
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

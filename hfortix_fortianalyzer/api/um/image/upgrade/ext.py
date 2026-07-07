"""
FortiAnalyzer API endpoint: um.image.upgrade.ext

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class UmImageUpgradeExt:
    """
    FortiAnalyzer endpoint: um.image.upgrade.ext
    
    
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
        create_task: str | None = None,
        device: list[Any] | None = None,
        flags: Literal["f_boot_alt_partition", "f_skip_retrieve", "f_skip_multi_steps", "f_skip_fortiguard_img", "f_preview"] | None = None,
        image: str | None = None,
        schedule_time: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        EXEC operation.
        
        Args:
            create_task: create_task parameter
            device: device parameter
            flags: flags parameter
            image: Support version with a build number. e.g., 6.2-b1111
            schedule_time: schedule_time parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/um/image/upgrade/ext"
        
        # Build data payload
        data = {}
        if create_task is not None:
            data["create_task"] = create_task
        if device is not None:
            data["device"] = device
        if flags is not None:
            data["flags"] = flags
        if image is not None:
            data["image"] = image
        if schedule_time is not None:
            data["schedule_time"] = schedule_time
        
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

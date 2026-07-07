"""
FortiAnalyzer API endpoint: cli.global.system.backup.all-settings

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemBackupAllSettings:
    """
    FortiAnalyzer endpoint: cli.global.system.backup.all-settings
    
    
    Available methods: get, set, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/backup/all-settings"
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        protocol: Literal["sftp", "ftp", "scp"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        cert: str | None = None,
        crptpasswd: list[Any] | None = None,
        directory: str | None = None,
        passwd: list[Any] | None = None,
        server: str | None = None,
        time: str | None = None,
        user: str | None = None,
        week_days: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            cert: cert parameter
            crptpasswd: crptpasswd parameter
            directory: directory parameter
            passwd: passwd parameter
            protocol: protocol parameter
            server: server parameter
            status: status parameter
            time: time parameter
            user: user parameter
            week_days: week_days parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/backup/all-settings"
        
        # Build data payload
        data = {}
        if cert is not None:
            data["cert"] = cert
        if crptpasswd is not None:
            data["crptpasswd"] = crptpasswd
        if directory is not None:
            data["directory"] = directory
        if passwd is not None:
            data["passwd"] = passwd
        if protocol is not None:
            data["protocol"] = protocol
        if server is not None:
            data["server"] = server
        if status is not None:
            data["status"] = status
        if time is not None:
            data["time"] = time
        if user is not None:
            data["user"] = user
        if week_days is not None:
            data["week_days"] = week_days
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def update(
        self,
        protocol: Literal["sftp", "ftp", "scp"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        cert: str | None = None,
        crptpasswd: list[Any] | None = None,
        directory: str | None = None,
        passwd: list[Any] | None = None,
        server: str | None = None,
        time: str | None = None,
        user: str | None = None,
        week_days: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            cert: cert parameter
            crptpasswd: crptpasswd parameter
            directory: directory parameter
            passwd: passwd parameter
            protocol: protocol parameter
            server: server parameter
            status: status parameter
            time: time parameter
            user: user parameter
            week_days: week_days parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/backup/all-settings"
        
        # Build data payload
        data = {}
        if cert is not None:
            data["cert"] = cert
        if crptpasswd is not None:
            data["crptpasswd"] = crptpasswd
        if directory is not None:
            data["directory"] = directory
        if passwd is not None:
            data["passwd"] = passwd
        if protocol is not None:
            data["protocol"] = protocol
        if server is not None:
            data["server"] = server
        if status is not None:
            data["status"] = status
        if time is not None:
            data["time"] = time
        if user is not None:
            data["user"] = user
        if week_days is not None:
            data["week_days"] = week_days
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

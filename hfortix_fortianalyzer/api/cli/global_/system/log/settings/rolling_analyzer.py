"""
FortiAnalyzer API endpoint: cli.global.system.log.settings.rolling-analyzer

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogSettingsRollingAnalyzer:
    """
    FortiAnalyzer endpoint: cli.global.system.log.settings.rolling-analyzer
    
    
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
        url = "/cli/global/system/log/settings/rolling-analyzer"
        
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
        del_files: Literal["disable", "enable"] | None = None,
        file_size: int | None = None,
        gzip_format: Literal["disable", "enable"] | None = None,
        hour: int | None = None,
        log_format: Literal["native", "text", "csv"] | None = None,
        min: int | None = None,
        port: int | None = None,
        port2: int | None = None,
        port3: int | None = None,
        rolling_upgrade_status: int | None = None,
        server_type: Literal["ftp", "sftp", "scp"] | None = None,
        upload: Literal["disable", "enable"] | None = None,
        upload_hour: int | None = None,
        upload_mode: Literal["backup", "mirror"] | None = None,
        upload_trigger: Literal["on-roll", "on-schedule"] | None = None,
        when: Literal["none", "daily", "weekly"] | None = None,
        days: list[Any] | None = None,
        directory: str | None = None,
        password: list[Any] | None = None,
        password2: list[Any] | None = None,
        password3: list[Any] | None = None,
        server: str | None = None,
        server2: str | None = None,
        server3: str | None = None,
        username: str | None = None,
        username2: str | None = None,
        username3: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            days: days parameter
            del_files: del-files parameter
            directory: directory parameter
            file_size: file-size parameter
            gzip_format: gzip-format parameter
            hour: hour parameter
            log_format: log-format parameter
            min: min parameter
            password: password parameter
            password2: password2 parameter
            ... (17 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/settings/rolling-analyzer"
        
        # Build data payload
        data = {}
        if days is not None:
            data["days"] = days
        if del_files is not None:
            data["del-files"] = del_files
        if directory is not None:
            data["directory"] = directory
        if file_size is not None:
            data["file-size"] = file_size
        if gzip_format is not None:
            data["gzip-format"] = gzip_format
        if hour is not None:
            data["hour"] = hour
        if log_format is not None:
            data["log-format"] = log_format
        if min is not None:
            data["min"] = min
        if password is not None:
            data["password"] = password
        if password2 is not None:
            data["password2"] = password2
        if password3 is not None:
            data["password3"] = password3
        if port is not None:
            data["port"] = port
        if port2 is not None:
            data["port2"] = port2
        if port3 is not None:
            data["port3"] = port3
        if rolling_upgrade_status is not None:
            data["rolling-upgrade-status"] = rolling_upgrade_status
        if server is not None:
            data["server"] = server
        if server_type is not None:
            data["server-type"] = server_type
        if server2 is not None:
            data["server2"] = server2
        if server3 is not None:
            data["server3"] = server3
        if upload is not None:
            data["upload"] = upload
        if upload_hour is not None:
            data["upload-hour"] = upload_hour
        if upload_mode is not None:
            data["upload-mode"] = upload_mode
        if upload_trigger is not None:
            data["upload-trigger"] = upload_trigger
        if username is not None:
            data["username"] = username
        if username2 is not None:
            data["username2"] = username2
        if username3 is not None:
            data["username3"] = username3
        if when is not None:
            data["when"] = when
        
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
        del_files: Literal["disable", "enable"] | None = None,
        file_size: int | None = None,
        gzip_format: Literal["disable", "enable"] | None = None,
        hour: int | None = None,
        log_format: Literal["native", "text", "csv"] | None = None,
        min: int | None = None,
        port: int | None = None,
        port2: int | None = None,
        port3: int | None = None,
        rolling_upgrade_status: int | None = None,
        server_type: Literal["ftp", "sftp", "scp"] | None = None,
        upload: Literal["disable", "enable"] | None = None,
        upload_hour: int | None = None,
        upload_mode: Literal["backup", "mirror"] | None = None,
        upload_trigger: Literal["on-roll", "on-schedule"] | None = None,
        when: Literal["none", "daily", "weekly"] | None = None,
        days: list[Any] | None = None,
        directory: str | None = None,
        password: list[Any] | None = None,
        password2: list[Any] | None = None,
        password3: list[Any] | None = None,
        server: str | None = None,
        server2: str | None = None,
        server3: str | None = None,
        username: str | None = None,
        username2: str | None = None,
        username3: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            days: days parameter
            del_files: del-files parameter
            directory: directory parameter
            file_size: file-size parameter
            gzip_format: gzip-format parameter
            hour: hour parameter
            log_format: log-format parameter
            min: min parameter
            password: password parameter
            password2: password2 parameter
            ... (17 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log/settings/rolling-analyzer"
        
        # Build data payload
        data = {}
        if days is not None:
            data["days"] = days
        if del_files is not None:
            data["del-files"] = del_files
        if directory is not None:
            data["directory"] = directory
        if file_size is not None:
            data["file-size"] = file_size
        if gzip_format is not None:
            data["gzip-format"] = gzip_format
        if hour is not None:
            data["hour"] = hour
        if log_format is not None:
            data["log-format"] = log_format
        if min is not None:
            data["min"] = min
        if password is not None:
            data["password"] = password
        if password2 is not None:
            data["password2"] = password2
        if password3 is not None:
            data["password3"] = password3
        if port is not None:
            data["port"] = port
        if port2 is not None:
            data["port2"] = port2
        if port3 is not None:
            data["port3"] = port3
        if rolling_upgrade_status is not None:
            data["rolling-upgrade-status"] = rolling_upgrade_status
        if server is not None:
            data["server"] = server
        if server_type is not None:
            data["server-type"] = server_type
        if server2 is not None:
            data["server2"] = server2
        if server3 is not None:
            data["server3"] = server3
        if upload is not None:
            data["upload"] = upload
        if upload_hour is not None:
            data["upload-hour"] = upload_hour
        if upload_mode is not None:
            data["upload-mode"] = upload_mode
        if upload_trigger is not None:
            data["upload-trigger"] = upload_trigger
        if username is not None:
            data["username"] = username
        if username2 is not None:
            data["username2"] = username2
        if username3 is not None:
            data["username3"] = username3
        if when is not None:
            data["when"] = when
        
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

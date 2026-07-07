"""
FortiAnalyzer API endpoint: cli.global.system.locallog.disk.setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogDiskSetting:
    """
    FortiAnalyzer endpoint: cli.global.system.locallog.disk.setting
    
    
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
        url = "/cli/global/system/locallog/disk/setting"
        
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
        diskfull: Literal["overwrite", "nolog"] | None = None,
        log_disk_full_percentage: int | None = None,
        log_disk_quota: int | None = None,
        log_rate_limit: int | None = None,
        max_log_file_num: int | None = None,
        max_log_file_size: int | None = None,
        roll_schedule: Literal["none", "daily", "weekly"] | None = None,
        server_type: Literal["FTP", "SFTP", "SCP"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        upload: Literal["disable", "enable"] | None = None,
        upload_delete_files: Literal["disable", "enable"] | None = None,
        uploadip: str | None = None,
        uploadport: int | None = None,
        uploadsched: Literal["disable", "enable"] | None = None,
        uploadzip: Literal["disable", "enable"] | None = None,
        roll_day: list[Any] | None = None,
        roll_time: str | None = None,
        upload_time: str | None = None,
        uploaddir: str | None = None,
        uploadpass: list[Any] | None = None,
        uploadtype: list[Any] | None = None,
        uploaduser: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            diskfull: diskfull parameter
            log_disk_full_percentage: log-disk-full-percentage parameter
            log_disk_quota: log-disk-quota parameter
            log_rate_limit: log-rate-limit parameter
            max_log_file_num: max-log-file-num parameter
            max_log_file_size: max-log-file-size parameter
            roll_day: roll-day parameter
            roll_schedule: roll-schedule parameter
            roll_time: roll-time parameter
            server_type: server-type parameter
            ... (13 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/disk/setting"
        
        # Build data payload
        data = {}
        if diskfull is not None:
            data["diskfull"] = diskfull
        if log_disk_full_percentage is not None:
            data["log-disk-full-percentage"] = log_disk_full_percentage
        if log_disk_quota is not None:
            data["log-disk-quota"] = log_disk_quota
        if log_rate_limit is not None:
            data["log-rate-limit"] = log_rate_limit
        if max_log_file_num is not None:
            data["max-log-file-num"] = max_log_file_num
        if max_log_file_size is not None:
            data["max-log-file-size"] = max_log_file_size
        if roll_day is not None:
            data["roll-day"] = roll_day
        if roll_schedule is not None:
            data["roll-schedule"] = roll_schedule
        if roll_time is not None:
            data["roll-time"] = roll_time
        if server_type is not None:
            data["server-type"] = server_type
        if severity is not None:
            data["severity"] = severity
        if status is not None:
            data["status"] = status
        if upload is not None:
            data["upload"] = upload
        if upload_delete_files is not None:
            data["upload-delete-files"] = upload_delete_files
        if upload_time is not None:
            data["upload-time"] = upload_time
        if uploaddir is not None:
            data["uploaddir"] = uploaddir
        if uploadip is not None:
            data["uploadip"] = uploadip
        if uploadpass is not None:
            data["uploadpass"] = uploadpass
        if uploadport is not None:
            data["uploadport"] = uploadport
        if uploadsched is not None:
            data["uploadsched"] = uploadsched
        if uploadtype is not None:
            data["uploadtype"] = uploadtype
        if uploaduser is not None:
            data["uploaduser"] = uploaduser
        if uploadzip is not None:
            data["uploadzip"] = uploadzip
        
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
        diskfull: Literal["overwrite", "nolog"] | None = None,
        log_disk_full_percentage: int | None = None,
        log_disk_quota: int | None = None,
        log_rate_limit: int | None = None,
        max_log_file_num: int | None = None,
        max_log_file_size: int | None = None,
        roll_schedule: Literal["none", "daily", "weekly"] | None = None,
        server_type: Literal["FTP", "SFTP", "SCP"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        upload: Literal["disable", "enable"] | None = None,
        upload_delete_files: Literal["disable", "enable"] | None = None,
        uploadip: str | None = None,
        uploadport: int | None = None,
        uploadsched: Literal["disable", "enable"] | None = None,
        uploadzip: Literal["disable", "enable"] | None = None,
        roll_day: list[Any] | None = None,
        roll_time: str | None = None,
        upload_time: str | None = None,
        uploaddir: str | None = None,
        uploadpass: list[Any] | None = None,
        uploadtype: list[Any] | None = None,
        uploaduser: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            diskfull: diskfull parameter
            log_disk_full_percentage: log-disk-full-percentage parameter
            log_disk_quota: log-disk-quota parameter
            log_rate_limit: log-rate-limit parameter
            max_log_file_num: max-log-file-num parameter
            max_log_file_size: max-log-file-size parameter
            roll_day: roll-day parameter
            roll_schedule: roll-schedule parameter
            roll_time: roll-time parameter
            server_type: server-type parameter
            ... (13 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/disk/setting"
        
        # Build data payload
        data = {}
        if diskfull is not None:
            data["diskfull"] = diskfull
        if log_disk_full_percentage is not None:
            data["log-disk-full-percentage"] = log_disk_full_percentage
        if log_disk_quota is not None:
            data["log-disk-quota"] = log_disk_quota
        if log_rate_limit is not None:
            data["log-rate-limit"] = log_rate_limit
        if max_log_file_num is not None:
            data["max-log-file-num"] = max_log_file_num
        if max_log_file_size is not None:
            data["max-log-file-size"] = max_log_file_size
        if roll_day is not None:
            data["roll-day"] = roll_day
        if roll_schedule is not None:
            data["roll-schedule"] = roll_schedule
        if roll_time is not None:
            data["roll-time"] = roll_time
        if server_type is not None:
            data["server-type"] = server_type
        if severity is not None:
            data["severity"] = severity
        if status is not None:
            data["status"] = status
        if upload is not None:
            data["upload"] = upload
        if upload_delete_files is not None:
            data["upload-delete-files"] = upload_delete_files
        if upload_time is not None:
            data["upload-time"] = upload_time
        if uploaddir is not None:
            data["uploaddir"] = uploaddir
        if uploadip is not None:
            data["uploadip"] = uploadip
        if uploadpass is not None:
            data["uploadpass"] = uploadpass
        if uploadport is not None:
            data["uploadport"] = uploadport
        if uploadsched is not None:
            data["uploadsched"] = uploadsched
        if uploadtype is not None:
            data["uploadtype"] = uploadtype
        if uploaduser is not None:
            data["uploaduser"] = uploaduser
        if uploadzip is not None:
            data["uploadzip"] = uploadzip
        
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

"""Type stubs for cli.global.system.locallog.disk.setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogDiskSettingGetItem:
    """Item yielded when iterating over CliGlobalSystemLocallogDiskSettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def diskfull(self) -> Literal["overwrite", "nolog"]: ...
    @property
    def log_disk_full_percentage(self) -> int: ...
    @property
    def log_disk_quota(self) -> int: ...
    @property
    def log_rate_limit(self) -> int: ...
    @property
    def max_log_file_num(self) -> int: ...
    @property
    def max_log_file_size(self) -> int: ...
    @property
    def roll_day(self) -> list[Any]: ...
    @property
    def roll_schedule(self) -> Literal["none", "daily", "weekly"]: ...
    @property
    def roll_time(self) -> str: ...
    @property
    def server_type(self) -> Literal["FTP", "SFTP", "SCP"]: ...
    @property
    def severity(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def upload(self) -> Literal["disable", "enable"]: ...
    @property
    def upload_delete_files(self) -> Literal["disable", "enable"]: ...
    @property
    def upload_time(self) -> str: ...
    @property
    def uploaddir(self) -> str: ...
    @property
    def uploadip(self) -> str: ...
    @property
    def uploadpass(self) -> list[Any]: ...
    @property
    def uploadport(self) -> int: ...
    @property
    def uploadsched(self) -> Literal["disable", "enable"]: ...
    @property
    def uploadtype(self) -> list[Any]: ...
    @property
    def uploaduser(self) -> str: ...
    @property
    def uploadzip(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocallogDiskSettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocallogDiskSettingGet endpoint with autocomplete support."""

    # ========================================================================
    # HTTP Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def http_status_code(self) -> int | None: ...
    @property
    def http_response_time(self) -> float | None: ...
    @property
    def http_method(self) -> str | None: ...
    @property
    def http_url(self) -> str | None: ...

    # ========================================================================
    # API Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def api_status_code(self) -> int | None: ...
    @property
    def api_status_message(self) -> str | None: ...
    @property
    def api_id(self) -> int | None: ...
    @property
    def api_url(self) -> str | None: ...
    @property
    def api_raw(self) -> dict[str, Any]: ...

    # ========================================================================
    # Data Fields (specific to this endpoint)
    # ========================================================================
    @property
    def oid(self) -> int | None:
        """Object ID (dynamically added by FortiAnalyzer API, not in Swagger schema)"""
        ...

    @property
    def diskfull(self) -> Literal["overwrite", "nolog"] | None:
        """Field: diskfull"""
        ...

    @property
    def log_disk_full_percentage(self) -> int | None:
        """Field: log-disk-full-percentage"""
        ...

    @property
    def log_disk_quota(self) -> int | None:
        """Field: log-disk-quota"""
        ...

    @property
    def log_rate_limit(self) -> int | None:
        """Field: log-rate-limit"""
        ...

    @property
    def max_log_file_num(self) -> int | None:
        """Field: max-log-file-num"""
        ...

    @property
    def max_log_file_size(self) -> int | None:
        """Field: max-log-file-size"""
        ...

    @property
    def roll_day(self) -> list[Any] | None:
        """Field: roll-day"""
        ...

    @property
    def roll_schedule(self) -> Literal["none", "daily", "weekly"] | None:
        """Field: roll-schedule"""
        ...

    @property
    def roll_time(self) -> str | None:
        """Field: roll-time"""
        ...

    @property
    def server_type(self) -> Literal["FTP", "SFTP", "SCP"] | None:
        """Field: server-type"""
        ...

    @property
    def severity(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None:
        """Field: severity"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def upload(self) -> Literal["disable", "enable"] | None:
        """Field: upload"""
        ...

    @property
    def upload_delete_files(self) -> Literal["disable", "enable"] | None:
        """Field: upload-delete-files"""
        ...

    @property
    def upload_time(self) -> str | None:
        """Field: upload-time"""
        ...

    @property
    def uploaddir(self) -> str | None:
        """Field: uploaddir"""
        ...

    @property
    def uploadip(self) -> str | None:
        """Field: uploadip"""
        ...

    @property
    def uploadpass(self) -> list[Any] | None:
        """Field: uploadpass"""
        ...

    @property
    def uploadport(self) -> int | None:
        """Field: uploadport"""
        ...

    @property
    def uploadsched(self) -> Literal["disable", "enable"] | None:
        """Field: uploadsched"""
        ...

    @property
    def uploadtype(self) -> list[Any] | None:
        """Field: uploadtype"""
        ...

    @property
    def uploaduser(self) -> str | None:
        """Field: uploaduser"""
        ...

    @property
    def uploadzip(self) -> Literal["disable", "enable"] | None:
        """Field: uploadzip"""
        ...


    # Inherited methods from FortiAnalyzerResponse
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[CliGlobalSystemLocallogDiskSettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocallogDiskSetting:
    """FortiAnalyzer endpoint: cli.global.system.locallog.disk.setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLocallogDiskSettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        diskfull: Literal["overwrite", "nolog"] | None = None,
        log_disk_full_percentage: int | None = None,
        log_disk_quota: int | None = None,
        log_rate_limit: int | None = None,
        max_log_file_num: int | None = None,
        max_log_file_size: int | None = None,
        roll_day: list[Any] | None = None,
        roll_schedule: Literal["none", "daily", "weekly"] | None = None,
        roll_time: str | None = None,
        server_type: Literal["FTP", "SFTP", "SCP"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        upload: Literal["disable", "enable"] | None = None,
        upload_delete_files: Literal["disable", "enable"] | None = None,
        upload_time: str | None = None,
        uploaddir: str | None = None,
        uploadip: str | None = None,
        uploadpass: list[Any] | None = None,
        uploadport: int | None = None,
        uploadsched: Literal["disable", "enable"] | None = None,
        uploadtype: list[Any] | None = None,
        uploaduser: str | None = None,
        uploadzip: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        diskfull: Literal["overwrite", "nolog"] | None = None,
        log_disk_full_percentage: int | None = None,
        log_disk_quota: int | None = None,
        log_rate_limit: int | None = None,
        max_log_file_num: int | None = None,
        max_log_file_size: int | None = None,
        roll_day: list[Any] | None = None,
        roll_schedule: Literal["none", "daily", "weekly"] | None = None,
        roll_time: str | None = None,
        server_type: Literal["FTP", "SFTP", "SCP"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        upload: Literal["disable", "enable"] | None = None,
        upload_delete_files: Literal["disable", "enable"] | None = None,
        upload_time: str | None = None,
        uploaddir: str | None = None,
        uploadip: str | None = None,
        uploadpass: list[Any] | None = None,
        uploadport: int | None = None,
        uploadsched: Literal["disable", "enable"] | None = None,
        uploadtype: list[Any] | None = None,
        uploaduser: str | None = None,
        uploadzip: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLocallogDiskSetting", "CliGlobalSystemLocallogDiskSettingGetResponse"]
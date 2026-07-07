"""Type stubs for cli.global.system.log.settings.rolling-analyzer"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogSettingsRollingAnalyzerGetItem:
    """Item yielded when iterating over CliGlobalSystemLogSettingsRollingAnalyzerGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def days(self) -> list[Any]: ...
    @property
    def del_files(self) -> Literal["disable", "enable"]: ...
    @property
    def directory(self) -> str: ...
    @property
    def file_size(self) -> int: ...
    @property
    def gzip_format(self) -> Literal["disable", "enable"]: ...
    @property
    def hour(self) -> int: ...
    @property
    def log_format(self) -> Literal["native", "text", "csv"]: ...
    @property
    def min(self) -> int: ...
    @property
    def password(self) -> list[Any]: ...
    @property
    def password2(self) -> list[Any]: ...
    @property
    def password3(self) -> list[Any]: ...
    @property
    def port(self) -> int: ...
    @property
    def port2(self) -> int: ...
    @property
    def port3(self) -> int: ...
    @property
    def rolling_upgrade_status(self) -> int: ...
    @property
    def server(self) -> str: ...
    @property
    def server_type(self) -> Literal["ftp", "sftp", "scp"]: ...
    @property
    def server2(self) -> str: ...
    @property
    def server3(self) -> str: ...
    @property
    def upload(self) -> Literal["disable", "enable"]: ...
    @property
    def upload_hour(self) -> int: ...
    @property
    def upload_mode(self) -> Literal["backup", "mirror"]: ...
    @property
    def upload_trigger(self) -> Literal["on-roll", "on-schedule"]: ...
    @property
    def username(self) -> str: ...
    @property
    def username2(self) -> str: ...
    @property
    def username3(self) -> str: ...
    @property
    def when(self) -> Literal["none", "daily", "weekly"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogSettingsRollingAnalyzerGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogSettingsRollingAnalyzerGet endpoint with autocomplete support."""

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
    def days(self) -> list[Any] | None:
        """Field: days"""
        ...

    @property
    def del_files(self) -> Literal["disable", "enable"] | None:
        """Field: del-files"""
        ...

    @property
    def directory(self) -> str | None:
        """Field: directory"""
        ...

    @property
    def file_size(self) -> int | None:
        """Field: file-size"""
        ...

    @property
    def gzip_format(self) -> Literal["disable", "enable"] | None:
        """Field: gzip-format"""
        ...

    @property
    def hour(self) -> int | None:
        """Field: hour"""
        ...

    @property
    def log_format(self) -> Literal["native", "text", "csv"] | None:
        """Field: log-format"""
        ...

    @property
    def min(self) -> int | None:
        """Field: min"""
        ...

    @property
    def password(self) -> list[Any] | None:
        """Field: password"""
        ...

    @property
    def password2(self) -> list[Any] | None:
        """Field: password2"""
        ...

    @property
    def password3(self) -> list[Any] | None:
        """Field: password3"""
        ...

    @property
    def port(self) -> int | None:
        """Field: port"""
        ...

    @property
    def port2(self) -> int | None:
        """Field: port2"""
        ...

    @property
    def port3(self) -> int | None:
        """Field: port3"""
        ...

    @property
    def rolling_upgrade_status(self) -> int | None:
        """Field: rolling-upgrade-status"""
        ...

    @property
    def server(self) -> str | None:
        """Field: server"""
        ...

    @property
    def server_type(self) -> Literal["ftp", "sftp", "scp"] | None:
        """Field: server-type"""
        ...

    @property
    def server2(self) -> str | None:
        """Field: server2"""
        ...

    @property
    def server3(self) -> str | None:
        """Field: server3"""
        ...

    @property
    def upload(self) -> Literal["disable", "enable"] | None:
        """Field: upload"""
        ...

    @property
    def upload_hour(self) -> int | None:
        """Field: upload-hour"""
        ...

    @property
    def upload_mode(self) -> Literal["backup", "mirror"] | None:
        """Field: upload-mode"""
        ...

    @property
    def upload_trigger(self) -> Literal["on-roll", "on-schedule"] | None:
        """Field: upload-trigger"""
        ...

    @property
    def username(self) -> str | None:
        """Field: username"""
        ...

    @property
    def username2(self) -> str | None:
        """Field: username2"""
        ...

    @property
    def username3(self) -> str | None:
        """Field: username3"""
        ...

    @property
    def when(self) -> Literal["none", "daily", "weekly"] | None:
        """Field: when"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogSettingsRollingAnalyzerGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogSettingsRollingAnalyzer:
    """FortiAnalyzer endpoint: cli.global.system.log.settings.rolling-analyzer"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogSettingsRollingAnalyzerGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        days: list[Any] | None = None,
        del_files: Literal["disable", "enable"] | None = None,
        directory: str | None = None,
        file_size: int | None = None,
        gzip_format: Literal["disable", "enable"] | None = None,
        hour: int | None = None,
        log_format: Literal["native", "text", "csv"] | None = None,
        min: int | None = None,
        password: list[Any] | None = None,
        password2: list[Any] | None = None,
        password3: list[Any] | None = None,
        port: int | None = None,
        port2: int | None = None,
        port3: int | None = None,
        rolling_upgrade_status: int | None = None,
        server: str | None = None,
        server_type: Literal["ftp", "sftp", "scp"] | None = None,
        server2: str | None = None,
        server3: str | None = None,
        upload: Literal["disable", "enable"] | None = None,
        upload_hour: int | None = None,
        upload_mode: Literal["backup", "mirror"] | None = None,
        upload_trigger: Literal["on-roll", "on-schedule"] | None = None,
        username: str | None = None,
        username2: str | None = None,
        username3: str | None = None,
        when: Literal["none", "daily", "weekly"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        days: list[Any] | None = None,
        del_files: Literal["disable", "enable"] | None = None,
        directory: str | None = None,
        file_size: int | None = None,
        gzip_format: Literal["disable", "enable"] | None = None,
        hour: int | None = None,
        log_format: Literal["native", "text", "csv"] | None = None,
        min: int | None = None,
        password: list[Any] | None = None,
        password2: list[Any] | None = None,
        password3: list[Any] | None = None,
        port: int | None = None,
        port2: int | None = None,
        port3: int | None = None,
        rolling_upgrade_status: int | None = None,
        server: str | None = None,
        server_type: Literal["ftp", "sftp", "scp"] | None = None,
        server2: str | None = None,
        server3: str | None = None,
        upload: Literal["disable", "enable"] | None = None,
        upload_hour: int | None = None,
        upload_mode: Literal["backup", "mirror"] | None = None,
        upload_trigger: Literal["on-roll", "on-schedule"] | None = None,
        username: str | None = None,
        username2: str | None = None,
        username3: str | None = None,
        when: Literal["none", "daily", "weekly"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogSettingsRollingAnalyzer", "CliGlobalSystemLogSettingsRollingAnalyzerGetResponse"]
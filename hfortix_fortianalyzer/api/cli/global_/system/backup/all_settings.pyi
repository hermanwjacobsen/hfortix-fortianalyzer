"""Type stubs for cli.global.system.backup.all-settings"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemBackupAllSettingsGetItem:
    """Item yielded when iterating over CliGlobalSystemBackupAllSettingsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def cert(self) -> str: ...
    @property
    def crptpasswd(self) -> list[Any]: ...
    @property
    def directory(self) -> str: ...
    @property
    def passwd(self) -> list[Any]: ...
    @property
    def protocol(self) -> Literal["sftp", "ftp", "scp"]: ...
    @property
    def server(self) -> str: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def time(self) -> str: ...
    @property
    def user(self) -> str: ...
    @property
    def week_days(self) -> list[Any]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemBackupAllSettingsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemBackupAllSettingsGet endpoint with autocomplete support."""

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
    def cert(self) -> str | None:
        """Field: cert"""
        ...

    @property
    def crptpasswd(self) -> list[Any] | None:
        """Field: crptpasswd"""
        ...

    @property
    def directory(self) -> str | None:
        """Field: directory"""
        ...

    @property
    def passwd(self) -> list[Any] | None:
        """Field: passwd"""
        ...

    @property
    def protocol(self) -> Literal["sftp", "ftp", "scp"] | None:
        """Field: protocol"""
        ...

    @property
    def server(self) -> str | None:
        """Field: server"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def time(self) -> str | None:
        """Field: time"""
        ...

    @property
    def user(self) -> str | None:
        """Field: user"""
        ...

    @property
    def week_days(self) -> list[Any] | None:
        """Field: week_days"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemBackupAllSettingsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemBackupAllSettings:
    """FortiAnalyzer endpoint: cli.global.system.backup.all-settings"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemBackupAllSettingsGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        cert: str | None = None,
        crptpasswd: list[Any] | None = None,
        directory: str | None = None,
        passwd: list[Any] | None = None,
        protocol: Literal["sftp", "ftp", "scp"] | None = None,
        server: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        time: str | None = None,
        user: str | None = None,
        week_days: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        cert: str | None = None,
        crptpasswd: list[Any] | None = None,
        directory: str | None = None,
        passwd: list[Any] | None = None,
        protocol: Literal["sftp", "ftp", "scp"] | None = None,
        server: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        time: str | None = None,
        user: str | None = None,
        week_days: list[Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemBackupAllSettings", "CliGlobalSystemBackupAllSettingsGetResponse"]
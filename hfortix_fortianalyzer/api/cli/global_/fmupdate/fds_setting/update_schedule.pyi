"""Type stubs for cli.global.fmupdate.fds-setting.update-schedule"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFdsSettingUpdateScheduleGetItem:
    """Item yielded when iterating over CliGlobalFmupdateFdsSettingUpdateScheduleGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def day(self) -> Literal["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]: ...
    @property
    def frequency(self) -> Literal["every", "daily", "weekly"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def time(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalFmupdateFdsSettingUpdateScheduleGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateFdsSettingUpdateScheduleGet endpoint with autocomplete support."""

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
    def day(self) -> Literal["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] | None:
        """Field: day"""
        ...

    @property
    def frequency(self) -> Literal["every", "daily", "weekly"] | None:
        """Field: frequency"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def time(self) -> str | None:
        """Field: time"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateFdsSettingUpdateScheduleGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateFdsSettingUpdateSchedule:
    """FortiAnalyzer endpoint: cli.global.fmupdate.fds-setting.update-schedule"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateFdsSettingUpdateScheduleGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        day: Literal["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] | None = None,
        frequency: Literal["every", "daily", "weekly"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        time: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        day: Literal["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] | None = None,
        frequency: Literal["every", "daily", "weekly"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        time: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateFdsSettingUpdateSchedule", "CliGlobalFmupdateFdsSettingUpdateScheduleGetResponse"]
"""Type stubs for cli.global.system.locallog.memory.setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogMemorySettingGetItem:
    """Item yielded when iterating over CliGlobalSystemLocallogMemorySettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def diskfull(self) -> Literal["overwrite", "nolog"]: ...
    @property
    def severity(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocallogMemorySettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocallogMemorySettingGet endpoint with autocomplete support."""

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
    def severity(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None:
        """Field: severity"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocallogMemorySettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocallogMemorySetting:
    """FortiAnalyzer endpoint: cli.global.system.locallog.memory.setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLocallogMemorySettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        diskfull: Literal["overwrite", "nolog"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        diskfull: Literal["overwrite", "nolog"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLocallogMemorySetting", "CliGlobalSystemLocallogMemorySettingGetResponse"]
"""Type stubs for cli.global.system.alert-console"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAlertConsoleGetItem:
    """Item yielded when iterating over CliGlobalSystemAlertConsoleGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def period(self) -> Literal["1", "2", "3", "4", "5", "6", "7"]: ...
    @property
    def severity_level(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notify", "information", "debug"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAlertConsoleGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAlertConsoleGet endpoint with autocomplete support."""

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
    def period(self) -> Literal["1", "2", "3", "4", "5", "6", "7"] | None:
        """Field: period"""
        ...

    @property
    def severity_level(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notify", "information", "debug"] | None:
        """Field: severity-level"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAlertConsoleGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAlertConsole:
    """FortiAnalyzer endpoint: cli.global.system.alert-console"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemAlertConsoleGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        period: Literal["1", "2", "3", "4", "5", "6", "7"] | None = None,
        severity_level: Literal["emergency", "alert", "critical", "error", "warning", "notify", "information", "debug"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        period: Literal["1", "2", "3", "4", "5", "6", "7"] | None = None,
        severity_level: Literal["emergency", "alert", "critical", "error", "warning", "notify", "information", "debug"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemAlertConsole", "CliGlobalSystemAlertConsoleGetResponse"]
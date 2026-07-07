"""Type stubs for cli.global.system.log.alert"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogAlertGetItem:
    """Item yielded when iterating over CliGlobalSystemLogAlertGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def max_alert_count(self) -> int: ...
    @property
    def min_severity_to_raise_incident_by_grouping(self) -> Literal["none", "critical", "high"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogAlertGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogAlertGet endpoint with autocomplete support."""

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
    def max_alert_count(self) -> int | None:
        """Field: max-alert-count"""
        ...

    @property
    def min_severity_to_raise_incident_by_grouping(self) -> Literal["none", "critical", "high"] | None:
        """Field: min-severity-to-raise-incident-by-grouping"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogAlertGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogAlert:
    """FortiAnalyzer endpoint: cli.global.system.log.alert"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLogAlertGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        max_alert_count: int | None = None,
        min_severity_to_raise_incident_by_grouping: Literal["none", "critical", "high"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        max_alert_count: int | None = None,
        min_severity_to_raise_incident_by_grouping: Literal["none", "critical", "high"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLogAlert", "CliGlobalSystemLogAlertGetResponse"]
"""Type stubs for cli.global.system.auto-delete.report-auto-deletion"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAutoDeleteReportAutoDeletionGetItem:
    """Item yielded when iterating over CliGlobalSystemAutoDeleteReportAutoDeletionGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def retention(self) -> Literal["days", "weeks", "months"]: ...
    @property
    def runat(self) -> int: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def value(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAutoDeleteReportAutoDeletionGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAutoDeleteReportAutoDeletionGet endpoint with autocomplete support."""

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
    def retention(self) -> Literal["days", "weeks", "months"] | None:
        """Field: retention"""
        ...

    @property
    def runat(self) -> int | None:
        """Field: runat"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def value(self) -> int | None:
        """Field: value"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAutoDeleteReportAutoDeletionGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAutoDeleteReportAutoDeletion:
    """FortiAnalyzer endpoint: cli.global.system.auto-delete.report-auto-deletion"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemAutoDeleteReportAutoDeletionGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        retention: Literal["days", "weeks", "months"] | None = None,
        runat: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        value: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        retention: Literal["days", "weeks", "months"] | None = None,
        runat: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        value: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemAutoDeleteReportAutoDeletion", "CliGlobalSystemAutoDeleteReportAutoDeletionGetResponse"]
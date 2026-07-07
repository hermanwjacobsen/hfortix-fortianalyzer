"""Type stubs for cli.global.system.auto-delete"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAutoDeleteGetItem:
    """Item yielded when iterating over CliGlobalSystemAutoDeleteGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def dlp_files_auto_deletion(self) -> dict[str, Any]: ...
    @property
    def log_auto_deletion(self) -> dict[str, Any]: ...
    @property
    def quarantine_files_auto_deletion(self) -> dict[str, Any]: ...
    @property
    def report_auto_deletion(self) -> dict[str, Any]: ...
    @property
    def status_fake(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAutoDeleteGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAutoDeleteGet endpoint with autocomplete support."""

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
    def dlp_files_auto_deletion(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.auto-delete.dlp-files-auto-deletion)."""
        ...

    @property
    def log_auto_deletion(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.auto-delete.log-auto-deletion)."""
        ...

    @property
    def quarantine_files_auto_deletion(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.auto-delete.quarantine-files-auto-deletion)."""
        ...

    @property
    def report_auto_deletion(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.system.auto-delete.report-auto-deletion)."""
        ...

    @property
    def status_fake(self) -> int | None:
        """Field: status-fake"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAutoDeleteGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAutoDelete:
    """FortiAnalyzer endpoint: cli.global.system.auto-delete"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemAutoDeleteGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        dlp_files_auto_deletion: dict[str, Any] | None = None,
        log_auto_deletion: dict[str, Any] | None = None,
        quarantine_files_auto_deletion: dict[str, Any] | None = None,
        report_auto_deletion: dict[str, Any] | None = None,
        status_fake: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        dlp_files_auto_deletion: dict[str, Any] | None = None,
        log_auto_deletion: dict[str, Any] | None = None,
        quarantine_files_auto_deletion: dict[str, Any] | None = None,
        report_auto_deletion: dict[str, Any] | None = None,
        status_fake: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemAutoDelete", "CliGlobalSystemAutoDeleteGetResponse"]
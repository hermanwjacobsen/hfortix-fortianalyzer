"""Type stubs for cli.global.system.fortiview.setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemFortiviewSettingGetItem:
    """Item yielded when iterating over CliGlobalSystemFortiviewSettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def data_source(self) -> Literal["auto", "cache-only", "log-and-cache"]: ...
    @property
    def not_scanned_apps(self) -> Literal["exclude", "include"]: ...
    @property
    def query_run_mode(self) -> Literal["auto", "boost"]: ...
    @property
    def resolve_ip(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemFortiviewSettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemFortiviewSettingGet endpoint with autocomplete support."""

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
    def data_source(self) -> Literal["auto", "cache-only", "log-and-cache"] | None:
        """Field: data-source"""
        ...

    @property
    def not_scanned_apps(self) -> Literal["exclude", "include"] | None:
        """Field: not-scanned-apps"""
        ...

    @property
    def query_run_mode(self) -> Literal["auto", "boost"] | None:
        """Field: query-run-mode"""
        ...

    @property
    def resolve_ip(self) -> Literal["disable", "enable"] | None:
        """Field: resolve-ip"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemFortiviewSettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemFortiviewSetting:
    """FortiAnalyzer endpoint: cli.global.system.fortiview.setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemFortiviewSettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        data_source: Literal["auto", "cache-only", "log-and-cache"] | None = None,
        not_scanned_apps: Literal["exclude", "include"] | None = None,
        query_run_mode: Literal["auto", "boost"] | None = None,
        resolve_ip: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        data_source: Literal["auto", "cache-only", "log-and-cache"] | None = None,
        not_scanned_apps: Literal["exclude", "include"] | None = None,
        query_run_mode: Literal["auto", "boost"] | None = None,
        resolve_ip: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemFortiviewSetting", "CliGlobalSystemFortiviewSettingGetResponse"]
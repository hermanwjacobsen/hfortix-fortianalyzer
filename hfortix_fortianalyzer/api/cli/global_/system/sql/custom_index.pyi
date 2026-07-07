"""Type stubs for cli.global.system.sql.custom-index"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSqlCustomIndexGetItem:
    """Item yielded when iterating over CliGlobalSystemSqlCustomIndexGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def case_sensitive(self) -> Literal["disable", "enable"]: ...
    @property
    def device_type(self) -> Literal["FortiGate", "FortiMail", "FortiWeb"]: ...
    @property
    def id(self) -> int: ...
    @property
    def index_field(self) -> str: ...
    @property
    def log_type(self) -> Literal["app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "asset", "protocol", "siem", "ztna", "security"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemSqlCustomIndexGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSqlCustomIndexGet endpoint with autocomplete support."""

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
    def case_sensitive(self) -> Literal["disable", "enable"] | None:
        """Field: case-sensitive"""
        ...

    @property
    def device_type(self) -> Literal["FortiGate", "FortiMail", "FortiWeb"] | None:
        """Field: device-type"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def index_field(self) -> str | None:
        """Field: index-field"""
        ...

    @property
    def log_type(self) -> Literal["app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "asset", "protocol", "siem", "ztna", "security"] | None:
        """Field: log-type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSqlCustomIndexGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSqlCustomIndex:
    """FortiAnalyzer endpoint: cli.global.system.sql.custom-index"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        custom_index: int | str | None = None,
        fields: list[Literal["case-sensitive", "device-type", "id", "index-field", "log-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemSqlCustomIndexGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        custom_index: int | str | None = None,
        case_sensitive: Literal["disable", "enable"] | None = None,
        device_type: Literal["FortiGate", "FortiMail", "FortiWeb"] | None = None,
        id: int | None = None,
        index_field: str | None = None,
        log_type: Literal["app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "asset", "protocol", "siem", "ztna", "security"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        custom_index: int | str | None = None,
        case_sensitive: Literal["disable", "enable"] | None = None,
        device_type: Literal["FortiGate", "FortiMail", "FortiWeb"] | None = None,
        id: int | None = None,
        index_field: str | None = None,
        log_type: Literal["app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "asset", "protocol", "siem", "ztna", "security"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        custom_index: int | str | None = None,
        case_sensitive: Literal["disable", "enable"] | None = None,
        device_type: Literal["FortiGate", "FortiMail", "FortiWeb"] | None = None,
        id: int | None = None,
        index_field: str | None = None,
        log_type: Literal["app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "asset", "protocol", "siem", "ztna", "security"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        custom_index: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemSqlCustomIndex", "CliGlobalSystemSqlCustomIndexGetResponse"]
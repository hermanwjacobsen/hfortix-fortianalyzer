"""Type stubs for cli.global.system.sql"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSqlGetItem:
    """Item yielded when iterating over CliGlobalSystemSqlGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def background_rebuild(self) -> Literal["disable", "enable"]: ...
    @property
    def compress_table_min_age(self) -> int: ...
    @property
    def custom_index(self) -> list[CustomIndexItem]: ...
    @property
    def custom_skipidx(self) -> list[CustomSkipidxItem]: ...
    @property
    def database_name(self) -> str: ...
    @property
    def database_type(self) -> Literal["mysql", "postgres"]: ...
    @property
    def device_count_high(self) -> Literal["disable", "enable"]: ...
    @property
    def event_table_partition_time(self) -> int: ...
    @property
    def fct_table_partition_time(self) -> int: ...
    @property
    def logtype(self) -> list[Any]: ...
    @property
    def password(self) -> list[Any]: ...
    @property
    def prompt_sql_upgrade(self) -> Literal["disable", "enable"]: ...
    @property
    def server(self) -> str: ...
    @property
    def start_time(self) -> list[Any]: ...
    @property
    def status(self) -> Literal["disable", "local"]: ...
    @property
    def text_search_index(self) -> Literal["disable", "enable"]: ...
    @property
    def traffic_table_partition_time(self) -> int: ...
    @property
    def ts_index_field(self) -> list[TsIndexFieldItem]: ...
    @property
    def username(self) -> str: ...
    @property
    def utm_table_partition_time(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CustomIndexItem:
    """Nested item type for custom-index array."""

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

class CustomSkipidxItem:
    """Nested item type for custom-skipidx array."""

    @property
    def device_type(self) -> Literal["FortiGate", "FortiManager", "FortiClient", "FortiMail", "FortiWeb", "FortiSandbox", "FortiProxy"]: ...
    @property
    def id(self) -> int: ...
    @property
    def index_field(self) -> str: ...
    @property
    def log_type(self) -> Literal["app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "asset", "protocol", "siem", "ztna", "security"]: ...

class TsIndexFieldItem:
    """Nested item type for ts-index-field array."""

    @property
    def category(self) -> str: ...
    @property
    def value(self) -> str: ...


class CliGlobalSystemSqlGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSqlGet endpoint with autocomplete support."""

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
    def background_rebuild(self) -> Literal["disable", "enable"] | None:
        """Field: background-rebuild"""
        ...

    @property
    def compress_table_min_age(self) -> int | None:
        """Field: compress-table-min-age"""
        ...

    @property
    def custom_index(self) -> list[CustomIndexItem]:
        """Field: custom-index"""
        ...

    @property
    def custom_skipidx(self) -> list[CustomSkipidxItem]:
        """Field: custom-skipidx"""
        ...

    @property
    def database_name(self) -> str | None:
        """Field: database-name"""
        ...

    @property
    def database_type(self) -> Literal["mysql", "postgres"] | None:
        """Field: database-type"""
        ...

    @property
    def device_count_high(self) -> Literal["disable", "enable"] | None:
        """Field: device-count-high"""
        ...

    @property
    def event_table_partition_time(self) -> int | None:
        """Field: event-table-partition-time"""
        ...

    @property
    def fct_table_partition_time(self) -> int | None:
        """Field: fct-table-partition-time"""
        ...

    @property
    def logtype(self) -> list[Any] | None:
        """Field: logtype"""
        ...

    @property
    def password(self) -> list[Any] | None:
        """Field: password"""
        ...

    @property
    def prompt_sql_upgrade(self) -> Literal["disable", "enable"] | None:
        """Field: prompt-sql-upgrade"""
        ...

    @property
    def server(self) -> str | None:
        """Field: server"""
        ...

    @property
    def start_time(self) -> list[Any] | None:
        """Field: start-time"""
        ...

    @property
    def status(self) -> Literal["disable", "local"] | None:
        """Field: status"""
        ...

    @property
    def text_search_index(self) -> Literal["disable", "enable"] | None:
        """Field: text-search-index"""
        ...

    @property
    def traffic_table_partition_time(self) -> int | None:
        """Field: traffic-table-partition-time"""
        ...

    @property
    def ts_index_field(self) -> list[TsIndexFieldItem]:
        """Field: ts-index-field"""
        ...

    @property
    def username(self) -> str | None:
        """Field: username"""
        ...

    @property
    def utm_table_partition_time(self) -> int | None:
        """Field: utm-table-partition-time"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSqlGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSql:
    """FortiAnalyzer endpoint: cli.global.system.sql"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemSqlGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        background_rebuild: Literal["disable", "enable"] | None = None,
        compress_table_min_age: int | None = None,
        custom_index: list[dict[str, Any]] | None = None,
        custom_skipidx: list[dict[str, Any]] | None = None,
        database_name: str | None = None,
        database_type: Literal["mysql", "postgres"] | None = None,
        device_count_high: Literal["disable", "enable"] | None = None,
        event_table_partition_time: int | None = None,
        fct_table_partition_time: int | None = None,
        logtype: list[Any] | None = None,
        password: list[Any] | None = None,
        prompt_sql_upgrade: Literal["disable", "enable"] | None = None,
        server: str | None = None,
        start_time: list[Any] | None = None,
        status: Literal["disable", "local"] | None = None,
        text_search_index: Literal["disable", "enable"] | None = None,
        traffic_table_partition_time: int | None = None,
        ts_index_field: list[dict[str, Any]] | None = None,
        username: str | None = None,
        utm_table_partition_time: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        background_rebuild: Literal["disable", "enable"] | None = None,
        compress_table_min_age: int | None = None,
        custom_index: list[dict[str, Any]] | None = None,
        custom_skipidx: list[dict[str, Any]] | None = None,
        database_name: str | None = None,
        database_type: Literal["mysql", "postgres"] | None = None,
        device_count_high: Literal["disable", "enable"] | None = None,
        event_table_partition_time: int | None = None,
        fct_table_partition_time: int | None = None,
        logtype: list[Any] | None = None,
        password: list[Any] | None = None,
        prompt_sql_upgrade: Literal["disable", "enable"] | None = None,
        server: str | None = None,
        start_time: list[Any] | None = None,
        status: Literal["disable", "local"] | None = None,
        text_search_index: Literal["disable", "enable"] | None = None,
        traffic_table_partition_time: int | None = None,
        ts_index_field: list[dict[str, Any]] | None = None,
        username: str | None = None,
        utm_table_partition_time: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemSql", "CliGlobalSystemSqlGetResponse"]
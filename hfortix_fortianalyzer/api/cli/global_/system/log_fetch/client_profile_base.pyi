"""Type stubs for cli.global.system.log-fetch.client-profile"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogFetchClientProfileGetItem:
    """Item yielded when iterating over CliGlobalSystemLogFetchClientProfileGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def client_adom(self) -> str: ...
    @property
    def data_range(self) -> Literal["custom"]: ...
    @property
    def data_range_value(self) -> int: ...
    @property
    def device_filter(self) -> list[DeviceFilterItem]: ...
    @property
    def end_time(self) -> list[Any]: ...
    @property
    def id(self) -> int: ...
    @property
    def index_fetch_logs(self) -> Literal["disable", "enable"]: ...
    @property
    def log_filter(self) -> list[LogFilterItem]: ...
    @property
    def log_filter_logic(self) -> Literal["and", "or"]: ...
    @property
    def log_filter_status(self) -> Literal["disable", "enable"]: ...
    @property
    def name(self) -> str: ...
    @property
    def password(self) -> list[Any]: ...
    @property
    def peer_cert_cn(self) -> str: ...
    @property
    def secure_connection(self) -> Literal["disable", "enable"]: ...
    @property
    def server_adom(self) -> str: ...
    @property
    def server_ip(self) -> str: ...
    @property
    def start_time(self) -> list[Any]: ...
    @property
    def sync_adom_config(self) -> Literal["disable", "enable"]: ...
    @property
    def user(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class DeviceFilterItem:
    """Nested item type for device-filter array."""

    @property
    def adom(self) -> str: ...
    @property
    def device(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def vdom(self) -> str: ...

class LogFilterItem:
    """Nested item type for log-filter array."""

    @property
    def field(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def oper(self) -> Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"]: ...
    @property
    def value(self) -> str: ...


class CliGlobalSystemLogFetchClientProfileGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogFetchClientProfileGet endpoint with autocomplete support."""

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
    def client_adom(self) -> str | None:
        """Field: client-adom"""
        ...

    @property
    def data_range(self) -> Literal["custom"] | None:
        """Field: data-range"""
        ...

    @property
    def data_range_value(self) -> int | None:
        """Field: data-range-value"""
        ...

    @property
    def device_filter(self) -> list[DeviceFilterItem]:
        """Field: device-filter"""
        ...

    @property
    def end_time(self) -> list[Any] | None:
        """Field: end-time"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def index_fetch_logs(self) -> Literal["disable", "enable"] | None:
        """Field: index-fetch-logs"""
        ...

    @property
    def log_filter(self) -> list[LogFilterItem]:
        """Field: log-filter"""
        ...

    @property
    def log_filter_logic(self) -> Literal["and", "or"] | None:
        """Field: log-filter-logic"""
        ...

    @property
    def log_filter_status(self) -> Literal["disable", "enable"] | None:
        """Field: log-filter-status"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def password(self) -> list[Any] | None:
        """Field: password"""
        ...

    @property
    def peer_cert_cn(self) -> str | None:
        """Field: peer-cert-cn"""
        ...

    @property
    def secure_connection(self) -> Literal["disable", "enable"] | None:
        """Field: secure-connection"""
        ...

    @property
    def server_adom(self) -> str | None:
        """Field: server-adom"""
        ...

    @property
    def server_ip(self) -> str | None:
        """Field: server-ip"""
        ...

    @property
    def start_time(self) -> list[Any] | None:
        """Field: start-time"""
        ...

    @property
    def sync_adom_config(self) -> Literal["disable", "enable"] | None:
        """Field: sync-adom-config"""
        ...

    @property
    def user(self) -> str | None:
        """Field: user"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogFetchClientProfileGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogFetchClientProfile:
    """FortiAnalyzer endpoint: cli.global.system.log-fetch.client-profile"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        client_profile: int | str | None = None,
        fields: list[Literal["client-adom", "data-range", "data-range-value", "end-time", "id", "index-fetch-logs", "log-filter-logic", "log-filter-status", "name", "password", "peer-cert-cn", "secure-connection", "server-adom", "server-ip", "start-time", "sync-adom-config", "user"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLogFetchClientProfileGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        client_profile: int | str | None = None,
        client_adom: str | None = None,
        data_range: Literal["custom"] | None = None,
        data_range_value: int | None = None,
        device_filter: list[dict[str, Any]] | None = None,
        end_time: list[Any] | None = None,
        id: int | None = None,
        index_fetch_logs: Literal["disable", "enable"] | None = None,
        log_filter: list[dict[str, Any]] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        peer_cert_cn: str | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        server_adom: str | None = None,
        server_ip: str | None = None,
        start_time: list[Any] | None = None,
        sync_adom_config: Literal["disable", "enable"] | None = None,
        user: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        client_profile: int | str | None = None,
        client_adom: str | None = None,
        data_range: Literal["custom"] | None = None,
        data_range_value: int | None = None,
        device_filter: list[dict[str, Any]] | None = None,
        end_time: list[Any] | None = None,
        id: int | None = None,
        index_fetch_logs: Literal["disable", "enable"] | None = None,
        log_filter: list[dict[str, Any]] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        peer_cert_cn: str | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        server_adom: str | None = None,
        server_ip: str | None = None,
        start_time: list[Any] | None = None,
        sync_adom_config: Literal["disable", "enable"] | None = None,
        user: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        client_profile: int | str | None = None,
        client_adom: str | None = None,
        data_range: Literal["custom"] | None = None,
        data_range_value: int | None = None,
        device_filter: list[dict[str, Any]] | None = None,
        end_time: list[Any] | None = None,
        id: int | None = None,
        index_fetch_logs: Literal["disable", "enable"] | None = None,
        log_filter: list[dict[str, Any]] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        peer_cert_cn: str | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        server_adom: str | None = None,
        server_ip: str | None = None,
        start_time: list[Any] | None = None,
        sync_adom_config: Literal["disable", "enable"] | None = None,
        user: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        client_profile: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLogFetchClientProfile", "CliGlobalSystemLogFetchClientProfileGetResponse"]
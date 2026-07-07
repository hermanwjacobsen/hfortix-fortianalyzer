"""Type stubs for cli.global.system.log-forward.log-filter"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogForwardLogFilterGetItem:
    """Item yielded when iterating over CliGlobalSystemLogForwardLogFilterGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def field(self) -> Literal["type", "logid", "level", "devid", "vd", "srcip", "srcintf", "dstip", "dstintf", "dstport", "user", "group", "free-text"]: ...
    @property
    def id(self) -> int: ...
    @property
    def oper(self) -> Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"]: ...
    @property
    def value(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogForwardLogFilterGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogForwardLogFilterGet endpoint with autocomplete support."""

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
    def field(self) -> Literal["type", "logid", "level", "devid", "vd", "srcip", "srcintf", "dstip", "dstintf", "dstport", "user", "group", "free-text"] | None:
        """Field: field"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def oper(self) -> Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"] | None:
        """Field: oper"""
        ...

    @property
    def value(self) -> str | None:
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogForwardLogFilterGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogForwardLogFilter:
    """FortiAnalyzer endpoint: cli.global.system.log-forward.log-filter"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        log_forward: str,
        log_filter: int | str | None = None,
        fields: list[Literal["field", "id", "oper", "value"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLogForwardLogFilterGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        log_forward: str,
        log_filter: int | str | None = None,
        field: Literal["type", "logid", "level", "devid", "vd", "srcip", "srcintf", "dstip", "dstintf", "dstport", "user", "group", "free-text"] | None = None,
        id: int | None = None,
        oper: Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"] | None = None,
        value: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        log_forward: str,
        log_filter: int | str | None = None,
        field: Literal["type", "logid", "level", "devid", "vd", "srcip", "srcintf", "dstip", "dstintf", "dstport", "user", "group", "free-text"] | None = None,
        id: int | None = None,
        oper: Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"] | None = None,
        value: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        log_forward: str,
        log_filter: int | str | None = None,
        field: Literal["type", "logid", "level", "devid", "vd", "srcip", "srcintf", "dstip", "dstintf", "dstport", "user", "group", "free-text"] | None = None,
        id: int | None = None,
        oper: Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"] | None = None,
        value: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        log_forward: str,
        log_filter: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLogForwardLogFilter", "CliGlobalSystemLogForwardLogFilterGetResponse"]
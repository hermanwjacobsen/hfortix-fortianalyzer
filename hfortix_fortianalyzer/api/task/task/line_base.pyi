"""Type stubs for task.task.line"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class TaskTaskLineGetItem:
    """Item yielded when iterating over TaskTaskLineGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def detail(self) -> str: ...
    @property
    def end_tm(self) -> int: ...
    @property
    def err(self) -> int: ...
    @property
    def history(self) -> list[HistoryItem]: ...
    @property
    def ip(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def oid(self) -> int: ...
    @property
    def percent(self) -> int: ...
    @property
    def poid(self) -> int: ...
    @property
    def start_tm(self) -> int: ...
    @property
    def state(self) -> Literal["pending", "running", "cancelling", "cancelled", "done", "error", "aborting", "aborted", "warning", "to_continue", "unknown"]: ...
    @property
    def vdom(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class HistoryItem:
    """Nested item type for history array."""

    @property
    def detail(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def percent(self) -> int: ...
    @property
    def state(self) -> int: ...
    @property
    def vdom(self) -> str: ...


class TaskTaskLineGetResponse(FortiAnalyzerResponse):
    """Typed response for TaskTaskLineGet endpoint with autocomplete support."""

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
    def detail(self) -> str | None:
        """Field: detail"""
        ...

    @property
    def end_tm(self) -> int | None:
        """Field: end_tm"""
        ...

    @property
    def err(self) -> int | None:
        """Field: err"""
        ...

    @property
    def history(self) -> list[HistoryItem]:
        """Field: history"""
        ...

    @property
    def ip(self) -> str | None:
        """Field: ip"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def oid(self) -> int | None:
        """Field: oid"""
        ...

    @property
    def percent(self) -> int | None:
        """Field: percent"""
        ...

    @property
    def poid(self) -> int | None:
        """Field: poid"""
        ...

    @property
    def start_tm(self) -> int | None:
        """Field: start_tm"""
        ...

    @property
    def state(self) -> Literal["pending", "running", "cancelling", "cancelled", "done", "error", "aborting", "aborted", "warning", "to_continue", "unknown"] | None:
        """Field: state"""
        ...

    @property
    def vdom(self) -> str | None:
        """Field: vdom"""
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
    def __iter__(self) -> Iterator[TaskTaskLineGetItem]: ...
    def __len__(self) -> int: ...


class TaskTaskLine:
    """FortiAnalyzer endpoint: task.task.line"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        task: str,
        line: int | str | None = None,
        fields: list[Literal["detail", "end_tm", "err", "ip", "name", "oid", "percent", "poid", "start_tm", "state", "vdom"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> TaskTaskLineGetResponse:
        """GET operation."""
        ...


__all__ = ["TaskTaskLine", "TaskTaskLineGetResponse"]
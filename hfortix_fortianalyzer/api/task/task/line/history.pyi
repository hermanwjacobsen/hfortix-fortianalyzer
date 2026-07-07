"""Type stubs for task.task.line.history"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class TaskTaskLineHistoryGetItem:
    """Item yielded when iterating over TaskTaskLineHistoryGetResponse."""

    @property
    def oid(self) -> int: ...
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

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class TaskTaskLineHistoryGetResponse(FortiAnalyzerResponse):
    """Typed response for TaskTaskLineHistoryGet endpoint with autocomplete support."""

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
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def percent(self) -> int | None:
        """Field: percent"""
        ...

    @property
    def state(self) -> int | None:
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
    def __iter__(self) -> Iterator[TaskTaskLineHistoryGetItem]: ...
    def __len__(self) -> int: ...


class TaskTaskLineHistory:
    """FortiAnalyzer endpoint: task.task.line.history"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        task: str,
        line: str,
        history: int | str | None = None,
        fields: list[Literal["detail", "name", "percent", "state", "vdom"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> TaskTaskLineHistoryGetResponse:
        """GET operation."""
        ...


__all__ = ["TaskTaskLineHistory", "TaskTaskLineHistoryGetResponse"]
"""Type stubs for task.task"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class TaskTaskGetItem:
    """Item yielded when iterating over TaskTaskGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def adom(self) -> int: ...
    @property
    def end_tm(self) -> int: ...
    @property
    def flags(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def line(self) -> list[LineItem]: ...
    @property
    def num_done(self) -> int: ...
    @property
    def num_err(self) -> int: ...
    @property
    def num_lines(self) -> int: ...
    @property
    def num_warn(self) -> int: ...
    @property
    def percent(self) -> int: ...
    @property
    def pid(self) -> int: ...
    @property
    def src(self) -> Literal["device manager", "security console", "global object", "config installation", "script installation", "check point", "import objects", "import interfaces and zones", "import policy", "ems policy", "policy check", "assignment", "object assignment", "cloning package", "certificate enrollment", "install objects", "install device", "fwm", "integrity check", "cloning policy block", "import config", "generate controllers", "unknown"]: ...
    @property
    def start_tm(self) -> int: ...
    @property
    def state(self) -> Literal["pending", "running", "cancelling", "cancelled", "done", "error", "aborting", "aborted", "warning", "to_continue", "unknown"]: ...
    @property
    def title(self) -> str: ...
    @property
    def tot_percent(self) -> int: ...
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


class LineItem:
    """Nested item type for line array."""

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


class TaskTaskGetResponse(FortiAnalyzerResponse):
    """Typed response for TaskTaskGet endpoint with autocomplete support."""

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
    def adom(self) -> int | None:
        """Field: adom"""
        ...

    @property
    def end_tm(self) -> int | None:
        """Field: end_tm"""
        ...

    @property
    def flags(self) -> int | None:
        """Field: flags"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def line(self) -> list[LineItem]:
        """Field: line"""
        ...

    @property
    def num_done(self) -> int | None:
        """Field: num_done"""
        ...

    @property
    def num_err(self) -> int | None:
        """Field: num_err"""
        ...

    @property
    def num_lines(self) -> int | None:
        """Field: num_lines"""
        ...

    @property
    def num_warn(self) -> int | None:
        """Field: num_warn"""
        ...

    @property
    def percent(self) -> int | None:
        """Field: percent"""
        ...

    @property
    def pid(self) -> int | None:
        """Field: pid"""
        ...

    @property
    def src(self) -> Literal["device manager", "security console", "global object", "config installation", "script installation", "check point", "import objects", "import interfaces and zones", "import policy", "ems policy", "policy check", "assignment", "object assignment", "cloning package", "certificate enrollment", "install objects", "install device", "fwm", "integrity check", "cloning policy block", "import config", "generate controllers", "unknown"] | None:
        """Field: src"""
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
    def title(self) -> str | None:
        """Field: title"""
        ...

    @property
    def tot_percent(self) -> int | None:
        """Field: tot_percent"""
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
    def __iter__(self) -> Iterator[TaskTaskGetItem]: ...
    def __len__(self) -> int: ...


class TaskTask:
    """FortiAnalyzer endpoint: task.task"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        task: int | str | None = None,
        fields: list[Literal["adom", "end_tm", "flags", "id", "num_done", "num_err", "num_lines", "num_warn", "percent", "pid", "src", "start_tm", "state", "title", "tot_percent", "user"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> TaskTaskGetResponse:
        """GET operation."""
        ...


__all__ = ["TaskTask", "TaskTaskGetResponse"]
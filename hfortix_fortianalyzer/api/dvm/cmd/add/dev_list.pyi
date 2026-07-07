"""Type stubs for dvm.cmd.add.dev-list"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmCmdAddDevListExecItem:
    """Item yielded when iterating over DvmCmdAddDevListExecResponse."""

    @property
    def pid(self) -> int: ...
    @property
    def taskid(self) -> list[Any]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class DvmCmdAddDevListExecResponse(FortiAnalyzerResponse):
    """Typed response for DvmCmdAddDevListExec endpoint with autocomplete support."""

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
    def pid(self) -> int | None:
        """When "nonblocking" flag is set, return the process ID for the command."""
        ...

    @property
    def taskid(self) -> list[Any] | None:
        """When "create_task" flag is set, return the ID of the task associated with the..."""
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
    def __iter__(self) -> Iterator[DvmCmdAddDevListExecItem]: ...
    def __len__(self) -> int: ...


class DvmCmdAddDevList:
    """FortiAnalyzer endpoint: dvm.cmd.add.dev-list"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        add_dev_list: list[dict[str, Any]] | None = None,
        adom: list[Any] | None = None,
        flags: list[Any] | None = None,
    ) -> DvmCmdAddDevListExecResponse:
        """EXEC operation."""
        ...


__all__ = ["DvmCmdAddDevList", "DvmCmdAddDevListExecResponse"]
"""Type stubs for dvm.cmd.add.device"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmCmdAddDeviceExecItem:
    """Item yielded when iterating over DvmCmdAddDeviceExecResponse."""

    @property
    def device(self) -> dict[str, Any]: ...
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


class DvmCmdAddDeviceExecResponse(FortiAnalyzerResponse):
    """Typed response for DvmCmdAddDeviceExec endpoint with autocomplete support."""

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
    def device(self) -> dict[str, Any] | None:
        """Nested object (schema: dvmdb.device)."""
        ...

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
    def __iter__(self) -> Iterator[DvmCmdAddDeviceExecItem]: ...
    def __len__(self) -> int: ...


class DvmCmdAddDevice:
    """FortiAnalyzer endpoint: dvm.cmd.add.device"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        adom: list[Any] | None = None,
        device: dict[str, Any] | None = None,
        flags: list[Any] | None = None,
        groups: list[Any] | None = None,
    ) -> DvmCmdAddDeviceExecResponse:
        """EXEC operation."""
        ...


__all__ = ["DvmCmdAddDevice", "DvmCmdAddDeviceExecResponse"]
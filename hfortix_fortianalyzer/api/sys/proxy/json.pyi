"""Type stubs for sys.proxy.json"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysProxyJsonExecItem:
    """Item yielded when iterating over SysProxyJsonExecResponse."""

    @property
    def response(self) -> dict[str, Any]: ...
    @property
    def target(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class SysProxyJsonExecResponse(FortiAnalyzerResponse):
    """Typed response for SysProxyJsonExec endpoint with autocomplete support."""

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
    def response(self) -> dict[str, Any] | None:
        """Nested object (schema: resp.sys.proxy.json.response.response)."""
        ...

    @property
    def target(self) -> str | None:
        """The name of the device where the set of data is belonged to."""
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
    def __iter__(self) -> Iterator[SysProxyJsonExecItem]: ...
    def __len__(self) -> int: ...


class SysProxyJson:
    """FortiAnalyzer endpoint: sys.proxy.json"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        action: Literal["get", "post", "put", "delete"] | None = None,
        payload: dict[str, Any] | None = None,
        resource: str | None = None,
        target: list[Any] | None = None,
        timeout: int | None = None,
    ) -> SysProxyJsonExecResponse:
        """EXEC operation."""
        ...


__all__ = ["SysProxyJson", "SysProxyJsonExecResponse"]
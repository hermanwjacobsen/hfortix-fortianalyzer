"""Type stubs for sys.api.sdnconnector"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysApiSdnconnectorExecItem:
    """Item yielded when iterating over SysApiSdnconnectorExecResponse."""

    @property
    def data(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class SysApiSdnconnectorExecResponse(FortiAnalyzerResponse):
    """Typed response for SysApiSdnconnectorExec endpoint with autocomplete support."""

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
    def data(self) -> str | None:
        """Query response in string format."""
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
    def __iter__(self) -> Iterator[SysApiSdnconnectorExecItem]: ...
    def __len__(self) -> int: ...


class SysApiSdnconnector:
    """FortiAnalyzer endpoint: sys.api.sdnconnector"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        adom: str | None = None,
        command: str | None = None,
        connector_name: str | None = None,
    ) -> SysApiSdnconnectorExecResponse:
        """EXEC operation."""
        ...


__all__ = ["SysApiSdnconnector", "SysApiSdnconnectorExecResponse"]
"""Type stubs for sys.generate.wsdl"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysGenerateWsdlExecItem:
    """Item yielded when iterating over SysGenerateWsdlExecResponse."""

    @property
    def syntax(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class SysGenerateWsdlExecResponse(FortiAnalyzerResponse):
    """Typed response for SysGenerateWsdlExec endpoint with autocomplete support."""

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
    def syntax(self) -> str | None:
        """Generated output of module/object syntax in WSDL format."""
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
    def __iter__(self) -> Iterator[SysGenerateWsdlExecItem]: ...
    def __len__(self) -> int: ...


class SysGenerateWsdl:
    """FortiAnalyzer endpoint: sys.generate.wsdl"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        endpoint: str | None = None,
        target: str | None = None,
    ) -> SysGenerateWsdlExecResponse:
        """EXEC operation."""
        ...


__all__ = ["SysGenerateWsdl", "SysGenerateWsdlExecResponse"]
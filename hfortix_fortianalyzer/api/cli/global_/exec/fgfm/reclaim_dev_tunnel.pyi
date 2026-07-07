"""Type stubs for cli.global.exec.fgfm.reclaim-dev-tunnel"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalExecFgfmReclaimDevTunnelExecItem:
    """Item yielded when iterating over CliGlobalExecFgfmReclaimDevTunnelExecResponse."""

    @property
    def assigned_ip(self) -> str: ...
    @property
    def branch_pt(self) -> int: ...
    @property
    def build(self) -> int: ...
    @property
    def managed_serial(self) -> str: ...
    @property
    def platform_str(self) -> str: ...
    @property
    def serialno(self) -> str: ...
    @property
    def version(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalExecFgfmReclaimDevTunnelExecResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalExecFgfmReclaimDevTunnelExec endpoint with autocomplete support."""

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
    def assigned_ip(self) -> str | None:
        """Field: assigned_ip"""
        ...

    @property
    def branch_pt(self) -> int | None:
        """Field: branch_pt"""
        ...

    @property
    def build(self) -> int | None:
        """Field: build"""
        ...

    @property
    def managed_serial(self) -> str | None:
        """Field: managed_serial"""
        ...

    @property
    def platform_str(self) -> str | None:
        """Field: platform_str"""
        ...

    @property
    def serialno(self) -> str | None:
        """Field: serialno"""
        ...

    @property
    def version(self) -> int | None:
        """Field: version"""
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
    def __iter__(self) -> Iterator[CliGlobalExecFgfmReclaimDevTunnelExecItem]: ...
    def __len__(self) -> int: ...


class CliGlobalExecFgfmReclaimDevTunnel:
    """FortiAnalyzer endpoint: cli.global.exec.fgfm.reclaim-dev-tunnel"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        flags: list[Any] | None = None,
    ) -> CliGlobalExecFgfmReclaimDevTunnelExecResponse:
        """EXEC operation."""
        ...


__all__ = ["CliGlobalExecFgfmReclaimDevTunnel", "CliGlobalExecFgfmReclaimDevTunnelExecResponse"]
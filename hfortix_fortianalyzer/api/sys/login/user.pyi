"""Type stubs for sys.login.user"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysLoginUserExecItem:
    """Item yielded when iterating over SysLoginUserExecResponse."""

    @property
    def challenge(self) -> str: ...
    @property
    def session(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class SysLoginUserExecResponse(FortiAnalyzerResponse):
    """Typed response for SysLoginUserExec endpoint with autocomplete support."""

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
    def challenge(self) -> str | None:
        """The log in challenge question. User must follow this request with a <a href="..."""
        ...

    @property
    def session(self) -> str | None:
        """If there is a log in challenge, a temporary session is created. Use this sess..."""
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
    def __iter__(self) -> Iterator[SysLoginUserExecItem]: ...
    def __len__(self) -> int: ...


class SysLoginUser:
    """FortiAnalyzer endpoint: sys.login.user"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        passwd: str | None = None,
        user: str | None = None,
    ) -> SysLoginUserExecResponse:
        """EXEC operation."""
        ...


__all__ = ["SysLoginUser", "SysLoginUserExecResponse"]
"""Type stubs for sys.login.challenge"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SysLoginChallengeExecItem:
    """Item yielded when iterating over SysLoginChallengeExecResponse."""

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


class SysLoginChallengeExecResponse(FortiAnalyzerResponse):
    """Typed response for SysLoginChallengeExec endpoint with autocomplete support."""

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
        """New challenge question that must be answered with another <a href="#login_cha..."""
        ...

    @property
    def session(self) -> str | None:
        """If there is further challenge question(s), the session is used to along with ..."""
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
    def __iter__(self) -> Iterator[SysLoginChallengeExecItem]: ...
    def __len__(self) -> int: ...


class SysLoginChallenge:
    """FortiAnalyzer endpoint: sys.login.challenge"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        answer: str | None = None,
        session: str | None = None,
    ) -> SysLoginChallengeExecResponse:
        """EXEC operation."""
        ...


__all__ = ["SysLoginChallenge", "SysLoginChallengeExecResponse"]
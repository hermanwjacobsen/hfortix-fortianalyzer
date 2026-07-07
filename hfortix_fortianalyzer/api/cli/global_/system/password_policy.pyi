"""Type stubs for cli.global.system.password-policy"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemPasswordPolicyGetItem:
    """Item yielded when iterating over CliGlobalSystemPasswordPolicyGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def change_4_characters(self) -> Literal["disable", "enable"]: ...
    @property
    def expire(self) -> int: ...
    @property
    def login_lockout_upon_downgrade(self) -> Literal["disable", "enable"]: ...
    @property
    def minimum_length(self) -> int: ...
    @property
    def must_contain(self) -> list[Any]: ...
    @property
    def password_history(self) -> int: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemPasswordPolicyGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemPasswordPolicyGet endpoint with autocomplete support."""

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
    def change_4_characters(self) -> Literal["disable", "enable"] | None:
        """Field: change-4-characters"""
        ...

    @property
    def expire(self) -> int | None:
        """Field: expire"""
        ...

    @property
    def login_lockout_upon_downgrade(self) -> Literal["disable", "enable"] | None:
        """Field: login-lockout-upon-downgrade"""
        ...

    @property
    def minimum_length(self) -> int | None:
        """Field: minimum-length"""
        ...

    @property
    def must_contain(self) -> list[Any] | None:
        """Field: must-contain"""
        ...

    @property
    def password_history(self) -> int | None:
        """Field: password-history"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemPasswordPolicyGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemPasswordPolicy:
    """FortiAnalyzer endpoint: cli.global.system.password-policy"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemPasswordPolicyGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        change_4_characters: Literal["disable", "enable"] | None = None,
        expire: int | None = None,
        login_lockout_upon_downgrade: Literal["disable", "enable"] | None = None,
        minimum_length: int | None = None,
        must_contain: list[Any] | None = None,
        password_history: int | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        change_4_characters: Literal["disable", "enable"] | None = None,
        expire: int | None = None,
        login_lockout_upon_downgrade: Literal["disable", "enable"] | None = None,
        minimum_length: int | None = None,
        must_contain: list[Any] | None = None,
        password_history: int | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemPasswordPolicy", "CliGlobalSystemPasswordPolicyGetResponse"]
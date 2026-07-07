"""Type stubs for cli.global.system.admin.user.adom"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminUserAdomGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminUserAdomGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def adom_name(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAdminUserAdomGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminUserAdomGet endpoint with autocomplete support."""

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
    def adom_name(self) -> str | None:
        """Field: adom-name"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminUserAdomGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminUserAdom:
    """FortiAnalyzer endpoint: cli.global.system.admin.user.adom"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        user: str,
        adom: int | str | None = None,
        fields: list[Literal["adom-name"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminUserAdomGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        user: str,
        adom: int | str | None = None,
        adom_name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        user: str,
        adom: int | str | None = None,
        adom_name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        user: str,
        adom: int | str | None = None,
        adom_name: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        user: str,
        adom: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminUserAdom", "CliGlobalSystemAdminUserAdomGetResponse"]
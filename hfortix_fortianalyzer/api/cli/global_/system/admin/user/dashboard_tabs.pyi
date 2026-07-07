"""Type stubs for cli.global.system.admin.user.dashboard-tabs"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminUserDashboardTabsGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminUserDashboardTabsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def tabid(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAdminUserDashboardTabsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminUserDashboardTabsGet endpoint with autocomplete support."""

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
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def tabid(self) -> int | None:
        """Field: tabid"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminUserDashboardTabsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminUserDashboardTabs:
    """FortiAnalyzer endpoint: cli.global.system.admin.user.dashboard-tabs"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        user: str,
        dashboard_tabs: int | str | None = None,
        fields: list[Literal["name", "tabid"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminUserDashboardTabsGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        user: str,
        dashboard_tabs: int | str | None = None,
        name: str | None = None,
        tabid: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        user: str,
        dashboard_tabs: int | str | None = None,
        name: str | None = None,
        tabid: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        user: str,
        dashboard_tabs: int | str | None = None,
        name: str | None = None,
        tabid: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        user: str,
        dashboard_tabs: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminUserDashboardTabs", "CliGlobalSystemAdminUserDashboardTabsGetResponse"]
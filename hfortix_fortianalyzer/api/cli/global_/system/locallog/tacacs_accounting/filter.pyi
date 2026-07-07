"""Type stubs for cli.global.system.locallog.tacacs+accounting.filter"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogTacacsAccountingFilterGetItem:
    """Item yielded when iterating over CliGlobalSystemLocallogTacacsAccountingFilterGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def cli_cmd_audit(self) -> Literal["disable", "enable"]: ...
    @property
    def config_change_audit(self) -> Literal["disable", "enable"]: ...
    @property
    def login_audit(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocallogTacacsAccountingFilterGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocallogTacacsAccountingFilterGet endpoint with autocomplete support."""

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
    def cli_cmd_audit(self) -> Literal["disable", "enable"] | None:
        """Field: cli-cmd-audit"""
        ...

    @property
    def config_change_audit(self) -> Literal["disable", "enable"] | None:
        """Field: config-change-audit"""
        ...

    @property
    def login_audit(self) -> Literal["disable", "enable"] | None:
        """Field: login-audit"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocallogTacacsAccountingFilterGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocallogTacacsAccountingFilter:
    """FortiAnalyzer endpoint: cli.global.system.locallog.tacacs+accounting.filter"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLocallogTacacsAccountingFilterGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        cli_cmd_audit: Literal["disable", "enable"] | None = None,
        config_change_audit: Literal["disable", "enable"] | None = None,
        login_audit: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        cli_cmd_audit: Literal["disable", "enable"] | None = None,
        config_change_audit: Literal["disable", "enable"] | None = None,
        login_audit: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLocallogTacacsAccountingFilter", "CliGlobalSystemLocallogTacacsAccountingFilterGetResponse"]
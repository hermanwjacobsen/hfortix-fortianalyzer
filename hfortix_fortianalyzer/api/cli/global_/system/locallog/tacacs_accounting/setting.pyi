"""Type stubs for cli.global.system.locallog.tacacs+accounting.setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogTacacsAccountingSettingGetItem:
    """Item yielded when iterating over CliGlobalSystemLocallogTacacsAccountingSettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def tacacs_name(self) -> str: ...
    @property
    def timeout(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocallogTacacsAccountingSettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocallogTacacsAccountingSettingGet endpoint with autocomplete support."""

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
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def tacacs_name(self) -> str | None:
        """Field: tacacs-name"""
        ...

    @property
    def timeout(self) -> int | None:
        """Field: timeout"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocallogTacacsAccountingSettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocallogTacacsAccountingSetting:
    """FortiAnalyzer endpoint: cli.global.system.locallog.tacacs+accounting.setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLocallogTacacsAccountingSettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        status: Literal["disable", "enable"] | None = None,
        tacacs_name: str | None = None,
        timeout: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        status: Literal["disable", "enable"] | None = None,
        tacacs_name: str | None = None,
        timeout: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLocallogTacacsAccountingSetting", "CliGlobalSystemLocallogTacacsAccountingSettingGetResponse"]
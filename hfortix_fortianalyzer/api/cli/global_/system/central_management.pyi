"""Type stubs for cli.global.system.central-management"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCentralManagementGetItem:
    """Item yielded when iterating over CliGlobalSystemCentralManagementGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def acctid(self) -> str: ...
    @property
    def allow_monitor(self) -> Literal["disable", "enable"]: ...
    @property
    def authorized_manager_only(self) -> Literal["disable", "enable"]: ...
    @property
    def elite_service(self) -> Literal["disable", "enable"]: ...
    @property
    def enc_algorithm(self) -> Literal["default", "low", "high"]: ...
    @property
    def fmg(self) -> str: ...
    @property
    def mgmtid(self) -> str: ...
    @property
    def serial_number(self) -> list[Any]: ...
    @property
    def socaas_remote_access(self) -> Literal["disable", "enable"]: ...
    @property
    def type(self) -> Literal["fortimanager", "cloud-management", "none"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemCentralManagementGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCentralManagementGet endpoint with autocomplete support."""

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
    def acctid(self) -> str | None:
        """Field: acctid"""
        ...

    @property
    def allow_monitor(self) -> Literal["disable", "enable"] | None:
        """Field: allow-monitor"""
        ...

    @property
    def authorized_manager_only(self) -> Literal["disable", "enable"] | None:
        """Field: authorized-manager-only"""
        ...

    @property
    def elite_service(self) -> Literal["disable", "enable"] | None:
        """Field: elite-service"""
        ...

    @property
    def enc_algorithm(self) -> Literal["default", "low", "high"] | None:
        """Field: enc-algorithm"""
        ...

    @property
    def fmg(self) -> str | None:
        """Field: fmg"""
        ...

    @property
    def mgmtid(self) -> str | None:
        """Field: mgmtid"""
        ...

    @property
    def serial_number(self) -> list[Any] | None:
        """Field: serial-number"""
        ...

    @property
    def socaas_remote_access(self) -> Literal["disable", "enable"] | None:
        """Field: socaas-remote-access"""
        ...

    @property
    def type(self) -> Literal["fortimanager", "cloud-management", "none"] | None:
        """Field: type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemCentralManagementGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCentralManagement:
    """FortiAnalyzer endpoint: cli.global.system.central-management"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemCentralManagementGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        acctid: str | None = None,
        allow_monitor: Literal["disable", "enable"] | None = None,
        authorized_manager_only: Literal["disable", "enable"] | None = None,
        elite_service: Literal["disable", "enable"] | None = None,
        enc_algorithm: Literal["default", "low", "high"] | None = None,
        fmg: str | None = None,
        mgmtid: str | None = None,
        serial_number: list[Any] | None = None,
        socaas_remote_access: Literal["disable", "enable"] | None = None,
        type: Literal["fortimanager", "cloud-management", "none"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        acctid: str | None = None,
        allow_monitor: Literal["disable", "enable"] | None = None,
        authorized_manager_only: Literal["disable", "enable"] | None = None,
        elite_service: Literal["disable", "enable"] | None = None,
        enc_algorithm: Literal["default", "low", "high"] | None = None,
        fmg: str | None = None,
        mgmtid: str | None = None,
        serial_number: list[Any] | None = None,
        socaas_remote_access: Literal["disable", "enable"] | None = None,
        type: Literal["fortimanager", "cloud-management", "none"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemCentralManagement", "CliGlobalSystemCentralManagementGetResponse"]
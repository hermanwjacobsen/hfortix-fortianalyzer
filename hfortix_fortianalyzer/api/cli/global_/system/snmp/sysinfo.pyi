"""Type stubs for cli.global.system.snmp.sysinfo"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSnmpSysinfoGetItem:
    """Item yielded when iterating over CliGlobalSystemSnmpSysinfoGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def contact_info(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def engine_id(self) -> str: ...
    @property
    def fortianalyzer_legacy_sysoid(self) -> Literal["disable", "enable"]: ...
    @property
    def location(self) -> str: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def trap_cpu_high_exclude_nice_threshold(self) -> int: ...
    @property
    def trap_high_cpu_threshold(self) -> int: ...
    @property
    def trap_low_memory_threshold(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemSnmpSysinfoGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemSnmpSysinfoGet endpoint with autocomplete support."""

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
    def contact_info(self) -> str | None:
        """Field: contact_info"""
        ...

    @property
    def description(self) -> str | None:
        """Field: description"""
        ...

    @property
    def engine_id(self) -> str | None:
        """Field: engine-id"""
        ...

    @property
    def fortianalyzer_legacy_sysoid(self) -> Literal["disable", "enable"] | None:
        """Field: fortianalyzer-legacy-sysoid"""
        ...

    @property
    def location(self) -> str | None:
        """Field: location"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def trap_cpu_high_exclude_nice_threshold(self) -> int | None:
        """Field: trap-cpu-high-exclude-nice-threshold"""
        ...

    @property
    def trap_high_cpu_threshold(self) -> int | None:
        """Field: trap-high-cpu-threshold"""
        ...

    @property
    def trap_low_memory_threshold(self) -> int | None:
        """Field: trap-low-memory-threshold"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemSnmpSysinfoGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemSnmpSysinfo:
    """FortiAnalyzer endpoint: cli.global.system.snmp.sysinfo"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemSnmpSysinfoGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        contact_info: str | None = None,
        description: str | None = None,
        engine_id: str | None = None,
        fortianalyzer_legacy_sysoid: Literal["disable", "enable"] | None = None,
        location: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_cpu_high_exclude_nice_threshold: int | None = None,
        trap_high_cpu_threshold: int | None = None,
        trap_low_memory_threshold: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        contact_info: str | None = None,
        description: str | None = None,
        engine_id: str | None = None,
        fortianalyzer_legacy_sysoid: Literal["disable", "enable"] | None = None,
        location: str | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_cpu_high_exclude_nice_threshold: int | None = None,
        trap_high_cpu_threshold: int | None = None,
        trap_low_memory_threshold: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemSnmpSysinfo", "CliGlobalSystemSnmpSysinfoGetResponse"]
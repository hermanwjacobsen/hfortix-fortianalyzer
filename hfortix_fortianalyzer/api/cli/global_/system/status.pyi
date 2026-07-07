"""Type stubs for cli.global.system.status"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemStatusGetItem:
    """Item yielded when iterating over CliGlobalSystemStatusGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def Admin_Domain_Configuration(self) -> str: ...
    @property
    def BIOS_version(self) -> str: ...
    @property
    def Branch_Point(self) -> str: ...
    @property
    def Current_Time(self) -> str: ...
    @property
    def Daylight_Time_Saving(self) -> str: ...
    @property
    def Disk_Usage(self) -> str: ...
    @property
    def HA_Mode(self) -> str: ...
    @property
    def Hostname(self) -> str: ...
    @property
    def License_Status(self) -> str: ...
    @property
    def Max_Number_of_Admin_Domains(self) -> str: ...
    @property
    def Max_Number_of_Device_Groups(self) -> str: ...
    @property
    def Platform_Full_Name(self) -> str: ...
    @property
    def Platform_Type(self) -> str: ...
    @property
    def Release_Version_Information(self) -> str: ...
    @property
    def Serial_Number(self) -> str: ...
    @property
    def Time_Zone(self) -> str: ...
    @property
    def Version(self) -> str: ...
    @property
    def x86_64_Applications(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemStatusGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemStatusGet endpoint with autocomplete support."""

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
    def Admin_Domain_Configuration(self) -> str | None:
        """Field: Admin Domain Configuration"""
        ...

    @property
    def BIOS_version(self) -> str | None:
        """Field: BIOS version"""
        ...

    @property
    def Branch_Point(self) -> str | None:
        """Field: Branch Point"""
        ...

    @property
    def Current_Time(self) -> str | None:
        """Field: Current Time"""
        ...

    @property
    def Daylight_Time_Saving(self) -> str | None:
        """Field: Daylight Time Saving"""
        ...

    @property
    def Disk_Usage(self) -> str | None:
        """Field: Disk Usage"""
        ...

    @property
    def HA_Mode(self) -> str | None:
        """Field: HA Mode"""
        ...

    @property
    def Hostname(self) -> str | None:
        """Field: Hostname"""
        ...

    @property
    def License_Status(self) -> str | None:
        """Field: License Status"""
        ...

    @property
    def Max_Number_of_Admin_Domains(self) -> str | None:
        """Field: Max Number of Admin Domains"""
        ...

    @property
    def Max_Number_of_Device_Groups(self) -> str | None:
        """Field: Max Number of Device Groups"""
        ...

    @property
    def Platform_Full_Name(self) -> str | None:
        """Field: Platform Full Name"""
        ...

    @property
    def Platform_Type(self) -> str | None:
        """Field: Platform Type"""
        ...

    @property
    def Release_Version_Information(self) -> str | None:
        """Field: Release Version Information"""
        ...

    @property
    def Serial_Number(self) -> str | None:
        """Field: Serial Number"""
        ...

    @property
    def Time_Zone(self) -> str | None:
        """Field: Time Zone"""
        ...

    @property
    def Version(self) -> str | None:
        """Field: Version"""
        ...

    @property
    def x86_64_Applications(self) -> str | None:
        """Field: x86-64 Applications"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemStatusGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemStatus:
    """FortiAnalyzer endpoint: cli.global.system.status"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemStatusGetResponse:
        """GET operation."""
        ...


__all__ = ["CliGlobalSystemStatus", "CliGlobalSystemStatusGetResponse"]
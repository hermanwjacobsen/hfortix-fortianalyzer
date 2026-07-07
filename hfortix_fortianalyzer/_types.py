"""Type protocols for FortiAnalyzer response objects."""

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class DeviceObject(Protocol):
    """Protocol for device objects from dvmdb.device API."""

    # Common device fields
    name: str
    sn: str
    platform_str: str
    os_ver: str
    os_type: str
    patch: int
    mr: int
    build: int
    branch_pt: int

    # Hardware info
    vm_cpu: int
    vm_mem: int
    vm_cpu_limit: int
    vm_mem_limit: int

    # Network info
    ip: str
    mgmt_mode: str
    mgmt_if: str

    # Status
    conn_status: str
    conn_mode: str
    conf_status: str
    db_status: str

    # Version info
    version: int

    # Additional fields available via __getattr__
    def __getattr__(self, name: str) -> Any: ...

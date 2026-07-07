"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ha_slave import DvmdbAdomDeviceHaSlave
    from .vdom import DvmdbAdomDeviceVdom

__all__ = ["DvmdbAdomDevice"]


from ..device_base import DvmdbAdomDevice as DvmdbAdomDeviceBase

class DvmdbAdomDevice(DvmdbAdomDeviceBase):
    """DvmdbAdomDevice endpoints."""

    ha_slave: DvmdbAdomDeviceHaSlave
    vdom: DvmdbAdomDeviceVdom

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

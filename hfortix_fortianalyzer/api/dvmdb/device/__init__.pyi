"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ha_slave import DvmdbDeviceHaSlave
    from .vdom import DvmdbDeviceVdom

__all__ = ["DvmdbDevice"]


from ..device_base import DvmdbDevice as DvmdbDeviceBase

class DvmdbDevice(DvmdbDeviceBase):
    """DvmdbDevice endpoints."""

    ha_slave: DvmdbDeviceHaSlave
    vdom: DvmdbDeviceVdom

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

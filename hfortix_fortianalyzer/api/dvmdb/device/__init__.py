"""FortiAnalyzer device API endpoints."""

from __future__ import annotations

from ..device_base import DvmdbDevice as DvmdbDeviceBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ha_slave
    from . import vdom

__all__ = ["DvmdbDevice"]


class DvmdbDevice(DvmdbDeviceBase):
    """FortiAnalyzer device API endpoints."""

    ha_slave: "ha_slave.DvmdbDeviceHaSlave"
    vdom: "vdom.DvmdbDeviceVdom"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize DvmdbDevice with endpoint methods and child modules."""
        super().__init__(client)

        from . import ha_slave as ha_slave_module
        from . import vdom as vdom_module

        self.ha_slave = ha_slave_module.DvmdbDeviceHaSlave(client)
        self.vdom = vdom_module.DvmdbDeviceVdom(client)

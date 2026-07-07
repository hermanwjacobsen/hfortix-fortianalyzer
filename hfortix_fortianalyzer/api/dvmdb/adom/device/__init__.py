"""FortiAnalyzer device adom API endpoints."""

from __future__ import annotations

from ..device_base import DvmdbAdomDevice as DvmdbAdomDeviceBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ha_slave
    from . import vdom

__all__ = ["DvmdbAdomDevice"]


class DvmdbAdomDevice(DvmdbAdomDeviceBase):
    """FortiAnalyzer device adom API endpoints."""

    ha_slave: "ha_slave.DvmdbAdomDeviceHaSlave"
    vdom: "vdom.DvmdbAdomDeviceVdom"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize DvmdbAdomDevice with endpoint methods and child modules."""
        super().__init__(client)

        from . import ha_slave as ha_slave_module
        from . import vdom as vdom_module

        self.ha_slave = ha_slave_module.DvmdbAdomDeviceHaSlave(client)
        self.vdom = vdom_module.DvmdbAdomDeviceVdom(client)

"""FortiManager device API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ha_slave
    from . import vdom

__all__ = ["Device"]


class Device:
    """FortiManager device API endpoints."""

    ha_slave: "ha_slave.DvmdbDeviceHa_slave"
    vdom: "vdom.DvmdbDeviceVdom"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Device namespace with JSON-RPC client."""
        from . import ha_slave as ha_slave_module
        from . import vdom as vdom_module

        self.ha_slave = ha_slave_module.DvmdbDeviceHa_slave(client)
        self.vdom = vdom_module.DvmdbDeviceVdom(client)

"""FortiAnalyzer sys API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import api
    from . import generate
    from . import ha
    from . import login
    from . import logout
    from . import proxy
    from . import reboot
    from . import status

__all__ = ["Sys"]


class Sys:
    """FortiAnalyzer sys API endpoints."""

    api: "api.API"
    generate: "generate.Generate"
    ha: "ha.HA"
    login: "login.Login"
    logout: "logout.SysLogout"
    proxy: "proxy.Proxy"
    reboot: "reboot.SysReboot"
    status: "status.SysStatus"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Sys namespace with JSON-RPC client."""
        from . import api as api_module
        from . import generate as generate_module
        from . import ha as ha_module
        from . import login as login_module
        from . import logout as logout_module
        from . import proxy as proxy_module
        from . import reboot as reboot_module
        from . import status as status_module

        self.api = api_module.API(client)
        self.generate = generate_module.Generate(client)
        self.ha = ha_module.HA(client)
        self.login = login_module.Login(client)
        self.logout = logout_module.SysLogout(client)
        self.proxy = proxy_module.Proxy(client)
        self.reboot = reboot_module.SysReboot(client)
        self.status = status_module.SysStatus(client)

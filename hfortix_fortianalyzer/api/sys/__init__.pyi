"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .api import API
    from .generate import Generate
    from .ha import HA
    from .login import Login
    from .logout import SysLogout
    from .proxy import Proxy
    from .reboot import SysReboot
    from .status import SysStatus

__all__ = ["Sys"]


class Sys:
    """Sys endpoints."""

    api: API
    generate: Generate
    ha: HA
    login: Login
    logout: SysLogout
    proxy: Proxy
    reboot: SysReboot
    status: SysStatus

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .community import CliGlobalSystemSnmpCommunity
    from .sysinfo import CliGlobalSystemSnmpSysinfo
    from .user import CliGlobalSystemSnmpUser

__all__ = ["SNMP"]


class SNMP:
    """SNMP endpoints."""

    community: CliGlobalSystemSnmpCommunity
    sysinfo: CliGlobalSystemSnmpSysinfo
    user: CliGlobalSystemSnmpUser

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

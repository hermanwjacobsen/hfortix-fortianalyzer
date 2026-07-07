"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ipv6 import CliGlobalSystemInterfaceIpv6
    from .member import CliGlobalSystemInterfaceMember

__all__ = ["CliGlobalSystemInterface"]


from ..interface_base import CliGlobalSystemInterface as CliGlobalSystemInterfaceBase

class CliGlobalSystemInterface(CliGlobalSystemInterfaceBase):
    """CliGlobalSystemInterface endpoints."""

    ipv6: CliGlobalSystemInterfaceIpv6
    member: CliGlobalSystemInterfaceMember

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

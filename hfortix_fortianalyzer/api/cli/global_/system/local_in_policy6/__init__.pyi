"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .dport import CliGlobalSystemLocalInPolicy6Dport
    from .dst import CliGlobalSystemLocalInPolicy6Dst
    from .intf import CliGlobalSystemLocalInPolicy6Intf
    from .src import CliGlobalSystemLocalInPolicy6Src

__all__ = ["CliGlobalSystemLocalInPolicy6"]


from ..local_in_policy6_base import CliGlobalSystemLocalInPolicy6 as CliGlobalSystemLocalInPolicy6Base

class CliGlobalSystemLocalInPolicy6(CliGlobalSystemLocalInPolicy6Base):
    """CliGlobalSystemLocalInPolicy6 endpoints."""

    dport: CliGlobalSystemLocalInPolicy6Dport
    dst: CliGlobalSystemLocalInPolicy6Dst
    intf: CliGlobalSystemLocalInPolicy6Intf
    src: CliGlobalSystemLocalInPolicy6Src

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

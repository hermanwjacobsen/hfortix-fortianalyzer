"""FortiAnalyzer local_in_policy6 system API endpoints."""

from __future__ import annotations

from ..local_in_policy6_base import CliGlobalSystemLocalInPolicy6 as CliGlobalSystemLocalInPolicy6Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import dport
    from . import dst
    from . import intf
    from . import src

__all__ = ["CliGlobalSystemLocalInPolicy6"]


class CliGlobalSystemLocalInPolicy6(CliGlobalSystemLocalInPolicy6Base):
    """FortiAnalyzer local_in_policy6 system API endpoints."""

    dport: "dport.CliGlobalSystemLocalInPolicy6Dport"
    dst: "dst.CliGlobalSystemLocalInPolicy6Dst"
    intf: "intf.CliGlobalSystemLocalInPolicy6Intf"
    src: "src.CliGlobalSystemLocalInPolicy6Src"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemLocalInPolicy6 with endpoint methods and child modules."""
        super().__init__(client)

        from . import dport as dport_module
        from . import dst as dst_module
        from . import intf as intf_module
        from . import src as src_module

        self.dport = dport_module.CliGlobalSystemLocalInPolicy6Dport(client)
        self.dst = dst_module.CliGlobalSystemLocalInPolicy6Dst(client)
        self.intf = intf_module.CliGlobalSystemLocalInPolicy6Intf(client)
        self.src = src_module.CliGlobalSystemLocalInPolicy6Src(client)

"""FortiAnalyzer local_in_policy system API endpoints."""

from __future__ import annotations

from ..local_in_policy_base import CliGlobalSystemLocalInPolicy as CliGlobalSystemLocalInPolicyBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import dport
    from . import dst
    from . import intf
    from . import src

__all__ = ["CliGlobalSystemLocalInPolicy"]


class CliGlobalSystemLocalInPolicy(CliGlobalSystemLocalInPolicyBase):
    """FortiAnalyzer local_in_policy system API endpoints."""

    dport: "dport.CliGlobalSystemLocalInPolicyDport"
    dst: "dst.CliGlobalSystemLocalInPolicyDst"
    intf: "intf.CliGlobalSystemLocalInPolicyIntf"
    src: "src.CliGlobalSystemLocalInPolicySrc"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemLocalInPolicy with endpoint methods and child modules."""
        super().__init__(client)

        from . import dport as dport_module
        from . import dst as dst_module
        from . import intf as intf_module
        from . import src as src_module

        self.dport = dport_module.CliGlobalSystemLocalInPolicyDport(client)
        self.dst = dst_module.CliGlobalSystemLocalInPolicyDst(client)
        self.intf = intf_module.CliGlobalSystemLocalInPolicyIntf(client)
        self.src = src_module.CliGlobalSystemLocalInPolicySrc(client)

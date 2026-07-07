"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .dport import CliGlobalSystemLocalInPolicyDport
    from .dst import CliGlobalSystemLocalInPolicyDst
    from .intf import CliGlobalSystemLocalInPolicyIntf
    from .src import CliGlobalSystemLocalInPolicySrc

__all__ = ["CliGlobalSystemLocalInPolicy"]


from ..local_in_policy_base import CliGlobalSystemLocalInPolicy as CliGlobalSystemLocalInPolicyBase

class CliGlobalSystemLocalInPolicy(CliGlobalSystemLocalInPolicyBase):
    """CliGlobalSystemLocalInPolicy endpoints."""

    dport: CliGlobalSystemLocalInPolicyDport
    dst: CliGlobalSystemLocalInPolicyDst
    intf: CliGlobalSystemLocalInPolicyIntf
    src: CliGlobalSystemLocalInPolicySrc

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

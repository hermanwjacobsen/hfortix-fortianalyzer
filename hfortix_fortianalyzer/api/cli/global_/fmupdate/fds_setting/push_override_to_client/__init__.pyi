"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .announce_ip import CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIp

__all__ = ["CliGlobalFmupdateFdsSettingPushOverrideToClient"]


from ..push_override_to_client_base import CliGlobalFmupdateFdsSettingPushOverrideToClient as CliGlobalFmupdateFdsSettingPushOverrideToClientBase

class CliGlobalFmupdateFdsSettingPushOverrideToClient(CliGlobalFmupdateFdsSettingPushOverrideToClientBase):
    """CliGlobalFmupdateFdsSettingPushOverrideToClient endpoints."""

    announce_ip: CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIp

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

"""FortiAnalyzer push_override_to_client fds_setting API endpoints."""

from __future__ import annotations

from ..push_override_to_client_base import CliGlobalFmupdateFdsSettingPushOverrideToClient as CliGlobalFmupdateFdsSettingPushOverrideToClientBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import announce_ip

__all__ = ["CliGlobalFmupdateFdsSettingPushOverrideToClient"]


class CliGlobalFmupdateFdsSettingPushOverrideToClient(CliGlobalFmupdateFdsSettingPushOverrideToClientBase):
    """FortiAnalyzer push_override_to_client fds_setting API endpoints."""

    announce_ip: "announce_ip.CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIp"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalFmupdateFdsSettingPushOverrideToClient with endpoint methods and child modules."""
        super().__init__(client)

        from . import announce_ip as announce_ip_module

        self.announce_ip = announce_ip_module.CliGlobalFmupdateFdsSettingPushOverrideToClientAnnounceIp(client)

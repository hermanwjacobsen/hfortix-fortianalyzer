"""FortiAnalyzer fds_setting fmupdate API endpoints."""

from __future__ import annotations

from ..fds_setting_base import CliGlobalFmupdateFdsSetting as CliGlobalFmupdateFdsSettingBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import push_override
    from . import push_override_to_client
    from . import server_override
    from . import update_schedule

__all__ = ["CliGlobalFmupdateFdsSetting"]


class CliGlobalFmupdateFdsSetting(CliGlobalFmupdateFdsSettingBase):
    """FortiAnalyzer fds_setting fmupdate API endpoints."""

    push_override: "push_override.CliGlobalFmupdateFdsSettingPushOverride"
    push_override_to_client: "push_override_to_client.CliGlobalFmupdateFdsSettingPushOverrideToClient"
    server_override: "server_override.CliGlobalFmupdateFdsSettingServerOverride"
    update_schedule: "update_schedule.CliGlobalFmupdateFdsSettingUpdateSchedule"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalFmupdateFdsSetting with endpoint methods and child modules."""
        super().__init__(client)

        from . import push_override as push_override_module
        from . import push_override_to_client as push_override_to_client_module
        from . import server_override as server_override_module
        from . import update_schedule as update_schedule_module

        self.push_override = push_override_module.CliGlobalFmupdateFdsSettingPushOverride(client)
        self.push_override_to_client = push_override_to_client_module.CliGlobalFmupdateFdsSettingPushOverrideToClient(client)
        self.server_override = server_override_module.CliGlobalFmupdateFdsSettingServerOverride(client)
        self.update_schedule = update_schedule_module.CliGlobalFmupdateFdsSettingUpdateSchedule(client)

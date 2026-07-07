"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .push_override import CliGlobalFmupdateFdsSettingPushOverride
    from .push_override_to_client import CliGlobalFmupdateFdsSettingPushOverrideToClient
    from .server_override import CliGlobalFmupdateFdsSettingServerOverride
    from .update_schedule import CliGlobalFmupdateFdsSettingUpdateSchedule

__all__ = ["CliGlobalFmupdateFdsSetting"]


from ..fds_setting_base import CliGlobalFmupdateFdsSetting as CliGlobalFmupdateFdsSettingBase

class CliGlobalFmupdateFdsSetting(CliGlobalFmupdateFdsSettingBase):
    """CliGlobalFmupdateFdsSetting endpoints."""

    push_override: CliGlobalFmupdateFdsSettingPushOverride
    push_override_to_client: CliGlobalFmupdateFdsSettingPushOverrideToClient
    server_override: CliGlobalFmupdateFdsSettingServerOverride
    update_schedule: CliGlobalFmupdateFdsSettingUpdateSchedule

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

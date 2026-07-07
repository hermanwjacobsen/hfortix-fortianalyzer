"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .upgrade_timeout import CliGlobalFmupdateFwmSettingUpgradeTimeout

__all__ = ["CliGlobalFmupdateFwmSetting"]


from ..fwm_setting_base import CliGlobalFmupdateFwmSetting as CliGlobalFmupdateFwmSettingBase

class CliGlobalFmupdateFwmSetting(CliGlobalFmupdateFwmSettingBase):
    """CliGlobalFmupdateFwmSetting endpoints."""

    upgrade_timeout: CliGlobalFmupdateFwmSettingUpgradeTimeout

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

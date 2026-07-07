"""FortiAnalyzer fwm_setting fmupdate API endpoints."""

from __future__ import annotations

from ..fwm_setting_base import CliGlobalFmupdateFwmSetting as CliGlobalFmupdateFwmSettingBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import upgrade_timeout

__all__ = ["CliGlobalFmupdateFwmSetting"]


class CliGlobalFmupdateFwmSetting(CliGlobalFmupdateFwmSettingBase):
    """FortiAnalyzer fwm_setting fmupdate API endpoints."""

    upgrade_timeout: "upgrade_timeout.CliGlobalFmupdateFwmSettingUpgradeTimeout"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalFmupdateFwmSetting with endpoint methods and child modules."""
        super().__init__(client)

        from . import upgrade_timeout as upgrade_timeout_module

        self.upgrade_timeout = upgrade_timeout_module.CliGlobalFmupdateFwmSettingUpgradeTimeout(client)

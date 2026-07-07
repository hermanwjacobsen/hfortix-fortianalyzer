"""FortiAnalyzer fgd_setting fmupdate API endpoints."""

from __future__ import annotations

from ..fgd_setting_base import CliGlobalFmupdateFgdSetting as CliGlobalFmupdateFgdSettingBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import server_override

__all__ = ["CliGlobalFmupdateFgdSetting"]


class CliGlobalFmupdateFgdSetting(CliGlobalFmupdateFgdSettingBase):
    """FortiAnalyzer fgd_setting fmupdate API endpoints."""

    server_override: "server_override.CliGlobalFmupdateFgdSettingServerOverride"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalFmupdateFgdSetting with endpoint methods and child modules."""
        super().__init__(client)

        from . import server_override as server_override_module

        self.server_override = server_override_module.CliGlobalFmupdateFgdSettingServerOverride(client)

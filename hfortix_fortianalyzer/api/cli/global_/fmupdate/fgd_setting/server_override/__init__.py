"""FortiAnalyzer server_override fgd_setting API endpoints."""

from __future__ import annotations

from ..server_override_base import CliGlobalFmupdateFgdSettingServerOverride as CliGlobalFmupdateFgdSettingServerOverrideBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import servlist

__all__ = ["CliGlobalFmupdateFgdSettingServerOverride"]


class CliGlobalFmupdateFgdSettingServerOverride(CliGlobalFmupdateFgdSettingServerOverrideBase):
    """FortiAnalyzer server_override fgd_setting API endpoints."""

    servlist: "servlist.CliGlobalFmupdateFgdSettingServerOverrideServlist"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalFmupdateFgdSettingServerOverride with endpoint methods and child modules."""
        super().__init__(client)

        from . import servlist as servlist_module

        self.servlist = servlist_module.CliGlobalFmupdateFgdSettingServerOverrideServlist(client)

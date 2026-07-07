"""FortiAnalyzer server_override fds_setting API endpoints."""

from __future__ import annotations

from ..server_override_base import CliGlobalFmupdateFdsSettingServerOverride as CliGlobalFmupdateFdsSettingServerOverrideBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import servlist

__all__ = ["CliGlobalFmupdateFdsSettingServerOverride"]


class CliGlobalFmupdateFdsSettingServerOverride(CliGlobalFmupdateFdsSettingServerOverrideBase):
    """FortiAnalyzer server_override fds_setting API endpoints."""

    servlist: "servlist.CliGlobalFmupdateFdsSettingServerOverrideServlist"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalFmupdateFdsSettingServerOverride with endpoint methods and child modules."""
        super().__init__(client)

        from . import servlist as servlist_module

        self.servlist = servlist_module.CliGlobalFmupdateFdsSettingServerOverrideServlist(client)

"""FortiAnalyzer backup system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import all_settings

__all__ = ["Backup"]


class Backup:
    """FortiAnalyzer backup system API endpoints."""

    all_settings: "all_settings.CliGlobalSystemBackupAllSettings"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Backup namespace with JSON-RPC client."""
        from . import all_settings as all_settings_module

        self.all_settings = all_settings_module.CliGlobalSystemBackupAllSettings(client)

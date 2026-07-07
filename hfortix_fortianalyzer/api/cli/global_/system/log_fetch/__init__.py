"""FortiAnalyzer log_fetch system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import client_profile
    from . import server_settings

__all__ = ["Logfetch"]


class Logfetch:
    """FortiAnalyzer log_fetch system API endpoints."""

    client_profile: "client_profile.CliGlobalSystemLogFetchClientProfile"
    server_settings: "server_settings.CliGlobalSystemLogFetchServerSettings"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Logfetch namespace with JSON-RPC client."""
        from . import client_profile as client_profile_module
        from . import server_settings as server_settings_module

        self.client_profile = client_profile_module.CliGlobalSystemLogFetchClientProfile(client)
        self.server_settings = server_settings_module.CliGlobalSystemLogFetchServerSettings(client)

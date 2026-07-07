"""FortiAnalyzer adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import enduser_avatar
    from . import forticare
    from . import lograte
    from . import storage_info_history

__all__ = ["Adom"]


class Adom:
    """FortiAnalyzer adom API endpoints."""

    enduser_avatar: "enduser_avatar.FazsysAdomEnduserAvatar"
    forticare: "forticare.Forticare"
    lograte: "lograte.Lograte"
    storage_info_history: "storage_info_history.FazsysAdomStorageInfoHistory"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Adom namespace with JSON-RPC client."""
        from . import enduser_avatar as enduser_avatar_module
        from . import forticare as forticare_module
        from . import lograte as lograte_module
        from . import storage_info_history as storage_info_history_module

        self.enduser_avatar = enduser_avatar_module.FazsysAdomEnduserAvatar(client)
        self.forticare = forticare_module.Forticare(client)
        self.lograte = lograte_module.Lograte(client)
        self.storage_info_history = storage_info_history_module.FazsysAdomStorageInfoHistory(client)

"""FortiAnalyzer login API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import challenge
    from . import user

__all__ = ["Login"]


class Login:
    """FortiAnalyzer login API endpoints."""

    challenge: "challenge.SysLoginChallenge"
    user: "user.SysLoginUser"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Login namespace with JSON-RPC client."""
        from . import challenge as challenge_module
        from . import user as user_module

        self.challenge = challenge_module.SysLoginChallenge(client)
        self.user = user_module.SysLoginUser(client)

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .challenge import SysLoginChallenge
    from .user import SysLoginUser

__all__ = ["Login"]


class Login:
    """Login endpoints."""

    challenge: SysLoginChallenge
    user: SysLoginUser

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

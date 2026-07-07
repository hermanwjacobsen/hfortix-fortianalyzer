"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .enduser_avatar import FazsysAdomEnduserAvatar
    from .forticare import Forticare
    from .lograte import Lograte
    from .storage_info_history import FazsysAdomStorageInfoHistory

__all__ = ["Adom"]


class Adom:
    """Adom endpoints."""

    enduser_avatar: FazsysAdomEnduserAvatar
    forticare: Forticare
    lograte: Lograte
    storage_info_history: FazsysAdomStorageInfoHistory

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

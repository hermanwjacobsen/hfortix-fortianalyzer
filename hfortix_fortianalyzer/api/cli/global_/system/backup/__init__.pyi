"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .all_settings import CliGlobalSystemBackupAllSettings

__all__ = ["Backup"]


class Backup:
    """Backup endpoints."""

    all_settings: CliGlobalSystemBackupAllSettings

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

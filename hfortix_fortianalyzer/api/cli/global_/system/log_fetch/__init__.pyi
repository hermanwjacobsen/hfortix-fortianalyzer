"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .client_profile import CliGlobalSystemLogFetchClientProfile
    from .server_settings import CliGlobalSystemLogFetchServerSettings

__all__ = ["Logfetch"]


class Logfetch:
    """Logfetch endpoints."""

    client_profile: CliGlobalSystemLogFetchClientProfile
    server_settings: CliGlobalSystemLogFetchServerSettings

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

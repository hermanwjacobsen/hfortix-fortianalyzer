"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ssl_cipher_suites import CliGlobalSystemGlobalSslCipherSuites

__all__ = ["CliGlobalSystemGlobal"]


from ..global_base import CliGlobalSystemGlobal as CliGlobalSystemGlobalBase

class CliGlobalSystemGlobal(CliGlobalSystemGlobalBase):
    """CliGlobalSystemGlobal endpoints."""

    ssl_cipher_suites: CliGlobalSystemGlobalSslCipherSuites

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

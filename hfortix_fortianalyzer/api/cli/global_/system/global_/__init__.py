"""FortiAnalyzer global_ system API endpoints."""

from __future__ import annotations

from ..global_base import CliGlobalSystemGlobal as CliGlobalSystemGlobalBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ssl_cipher_suites

__all__ = ["CliGlobalSystemGlobal"]


class CliGlobalSystemGlobal(CliGlobalSystemGlobalBase):
    """FortiAnalyzer global_ system API endpoints."""

    ssl_cipher_suites: "ssl_cipher_suites.CliGlobalSystemGlobalSslCipherSuites"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemGlobal with endpoint methods and child modules."""
        super().__init__(client)

        from . import ssl_cipher_suites as ssl_cipher_suites_module

        self.ssl_cipher_suites = ssl_cipher_suites_module.CliGlobalSystemGlobalSslCipherSuites(client)

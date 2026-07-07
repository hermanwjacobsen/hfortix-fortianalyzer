"""FortiAnalyzer client_cert_auth settings API endpoints."""

from __future__ import annotations

from ..client_cert_auth_base import CliGlobalSystemLogSettingsClientCertAuth as CliGlobalSystemLogSettingsClientCertAuthBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import trusted_client

__all__ = ["CliGlobalSystemLogSettingsClientCertAuth"]


class CliGlobalSystemLogSettingsClientCertAuth(CliGlobalSystemLogSettingsClientCertAuthBase):
    """FortiAnalyzer client_cert_auth settings API endpoints."""

    trusted_client: "trusted_client.CliGlobalSystemLogSettingsClientCertAuthTrustedClient"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemLogSettingsClientCertAuth with endpoint methods and child modules."""
        super().__init__(client)

        from . import trusted_client as trusted_client_module

        self.trusted_client = trusted_client_module.CliGlobalSystemLogSettingsClientCertAuthTrustedClient(client)

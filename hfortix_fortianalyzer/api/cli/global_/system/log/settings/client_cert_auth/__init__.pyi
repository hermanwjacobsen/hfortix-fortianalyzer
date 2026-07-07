"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .trusted_client import CliGlobalSystemLogSettingsClientCertAuthTrustedClient

__all__ = ["CliGlobalSystemLogSettingsClientCertAuth"]


from ..client_cert_auth_base import CliGlobalSystemLogSettingsClientCertAuth as CliGlobalSystemLogSettingsClientCertAuthBase

class CliGlobalSystemLogSettingsClientCertAuth(CliGlobalSystemLogSettingsClientCertAuthBase):
    """CliGlobalSystemLogSettingsClientCertAuth endpoints."""

    trusted_client: CliGlobalSystemLogSettingsClientCertAuthTrustedClient

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

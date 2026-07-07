"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .client_cert_auth import CliGlobalSystemLogSettingsClientCertAuth
    from .rolling_analyzer import CliGlobalSystemLogSettingsRollingAnalyzer
    from .rolling_local import CliGlobalSystemLogSettingsRollingLocal
    from .rolling_regular import CliGlobalSystemLogSettingsRollingRegular

__all__ = ["CliGlobalSystemLogSettings"]


from ..settings_base import CliGlobalSystemLogSettings as CliGlobalSystemLogSettingsBase

class CliGlobalSystemLogSettings(CliGlobalSystemLogSettingsBase):
    """CliGlobalSystemLogSettings endpoints."""

    client_cert_auth: CliGlobalSystemLogSettingsClientCertAuth
    rolling_analyzer: CliGlobalSystemLogSettingsRollingAnalyzer
    rolling_local: CliGlobalSystemLogSettingsRollingLocal
    rolling_regular: CliGlobalSystemLogSettingsRollingRegular

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

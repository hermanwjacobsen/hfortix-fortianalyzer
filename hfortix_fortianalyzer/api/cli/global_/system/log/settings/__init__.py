"""FortiAnalyzer settings log API endpoints."""

from __future__ import annotations

from ..settings_base import CliGlobalSystemLogSettings as CliGlobalSystemLogSettingsBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import client_cert_auth
    from . import rolling_analyzer
    from . import rolling_local
    from . import rolling_regular

__all__ = ["CliGlobalSystemLogSettings"]


class CliGlobalSystemLogSettings(CliGlobalSystemLogSettingsBase):
    """FortiAnalyzer settings log API endpoints."""

    client_cert_auth: "client_cert_auth.CliGlobalSystemLogSettingsClientCertAuth"
    rolling_analyzer: "rolling_analyzer.CliGlobalSystemLogSettingsRollingAnalyzer"
    rolling_local: "rolling_local.CliGlobalSystemLogSettingsRollingLocal"
    rolling_regular: "rolling_regular.CliGlobalSystemLogSettingsRollingRegular"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemLogSettings with endpoint methods and child modules."""
        super().__init__(client)

        from . import client_cert_auth as client_cert_auth_module
        from . import rolling_analyzer as rolling_analyzer_module
        from . import rolling_local as rolling_local_module
        from . import rolling_regular as rolling_regular_module

        self.client_cert_auth = client_cert_auth_module.CliGlobalSystemLogSettingsClientCertAuth(client)
        self.rolling_analyzer = rolling_analyzer_module.CliGlobalSystemLogSettingsRollingAnalyzer(client)
        self.rolling_local = rolling_local_module.CliGlobalSystemLogSettingsRollingLocal(client)
        self.rolling_regular = rolling_regular_module.CliGlobalSystemLogSettingsRollingRegular(client)

"""FortiAnalyzer config adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import basic_handler
    from . import correlation_handler
    from . import data_selector
    from . import notification_profile

__all__ = ["Config"]


class Config:
    """FortiAnalyzer config adom API endpoints."""

    basic_handler: "basic_handler.EventmgmtAdomConfigBasicHandler"
    correlation_handler: "correlation_handler.EventmgmtAdomConfigCorrelationHandler"
    data_selector: "data_selector.EventmgmtAdomConfigDataSelector"
    notification_profile: "notification_profile.EventmgmtAdomConfigNotificationProfile"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Config namespace with JSON-RPC client."""
        from . import basic_handler as basic_handler_module
        from . import correlation_handler as correlation_handler_module
        from . import data_selector as data_selector_module
        from . import notification_profile as notification_profile_module

        self.basic_handler = basic_handler_module.EventmgmtAdomConfigBasicHandler(client)
        self.correlation_handler = correlation_handler_module.EventmgmtAdomConfigCorrelationHandler(client)
        self.data_selector = data_selector_module.EventmgmtAdomConfigDataSelector(client)
        self.notification_profile = notification_profile_module.EventmgmtAdomConfigNotificationProfile(client)

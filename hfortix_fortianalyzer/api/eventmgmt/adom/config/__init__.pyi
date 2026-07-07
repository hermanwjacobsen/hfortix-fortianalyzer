"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .basic_handler import EventmgmtAdomConfigBasicHandler
    from .correlation_handler import EventmgmtAdomConfigCorrelationHandler
    from .data_selector import EventmgmtAdomConfigDataSelector
    from .notification_profile import EventmgmtAdomConfigNotificationProfile

__all__ = ["Config"]


class Config:
    """Config endpoints."""

    basic_handler: EventmgmtAdomConfigBasicHandler
    correlation_handler: EventmgmtAdomConfigCorrelationHandler
    data_selector: EventmgmtAdomConfigDataSelector
    notification_profile: EventmgmtAdomConfigNotificationProfile

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

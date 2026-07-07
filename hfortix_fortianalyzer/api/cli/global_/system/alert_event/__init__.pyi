"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .alert_destination import CliGlobalSystemAlertEventAlertDestination

__all__ = ["CliGlobalSystemAlertEvent"]


from ..alert_event_base import CliGlobalSystemAlertEvent as CliGlobalSystemAlertEventBase

class CliGlobalSystemAlertEvent(CliGlobalSystemAlertEventBase):
    """CliGlobalSystemAlertEvent endpoints."""

    alert_destination: CliGlobalSystemAlertEventAlertDestination

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

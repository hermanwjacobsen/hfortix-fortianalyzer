"""FortiAnalyzer alert_event system API endpoints."""

from __future__ import annotations

from ..alert_event_base import CliGlobalSystemAlertEvent as CliGlobalSystemAlertEventBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import alert_destination

__all__ = ["CliGlobalSystemAlertEvent"]


class CliGlobalSystemAlertEvent(CliGlobalSystemAlertEventBase):
    """FortiAnalyzer alert_event system API endpoints."""

    alert_destination: "alert_destination.CliGlobalSystemAlertEventAlertDestination"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemAlertEvent with endpoint methods and child modules."""
        super().__init__(client)

        from . import alert_destination as alert_destination_module

        self.alert_destination = alert_destination_module.CliGlobalSystemAlertEventAlertDestination(client)

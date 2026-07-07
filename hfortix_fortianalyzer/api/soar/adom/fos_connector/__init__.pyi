"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .automation_rules import SoarAdomFosConnectorAutomationRules

__all__ = ["Fosconnector"]


class Fosconnector:
    """Fosconnector endpoints."""

    automation_rules: SoarAdomFosConnectorAutomationRules

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

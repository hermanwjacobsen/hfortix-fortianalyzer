"""FortiAnalyzer fos_connector adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import automation_rules

__all__ = ["Fosconnector"]


class Fosconnector:
    """FortiAnalyzer fos_connector adom API endpoints."""

    automation_rules: "automation_rules.SoarAdomFosConnectorAutomationRules"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Fosconnector namespace with JSON-RPC client."""
        from . import automation_rules as automation_rules_module

        self.automation_rules = automation_rules_module.SoarAdomFosConnectorAutomationRules(client)

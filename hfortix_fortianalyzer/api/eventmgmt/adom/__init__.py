"""FortiAnalyzer adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import alert_incident
    from . import alertfilter
    from . import alertlogs
    from . import alerts
    from . import basic_handlers
    from . import config
    from . import correlation_handlers
    from . import mitre_attack_matrix

__all__ = ["Adom"]


class Adom:
    """FortiAnalyzer adom API endpoints."""

    alert_incident: "alert_incident.Alertincident"
    alertfilter: "alertfilter.EventmgmtAdomAlertfilter"
    alertlogs: "alertlogs.EventmgmtAdomAlertlogs"
    alerts: "alerts.EventmgmtAdomAlerts"
    basic_handlers: "basic_handlers.Basichandlers"
    config: "config.Config"
    correlation_handlers: "correlation_handlers.Correlationhandlers"
    mitre_attack_matrix: "mitre_attack_matrix.EventmgmtAdomMitreAttackMatrix"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Adom namespace with JSON-RPC client."""
        from . import alert_incident as alert_incident_module
        from . import alertfilter as alertfilter_module
        from . import alertlogs as alertlogs_module
        from . import alerts as alerts_module
        from . import basic_handlers as basic_handlers_module
        from . import config as config_module
        from . import correlation_handlers as correlation_handlers_module
        from . import mitre_attack_matrix as mitre_attack_matrix_module

        self.alert_incident = alert_incident_module.Alertincident(client)
        self.alertfilter = alertfilter_module.EventmgmtAdomAlertfilter(client)
        self.alertlogs = alertlogs_module.EventmgmtAdomAlertlogs(client)
        self.alerts = alerts_module.EventmgmtAdomAlerts(client)
        self.basic_handlers = basic_handlers_module.Basichandlers(client)
        self.config = config_module.Config(client)
        self.correlation_handlers = correlation_handlers_module.Correlationhandlers(client)
        self.mitre_attack_matrix = mitre_attack_matrix_module.EventmgmtAdomMitreAttackMatrix(client)

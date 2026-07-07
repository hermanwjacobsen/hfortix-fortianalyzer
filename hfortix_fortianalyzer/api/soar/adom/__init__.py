"""FortiAnalyzer adom API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import alert
    from . import config
    from . import fos_connector
    from . import incident
    from . import indicator
    from . import playbook
    from . import subnet
    from . import task

__all__ = ["Adom"]


class Adom:
    """FortiAnalyzer adom API endpoints."""

    alert: "alert.Alert"
    config: "config.Config"
    fos_connector: "fos_connector.Fosconnector"
    incident: "incident.Incident"
    indicator: "indicator.SoarAdomIndicator"
    playbook: "playbook.Playbook"
    subnet: "subnet.Subnet"
    task: "task.Task"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Adom namespace with JSON-RPC client."""
        from . import alert as alert_module
        from . import config as config_module
        from . import fos_connector as fos_connector_module
        from . import incident as incident_module
        from . import indicator as indicator_module
        from . import playbook as playbook_module
        from . import subnet as subnet_module
        from . import task as task_module

        self.alert = alert_module.Alert(client)
        self.config = config_module.Config(client)
        self.fos_connector = fos_connector_module.Fosconnector(client)
        self.incident = incident_module.Incident(client)
        self.indicator = indicator_module.SoarAdomIndicator(client)
        self.playbook = playbook_module.Playbook(client)
        self.subnet = subnet_module.Subnet(client)
        self.task = task_module.Task(client)

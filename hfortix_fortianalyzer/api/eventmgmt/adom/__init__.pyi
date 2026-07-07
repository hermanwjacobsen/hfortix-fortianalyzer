"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .alert_incident import Alertincident
    from .alertfilter import EventmgmtAdomAlertfilter
    from .alertlogs import EventmgmtAdomAlertlogs
    from .alerts import EventmgmtAdomAlerts
    from .basic_handlers import Basichandlers
    from .config import Config
    from .correlation_handlers import Correlationhandlers
    from .mitre_attack_matrix import EventmgmtAdomMitreAttackMatrix

__all__ = ["Adom"]


class Adom:
    """Adom endpoints."""

    alert_incident: Alertincident
    alertfilter: EventmgmtAdomAlertfilter
    alertlogs: EventmgmtAdomAlertlogs
    alerts: EventmgmtAdomAlerts
    basic_handlers: Basichandlers
    config: Config
    correlation_handlers: Correlationhandlers
    mitre_attack_matrix: EventmgmtAdomMitreAttackMatrix

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

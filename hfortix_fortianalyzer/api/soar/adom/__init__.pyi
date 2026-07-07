"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .alert import Alert
    from .config import Config
    from .fos_connector import Fosconnector
    from .incident import Incident
    from .indicator import SoarAdomIndicator
    from .playbook import Playbook
    from .subnet import Subnet
    from .task import Task

__all__ = ["Adom"]


class Adom:
    """Adom endpoints."""

    alert: Alert
    config: Config
    fos_connector: Fosconnector
    incident: Incident
    indicator: SoarAdomIndicator
    playbook: Playbook
    subnet: Subnet
    task: Task

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

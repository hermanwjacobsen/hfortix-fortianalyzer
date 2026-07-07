"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .cli import Cli
    from .dvm import Dvm
    from .dvmdb import Dvmdb
    from .eventmgmt import Eventmgmt
    from .fazsys import Fazsys
    from .fortiview import Fortiview
    from .incidentmgmt import Incidentmgmt
    from .ioc import Ioc
    from .logview import Logview
    from .report import Report
    from .soar import Soar
    from .sql_report import Sqlreport
    from .sys import Sys
    from .task import Task
    from .um import UM

__all__ = ["API"]


class API:
    """API endpoints."""

    cli: Cli
    dvm: Dvm
    dvmdb: Dvmdb
    eventmgmt: Eventmgmt
    fazsys: Fazsys
    fortiview: Fortiview
    incidentmgmt: Incidentmgmt
    ioc: Ioc
    logview: Logview
    report: Report
    soar: Soar
    sql_report: Sqlreport
    sys: Sys
    task: Task
    um: UM

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

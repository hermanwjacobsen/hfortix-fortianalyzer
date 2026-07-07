"""API endpoint modules."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import cli
    from . import dvm
    from . import dvmdb
    from . import eventmgmt
    from . import fazsys
    from . import fortiview
    from . import incidentmgmt
    from . import ioc
    from . import logview
    from . import report
    from . import soar
    from . import sql_report
    from . import sys
    from . import task
    from . import um

__all__ = ["API"]


class API:
    """
    FortiAnalyzer JSON-RPC API Interface.
    
    Organizes all FortiAnalyzer API endpoints into logical categories.
    """

    cli: "cli.Cli"
    dvm: "dvm.Dvm"
    dvmdb: "dvmdb.Dvmdb"
    eventmgmt: "eventmgmt.Eventmgmt"
    fazsys: "fazsys.Fazsys"
    fortiview: "fortiview.Fortiview"
    incidentmgmt: "incidentmgmt.Incidentmgmt"
    ioc: "ioc.Ioc"
    logview: "logview.Logview"
    report: "report.Report"
    soar: "soar.Soar"
    sql_report: "sql_report.Sqlreport"
    sys: "sys.Sys"
    task: "task.Task"
    um: "um.UM"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize API namespace with JSON-RPC client."""
        from . import cli as cli_module
        from . import dvm as dvm_module
        from . import dvmdb as dvmdb_module
        from . import eventmgmt as eventmgmt_module
        from . import fazsys as fazsys_module
        from . import fortiview as fortiview_module
        from . import incidentmgmt as incidentmgmt_module
        from . import ioc as ioc_module
        from . import logview as logview_module
        from . import report as report_module
        from . import soar as soar_module
        from . import sql_report as sql_report_module
        from . import sys as sys_module
        from . import task as task_module
        from . import um as um_module

        self.cli = cli_module.Cli(client)
        self.dvm = dvm_module.Dvm(client)
        self.dvmdb = dvmdb_module.Dvmdb(client)
        self.eventmgmt = eventmgmt_module.Eventmgmt(client)
        self.fazsys = fazsys_module.Fazsys(client)
        self.fortiview = fortiview_module.Fortiview(client)
        self.incidentmgmt = incidentmgmt_module.Incidentmgmt(client)
        self.ioc = ioc_module.Ioc(client)
        self.logview = logview_module.Logview(client)
        self.report = report_module.Report(client)
        self.soar = soar_module.Soar(client)
        self.sql_report = sql_report_module.Sqlreport(client)
        self.sys = sys_module.Sys(client)
        self.task = task_module.Task(client)
        self.um = um_module.UM(client)

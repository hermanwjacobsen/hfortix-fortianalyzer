"""FortiAnalyzer system global_ API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import admin
    from . import alert_console
    from . import alert_event
    from . import alertemail
    from . import auto_delete
    from . import backup
    from . import central_management
    from . import certificate
    from . import connector
    from . import csf
    from . import dns
    from . import fips
    from . import fortiview
    from . import global_
    from . import ha
    from . import interface
    from . import local_in_policy
    from . import local_in_policy6
    from . import locallog
    from . import log
    from . import log_fetch
    from . import log_forward
    from . import log_forward_service
    from . import mail
    from . import metadata
    from . import ntp
    from . import password_policy
    from . import performance
    from . import report
    from . import route
    from . import route6
    from . import saml
    from . import sniffer
    from . import snmp
    from . import soc_fabric
    from . import sql
    from . import status
    from . import syslog
    from . import web_proxy
    from . import workflow

__all__ = ["System"]


class System:
    """FortiAnalyzer system global_ API endpoints."""

    admin: "admin.Admin"
    alert_console: "alert_console.CliGlobalSystemAlertConsole"
    alert_event: "alert_event.CliGlobalSystemAlertEvent"
    alertemail: "alertemail.CliGlobalSystemAlertemail"
    auto_delete: "auto_delete.CliGlobalSystemAutoDelete"
    backup: "backup.Backup"
    central_management: "central_management.CliGlobalSystemCentralManagement"
    certificate: "certificate.Certificate"
    connector: "connector.CliGlobalSystemConnector"
    csf: "csf.CliGlobalSystemCsf"
    dns: "dns.CliGlobalSystemDns"
    fips: "fips.CliGlobalSystemFips"
    fortiview: "fortiview.Fortiview"
    global_: "global_.CliGlobalSystemGlobal"
    ha: "ha.CliGlobalSystemHa"
    interface: "interface.CliGlobalSystemInterface"
    local_in_policy: "local_in_policy.CliGlobalSystemLocalInPolicy"
    local_in_policy6: "local_in_policy6.CliGlobalSystemLocalInPolicy6"
    locallog: "locallog.Locallog"
    log: "log.Log"
    log_fetch: "log_fetch.Logfetch"
    log_forward: "log_forward.CliGlobalSystemLogForward"
    log_forward_service: "log_forward_service.CliGlobalSystemLogForwardService"
    mail: "mail.CliGlobalSystemMail"
    metadata: "metadata.Metadata"
    ntp: "ntp.CliGlobalSystemNtp"
    password_policy: "password_policy.CliGlobalSystemPasswordPolicy"
    performance: "performance.CliGlobalSystemPerformance"
    report: "report.Report"
    route: "route.CliGlobalSystemRoute"
    route6: "route6.CliGlobalSystemRoute6"
    saml: "saml.CliGlobalSystemSaml"
    sniffer: "sniffer.CliGlobalSystemSniffer"
    snmp: "snmp.SNMP"
    soc_fabric: "soc_fabric.CliGlobalSystemSocFabric"
    sql: "sql.CliGlobalSystemSql"
    status: "status.CliGlobalSystemStatus"
    syslog: "syslog.CliGlobalSystemSyslog"
    web_proxy: "web_proxy.CliGlobalSystemWebProxy"
    workflow: "workflow.Workflow"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize System namespace with JSON-RPC client."""
        from . import admin as admin_module
        from . import alert_console as alert_console_module
        from . import alert_event as alert_event_module
        from . import alertemail as alertemail_module
        from . import auto_delete as auto_delete_module
        from . import backup as backup_module
        from . import central_management as central_management_module
        from . import certificate as certificate_module
        from . import connector as connector_module
        from . import csf as csf_module
        from . import dns as dns_module
        from . import fips as fips_module
        from . import fortiview as fortiview_module
        from . import global_ as global__module
        from . import ha as ha_module
        from . import interface as interface_module
        from . import local_in_policy as local_in_policy_module
        from . import local_in_policy6 as local_in_policy6_module
        from . import locallog as locallog_module
        from . import log as log_module
        from . import log_fetch as log_fetch_module
        from . import log_forward as log_forward_module
        from . import log_forward_service as log_forward_service_module
        from . import mail as mail_module
        from . import metadata as metadata_module
        from . import ntp as ntp_module
        from . import password_policy as password_policy_module
        from . import performance as performance_module
        from . import report as report_module
        from . import route as route_module
        from . import route6 as route6_module
        from . import saml as saml_module
        from . import sniffer as sniffer_module
        from . import snmp as snmp_module
        from . import soc_fabric as soc_fabric_module
        from . import sql as sql_module
        from . import status as status_module
        from . import syslog as syslog_module
        from . import web_proxy as web_proxy_module
        from . import workflow as workflow_module

        self.admin = admin_module.Admin(client)
        self.alert_console = alert_console_module.CliGlobalSystemAlertConsole(client)
        self.alert_event = alert_event_module.CliGlobalSystemAlertEvent(client)
        self.alertemail = alertemail_module.CliGlobalSystemAlertemail(client)
        self.auto_delete = auto_delete_module.CliGlobalSystemAutoDelete(client)
        self.backup = backup_module.Backup(client)
        self.central_management = central_management_module.CliGlobalSystemCentralManagement(client)
        self.certificate = certificate_module.Certificate(client)
        self.connector = connector_module.CliGlobalSystemConnector(client)
        self.csf = csf_module.CliGlobalSystemCsf(client)
        self.dns = dns_module.CliGlobalSystemDns(client)
        self.fips = fips_module.CliGlobalSystemFips(client)
        self.fortiview = fortiview_module.Fortiview(client)
        self.global_ = global__module.CliGlobalSystemGlobal(client)
        self.ha = ha_module.CliGlobalSystemHa(client)
        self.interface = interface_module.CliGlobalSystemInterface(client)
        self.local_in_policy = local_in_policy_module.CliGlobalSystemLocalInPolicy(client)
        self.local_in_policy6 = local_in_policy6_module.CliGlobalSystemLocalInPolicy6(client)
        self.locallog = locallog_module.Locallog(client)
        self.log = log_module.Log(client)
        self.log_fetch = log_fetch_module.Logfetch(client)
        self.log_forward = log_forward_module.CliGlobalSystemLogForward(client)
        self.log_forward_service = log_forward_service_module.CliGlobalSystemLogForwardService(client)
        self.mail = mail_module.CliGlobalSystemMail(client)
        self.metadata = metadata_module.Metadata(client)
        self.ntp = ntp_module.CliGlobalSystemNtp(client)
        self.password_policy = password_policy_module.CliGlobalSystemPasswordPolicy(client)
        self.performance = performance_module.CliGlobalSystemPerformance(client)
        self.report = report_module.Report(client)
        self.route = route_module.CliGlobalSystemRoute(client)
        self.route6 = route6_module.CliGlobalSystemRoute6(client)
        self.saml = saml_module.CliGlobalSystemSaml(client)
        self.sniffer = sniffer_module.CliGlobalSystemSniffer(client)
        self.snmp = snmp_module.SNMP(client)
        self.soc_fabric = soc_fabric_module.CliGlobalSystemSocFabric(client)
        self.sql = sql_module.CliGlobalSystemSql(client)
        self.status = status_module.CliGlobalSystemStatus(client)
        self.syslog = syslog_module.CliGlobalSystemSyslog(client)
        self.web_proxy = web_proxy_module.CliGlobalSystemWebProxy(client)
        self.workflow = workflow_module.Workflow(client)

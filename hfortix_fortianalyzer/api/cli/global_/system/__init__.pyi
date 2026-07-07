"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .admin import Admin
    from .alert_console import CliGlobalSystemAlertConsole
    from .alert_event import CliGlobalSystemAlertEvent
    from .alertemail import CliGlobalSystemAlertemail
    from .auto_delete import CliGlobalSystemAutoDelete
    from .backup import Backup
    from .central_management import CliGlobalSystemCentralManagement
    from .certificate import Certificate
    from .connector import CliGlobalSystemConnector
    from .csf import CliGlobalSystemCsf
    from .dns import CliGlobalSystemDns
    from .fips import CliGlobalSystemFips
    from .fortiview import Fortiview
    from .global_ import CliGlobalSystemGlobal
    from .ha import CliGlobalSystemHa
    from .interface import CliGlobalSystemInterface
    from .local_in_policy import CliGlobalSystemLocalInPolicy
    from .local_in_policy6 import CliGlobalSystemLocalInPolicy6
    from .locallog import Locallog
    from .log import Log
    from .log_fetch import Logfetch
    from .log_forward import CliGlobalSystemLogForward
    from .log_forward_service import CliGlobalSystemLogForwardService
    from .mail import CliGlobalSystemMail
    from .metadata import Metadata
    from .ntp import CliGlobalSystemNtp
    from .password_policy import CliGlobalSystemPasswordPolicy
    from .performance import CliGlobalSystemPerformance
    from .report import Report
    from .route import CliGlobalSystemRoute
    from .route6 import CliGlobalSystemRoute6
    from .saml import CliGlobalSystemSaml
    from .sniffer import CliGlobalSystemSniffer
    from .snmp import SNMP
    from .soc_fabric import CliGlobalSystemSocFabric
    from .sql import CliGlobalSystemSql
    from .status import CliGlobalSystemStatus
    from .syslog import CliGlobalSystemSyslog
    from .web_proxy import CliGlobalSystemWebProxy
    from .workflow import Workflow

__all__ = ["System"]


class System:
    """System endpoints."""

    admin: Admin
    alert_console: CliGlobalSystemAlertConsole
    alert_event: CliGlobalSystemAlertEvent
    alertemail: CliGlobalSystemAlertemail
    auto_delete: CliGlobalSystemAutoDelete
    backup: Backup
    central_management: CliGlobalSystemCentralManagement
    certificate: Certificate
    connector: CliGlobalSystemConnector
    csf: CliGlobalSystemCsf
    dns: CliGlobalSystemDns
    fips: CliGlobalSystemFips
    fortiview: Fortiview
    global_: CliGlobalSystemGlobal
    ha: CliGlobalSystemHa
    interface: CliGlobalSystemInterface
    local_in_policy: CliGlobalSystemLocalInPolicy
    local_in_policy6: CliGlobalSystemLocalInPolicy6
    locallog: Locallog
    log: Log
    log_fetch: Logfetch
    log_forward: CliGlobalSystemLogForward
    log_forward_service: CliGlobalSystemLogForwardService
    mail: CliGlobalSystemMail
    metadata: Metadata
    ntp: CliGlobalSystemNtp
    password_policy: CliGlobalSystemPasswordPolicy
    performance: CliGlobalSystemPerformance
    report: Report
    route: CliGlobalSystemRoute
    route6: CliGlobalSystemRoute6
    saml: CliGlobalSystemSaml
    sniffer: CliGlobalSystemSniffer
    snmp: SNMP
    soc_fabric: CliGlobalSystemSocFabric
    sql: CliGlobalSystemSql
    status: CliGlobalSystemStatus
    syslog: CliGlobalSystemSyslog
    web_proxy: CliGlobalSystemWebProxy
    workflow: Workflow

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

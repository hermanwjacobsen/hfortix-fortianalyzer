"""FortiAnalyzer log system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import alert
    from . import api_ratelimit
    from . import device_selector
    from . import fos_policy_stats
    from . import interface_stats
    from . import ioc
    from . import mail_domain
    from . import pcap_file
    from . import ratelimit
    from . import settings
    from . import topology
    from . import ueba

__all__ = ["Log"]


class Log:
    """FortiAnalyzer log system API endpoints."""

    alert: "alert.CliGlobalSystemLogAlert"
    api_ratelimit: "api_ratelimit.CliGlobalSystemLogApiRatelimit"
    device_selector: "device_selector.CliGlobalSystemLogDeviceSelector"
    fos_policy_stats: "fos_policy_stats.CliGlobalSystemLogFosPolicyStats"
    interface_stats: "interface_stats.CliGlobalSystemLogInterfaceStats"
    ioc: "ioc.CliGlobalSystemLogIoc"
    mail_domain: "mail_domain.CliGlobalSystemLogMailDomain"
    pcap_file: "pcap_file.CliGlobalSystemLogPcapFile"
    ratelimit: "ratelimit.CliGlobalSystemLogRatelimit"
    settings: "settings.CliGlobalSystemLogSettings"
    topology: "topology.CliGlobalSystemLogTopology"
    ueba: "ueba.CliGlobalSystemLogUeba"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Log namespace with JSON-RPC client."""
        from . import alert as alert_module
        from . import api_ratelimit as api_ratelimit_module
        from . import device_selector as device_selector_module
        from . import fos_policy_stats as fos_policy_stats_module
        from . import interface_stats as interface_stats_module
        from . import ioc as ioc_module
        from . import mail_domain as mail_domain_module
        from . import pcap_file as pcap_file_module
        from . import ratelimit as ratelimit_module
        from . import settings as settings_module
        from . import topology as topology_module
        from . import ueba as ueba_module

        self.alert = alert_module.CliGlobalSystemLogAlert(client)
        self.api_ratelimit = api_ratelimit_module.CliGlobalSystemLogApiRatelimit(client)
        self.device_selector = device_selector_module.CliGlobalSystemLogDeviceSelector(client)
        self.fos_policy_stats = fos_policy_stats_module.CliGlobalSystemLogFosPolicyStats(client)
        self.interface_stats = interface_stats_module.CliGlobalSystemLogInterfaceStats(client)
        self.ioc = ioc_module.CliGlobalSystemLogIoc(client)
        self.mail_domain = mail_domain_module.CliGlobalSystemLogMailDomain(client)
        self.pcap_file = pcap_file_module.CliGlobalSystemLogPcapFile(client)
        self.ratelimit = ratelimit_module.CliGlobalSystemLogRatelimit(client)
        self.settings = settings_module.CliGlobalSystemLogSettings(client)
        self.topology = topology_module.CliGlobalSystemLogTopology(client)
        self.ueba = ueba_module.CliGlobalSystemLogUeba(client)

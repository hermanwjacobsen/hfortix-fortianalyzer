"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .alert import CliGlobalSystemLogAlert
    from .api_ratelimit import CliGlobalSystemLogApiRatelimit
    from .device_selector import CliGlobalSystemLogDeviceSelector
    from .fos_policy_stats import CliGlobalSystemLogFosPolicyStats
    from .interface_stats import CliGlobalSystemLogInterfaceStats
    from .ioc import CliGlobalSystemLogIoc
    from .mail_domain import CliGlobalSystemLogMailDomain
    from .pcap_file import CliGlobalSystemLogPcapFile
    from .ratelimit import CliGlobalSystemLogRatelimit
    from .settings import CliGlobalSystemLogSettings
    from .topology import CliGlobalSystemLogTopology
    from .ueba import CliGlobalSystemLogUeba

__all__ = ["Log"]


class Log:
    """Log endpoints."""

    alert: CliGlobalSystemLogAlert
    api_ratelimit: CliGlobalSystemLogApiRatelimit
    device_selector: CliGlobalSystemLogDeviceSelector
    fos_policy_stats: CliGlobalSystemLogFosPolicyStats
    interface_stats: CliGlobalSystemLogInterfaceStats
    ioc: CliGlobalSystemLogIoc
    mail_domain: CliGlobalSystemLogMailDomain
    pcap_file: CliGlobalSystemLogPcapFile
    ratelimit: CliGlobalSystemLogRatelimit
    settings: CliGlobalSystemLogSettings
    topology: CliGlobalSystemLogTopology
    ueba: CliGlobalSystemLogUeba

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

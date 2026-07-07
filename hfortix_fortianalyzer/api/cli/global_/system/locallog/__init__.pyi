"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .disk import Disk
    from .fortianalyzer import Fortianalyzer
    from .fortianalyzer2 import Fortianalyzer2
    from .fortianalyzer3 import Fortianalyzer3
    from .memory import Memory
    from .setting import CliGlobalSystemLocallogSetting
    from .syslogd import Syslogd
    from .syslogd2 import Syslogd2
    from .syslogd3 import Syslogd3
    from .tacacs_accounting import Tacacsaccounting

__all__ = ["Locallog"]


class Locallog:
    """Locallog endpoints."""

    disk: Disk
    fortianalyzer: Fortianalyzer
    fortianalyzer2: Fortianalyzer2
    fortianalyzer3: Fortianalyzer3
    memory: Memory
    setting: CliGlobalSystemLocallogSetting
    syslogd: Syslogd
    syslogd2: Syslogd2
    syslogd3: Syslogd3
    tacacs_accounting: Tacacsaccounting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

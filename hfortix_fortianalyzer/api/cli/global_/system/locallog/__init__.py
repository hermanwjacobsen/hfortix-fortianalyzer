"""FortiAnalyzer locallog system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import disk
    from . import fortianalyzer
    from . import fortianalyzer2
    from . import fortianalyzer3
    from . import memory
    from . import setting
    from . import syslogd
    from . import syslogd2
    from . import syslogd3
    from . import tacacs_accounting

__all__ = ["Locallog"]


class Locallog:
    """FortiAnalyzer locallog system API endpoints."""

    disk: "disk.Disk"
    fortianalyzer: "fortianalyzer.Fortianalyzer"
    fortianalyzer2: "fortianalyzer2.Fortianalyzer2"
    fortianalyzer3: "fortianalyzer3.Fortianalyzer3"
    memory: "memory.Memory"
    setting: "setting.CliGlobalSystemLocallogSetting"
    syslogd: "syslogd.Syslogd"
    syslogd2: "syslogd2.Syslogd2"
    syslogd3: "syslogd3.Syslogd3"
    tacacs_accounting: "tacacs_accounting.Tacacsaccounting"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Locallog namespace with JSON-RPC client."""
        from . import disk as disk_module
        from . import fortianalyzer as fortianalyzer_module
        from . import fortianalyzer2 as fortianalyzer2_module
        from . import fortianalyzer3 as fortianalyzer3_module
        from . import memory as memory_module
        from . import setting as setting_module
        from . import syslogd as syslogd_module
        from . import syslogd2 as syslogd2_module
        from . import syslogd3 as syslogd3_module
        from . import tacacs_accounting as tacacs_accounting_module

        self.disk = disk_module.Disk(client)
        self.fortianalyzer = fortianalyzer_module.Fortianalyzer(client)
        self.fortianalyzer2 = fortianalyzer2_module.Fortianalyzer2(client)
        self.fortianalyzer3 = fortianalyzer3_module.Fortianalyzer3(client)
        self.memory = memory_module.Memory(client)
        self.setting = setting_module.CliGlobalSystemLocallogSetting(client)
        self.syslogd = syslogd_module.Syslogd(client)
        self.syslogd2 = syslogd2_module.Syslogd2(client)
        self.syslogd3 = syslogd3_module.Syslogd3(client)
        self.tacacs_accounting = tacacs_accounting_module.Tacacsaccounting(client)

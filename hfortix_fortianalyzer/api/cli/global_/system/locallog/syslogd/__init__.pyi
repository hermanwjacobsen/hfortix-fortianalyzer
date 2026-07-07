"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .filter import CliGlobalSystemLocallogSyslogdFilter
    from .setting import CliGlobalSystemLocallogSyslogdSetting

__all__ = ["Syslogd"]


class Syslogd:
    """Syslogd endpoints."""

    filter: CliGlobalSystemLocallogSyslogdFilter
    setting: CliGlobalSystemLocallogSyslogdSetting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

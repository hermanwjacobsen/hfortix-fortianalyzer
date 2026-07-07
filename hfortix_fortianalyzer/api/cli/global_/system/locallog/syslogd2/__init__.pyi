"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .filter import CliGlobalSystemLocallogSyslogd2Filter
    from .setting import CliGlobalSystemLocallogSyslogd2Setting

__all__ = ["Syslogd2"]


class Syslogd2:
    """Syslogd2 endpoints."""

    filter: CliGlobalSystemLocallogSyslogd2Filter
    setting: CliGlobalSystemLocallogSyslogd2Setting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

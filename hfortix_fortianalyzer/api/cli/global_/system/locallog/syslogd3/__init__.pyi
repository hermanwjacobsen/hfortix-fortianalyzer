"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .filter import CliGlobalSystemLocallogSyslogd3Filter
    from .setting import CliGlobalSystemLocallogSyslogd3Setting

__all__ = ["Syslogd3"]


class Syslogd3:
    """Syslogd3 endpoints."""

    filter: CliGlobalSystemLocallogSyslogd3Filter
    setting: CliGlobalSystemLocallogSyslogd3Setting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

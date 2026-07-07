"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ntpserver import CliGlobalSystemNtpNtpserver

__all__ = ["CliGlobalSystemNtp"]


from ..ntp_base import CliGlobalSystemNtp as CliGlobalSystemNtpBase

class CliGlobalSystemNtp(CliGlobalSystemNtpBase):
    """CliGlobalSystemNtp endpoints."""

    ntpserver: CliGlobalSystemNtpNtpserver

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

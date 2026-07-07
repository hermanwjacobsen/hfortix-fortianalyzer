"""FortiAnalyzer ntp system API endpoints."""

from __future__ import annotations

from ..ntp_base import CliGlobalSystemNtp as CliGlobalSystemNtpBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ntpserver

__all__ = ["CliGlobalSystemNtp"]


class CliGlobalSystemNtp(CliGlobalSystemNtpBase):
    """FortiAnalyzer ntp system API endpoints."""

    ntpserver: "ntpserver.CliGlobalSystemNtpNtpserver"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemNtp with endpoint methods and child modules."""
        super().__init__(client)

        from . import ntpserver as ntpserver_module

        self.ntpserver = ntpserver_module.CliGlobalSystemNtpNtpserver(client)

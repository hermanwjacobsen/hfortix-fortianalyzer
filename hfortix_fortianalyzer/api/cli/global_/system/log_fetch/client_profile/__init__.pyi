"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .device_filter import CliGlobalSystemLogFetchClientProfileDeviceFilter
    from .log_filter import CliGlobalSystemLogFetchClientProfileLogFilter

__all__ = ["CliGlobalSystemLogFetchClientProfile"]


from ..client_profile_base import CliGlobalSystemLogFetchClientProfile as CliGlobalSystemLogFetchClientProfileBase

class CliGlobalSystemLogFetchClientProfile(CliGlobalSystemLogFetchClientProfileBase):
    """CliGlobalSystemLogFetchClientProfile endpoints."""

    device_filter: CliGlobalSystemLogFetchClientProfileDeviceFilter
    log_filter: CliGlobalSystemLogFetchClientProfileLogFilter

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .device_filter import CliGlobalSystemLogForwardDeviceFilter
    from .log_field_exclusion import CliGlobalSystemLogForwardLogFieldExclusion
    from .log_filter import CliGlobalSystemLogForwardLogFilter
    from .log_masking_custom import CliGlobalSystemLogForwardLogMaskingCustom

__all__ = ["CliGlobalSystemLogForward"]


from ..log_forward_base import CliGlobalSystemLogForward as CliGlobalSystemLogForwardBase

class CliGlobalSystemLogForward(CliGlobalSystemLogForwardBase):
    """CliGlobalSystemLogForward endpoints."""

    device_filter: CliGlobalSystemLogForwardDeviceFilter
    log_field_exclusion: CliGlobalSystemLogForwardLogFieldExclusion
    log_filter: CliGlobalSystemLogForwardLogFilter
    log_masking_custom: CliGlobalSystemLogForwardLogMaskingCustom

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

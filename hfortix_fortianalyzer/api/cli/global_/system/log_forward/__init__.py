"""FortiAnalyzer log_forward system API endpoints."""

from __future__ import annotations

from ..log_forward_base import CliGlobalSystemLogForward as CliGlobalSystemLogForwardBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import device_filter
    from . import log_field_exclusion
    from . import log_filter
    from . import log_masking_custom

__all__ = ["CliGlobalSystemLogForward"]


class CliGlobalSystemLogForward(CliGlobalSystemLogForwardBase):
    """FortiAnalyzer log_forward system API endpoints."""

    device_filter: "device_filter.CliGlobalSystemLogForwardDeviceFilter"
    log_field_exclusion: "log_field_exclusion.CliGlobalSystemLogForwardLogFieldExclusion"
    log_filter: "log_filter.CliGlobalSystemLogForwardLogFilter"
    log_masking_custom: "log_masking_custom.CliGlobalSystemLogForwardLogMaskingCustom"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemLogForward with endpoint methods and child modules."""
        super().__init__(client)

        from . import device_filter as device_filter_module
        from . import log_field_exclusion as log_field_exclusion_module
        from . import log_filter as log_filter_module
        from . import log_masking_custom as log_masking_custom_module

        self.device_filter = device_filter_module.CliGlobalSystemLogForwardDeviceFilter(client)
        self.log_field_exclusion = log_field_exclusion_module.CliGlobalSystemLogForwardLogFieldExclusion(client)
        self.log_filter = log_filter_module.CliGlobalSystemLogForwardLogFilter(client)
        self.log_masking_custom = log_masking_custom_module.CliGlobalSystemLogForwardLogMaskingCustom(client)

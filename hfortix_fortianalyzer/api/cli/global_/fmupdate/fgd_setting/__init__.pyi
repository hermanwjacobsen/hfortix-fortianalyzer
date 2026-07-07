"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .server_override import CliGlobalFmupdateFgdSettingServerOverride

__all__ = ["CliGlobalFmupdateFgdSetting"]


from ..fgd_setting_base import CliGlobalFmupdateFgdSetting as CliGlobalFmupdateFgdSettingBase

class CliGlobalFmupdateFgdSetting(CliGlobalFmupdateFgdSettingBase):
    """CliGlobalFmupdateFgdSetting endpoints."""

    server_override: CliGlobalFmupdateFgdSettingServerOverride

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

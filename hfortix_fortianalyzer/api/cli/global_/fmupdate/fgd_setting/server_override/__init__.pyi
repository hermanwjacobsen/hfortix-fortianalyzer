"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .servlist import CliGlobalFmupdateFgdSettingServerOverrideServlist

__all__ = ["CliGlobalFmupdateFgdSettingServerOverride"]


from ..server_override_base import CliGlobalFmupdateFgdSettingServerOverride as CliGlobalFmupdateFgdSettingServerOverrideBase

class CliGlobalFmupdateFgdSettingServerOverride(CliGlobalFmupdateFgdSettingServerOverrideBase):
    """CliGlobalFmupdateFgdSettingServerOverride endpoints."""

    servlist: CliGlobalFmupdateFgdSettingServerOverrideServlist

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

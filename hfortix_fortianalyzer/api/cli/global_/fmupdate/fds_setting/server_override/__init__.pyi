"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .servlist import CliGlobalFmupdateFdsSettingServerOverrideServlist

__all__ = ["CliGlobalFmupdateFdsSettingServerOverride"]


from ..server_override_base import CliGlobalFmupdateFdsSettingServerOverride as CliGlobalFmupdateFdsSettingServerOverrideBase

class CliGlobalFmupdateFdsSettingServerOverride(CliGlobalFmupdateFdsSettingServerOverrideBase):
    """CliGlobalFmupdateFdsSettingServerOverride endpoints."""

    servlist: CliGlobalFmupdateFdsSettingServerOverrideServlist

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

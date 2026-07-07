"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .member import CliGlobalSystemAdminGroupMember

__all__ = ["CliGlobalSystemAdminGroup"]


from ..group_base import CliGlobalSystemAdminGroup as CliGlobalSystemAdminGroupBase

class CliGlobalSystemAdminGroup(CliGlobalSystemAdminGroupBase):
    """CliGlobalSystemAdminGroup endpoints."""

    member: CliGlobalSystemAdminGroupMember

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

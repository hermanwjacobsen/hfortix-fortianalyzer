"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .object_member import DvmdbAdomGroupObjectMember

__all__ = ["DvmdbAdomGroup"]


from ..group_base import DvmdbAdomGroup as DvmdbAdomGroupBase

class DvmdbAdomGroup(DvmdbAdomGroupBase):
    """DvmdbAdomGroup endpoints."""

    object_member: DvmdbAdomGroupObjectMember

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

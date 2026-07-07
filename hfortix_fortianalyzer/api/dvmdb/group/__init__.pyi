"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .object_member import DvmdbGroupObjectMember

__all__ = ["DvmdbGroup"]


from ..group_base import DvmdbGroup as DvmdbGroupBase

class DvmdbGroup(DvmdbGroupBase):
    """DvmdbGroup endpoints."""

    object_member: DvmdbGroupObjectMember

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

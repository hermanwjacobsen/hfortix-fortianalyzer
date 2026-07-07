"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .device import DvmdbAdomDevice
    from .folder import DvmdbAdomFolder
    from .group import DvmdbAdomGroup
    from .object_member import DvmdbAdomObjectMember

__all__ = ["DvmdbAdom"]


from ..adom_base import DvmdbAdom as DvmdbAdomBase

class DvmdbAdom(DvmdbAdomBase):
    """DvmdbAdom endpoints."""

    device: DvmdbAdomDevice
    folder: DvmdbAdomFolder
    group: DvmdbAdomGroup
    object_member: DvmdbAdomObjectMember

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

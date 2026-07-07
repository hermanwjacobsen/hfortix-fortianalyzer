"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .adom import DvmdbAdom
    from .device import DvmdbDevice
    from .folder import DvmdbFolder
    from .group import DvmdbGroup

__all__ = ["Dvmdb"]


class Dvmdb:
    """Dvmdb endpoints."""

    adom: DvmdbAdom
    device: DvmdbDevice
    folder: DvmdbFolder
    group: DvmdbGroup

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

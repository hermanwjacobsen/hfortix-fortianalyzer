"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .admins import CliGlobalSystemMetadataAdmins

__all__ = ["Metadata"]


class Metadata:
    """Metadata endpoints."""

    admins: CliGlobalSystemMetadataAdmins

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

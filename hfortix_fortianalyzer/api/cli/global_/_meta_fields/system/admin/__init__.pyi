"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .user import CliGlobalMetaFieldsSystemAdminUser

__all__ = ["Admin"]


class Admin:
    """Admin endpoints."""

    user: CliGlobalMetaFieldsSystemAdminUser

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

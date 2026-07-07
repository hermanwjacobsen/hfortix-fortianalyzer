"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .dev_list import DvmCmdImportDevList

__all__ = ["Import"]


class Import:
    """Import endpoints."""

    dev_list: DvmCmdImportDevList

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

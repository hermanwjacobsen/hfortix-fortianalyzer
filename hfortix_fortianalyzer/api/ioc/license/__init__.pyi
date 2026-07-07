"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .state import IocLicenseState

__all__ = ["License"]


class License:
    """License endpoints."""

    state: IocLicenseState

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

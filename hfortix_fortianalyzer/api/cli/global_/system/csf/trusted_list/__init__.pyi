"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .adom import CliGlobalSystemCsfTrustedListAdom

__all__ = ["CliGlobalSystemCsfTrustedList"]


from ..trusted_list_base import CliGlobalSystemCsfTrustedList as CliGlobalSystemCsfTrustedListBase

class CliGlobalSystemCsfTrustedList(CliGlobalSystemCsfTrustedListBase):
    """CliGlobalSystemCsfTrustedList endpoints."""

    adom: CliGlobalSystemCsfTrustedListAdom

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .trusted_list import CliGlobalSystemSocFabricTrustedList

__all__ = ["CliGlobalSystemSocFabric"]


from ..soc_fabric_base import CliGlobalSystemSocFabric as CliGlobalSystemSocFabricBase

class CliGlobalSystemSocFabric(CliGlobalSystemSocFabricBase):
    """CliGlobalSystemSocFabric endpoints."""

    trusted_list: CliGlobalSystemSocFabricTrustedList

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

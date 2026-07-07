"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .fabric_connector import CliGlobalSystemCsfFabricConnector
    from .trusted_list import CliGlobalSystemCsfTrustedList

__all__ = ["CliGlobalSystemCsf"]


from ..csf_base import CliGlobalSystemCsf as CliGlobalSystemCsfBase

class CliGlobalSystemCsf(CliGlobalSystemCsfBase):
    """CliGlobalSystemCsf endpoints."""

    fabric_connector: CliGlobalSystemCsfFabricConnector
    trusted_list: CliGlobalSystemCsfTrustedList

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

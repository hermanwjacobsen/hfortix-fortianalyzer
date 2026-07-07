"""FortiAnalyzer csf system API endpoints."""

from __future__ import annotations

from ..csf_base import CliGlobalSystemCsf as CliGlobalSystemCsfBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import fabric_connector
    from . import trusted_list

__all__ = ["CliGlobalSystemCsf"]


class CliGlobalSystemCsf(CliGlobalSystemCsfBase):
    """FortiAnalyzer csf system API endpoints."""

    fabric_connector: "fabric_connector.CliGlobalSystemCsfFabricConnector"
    trusted_list: "trusted_list.CliGlobalSystemCsfTrustedList"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemCsf with endpoint methods and child modules."""
        super().__init__(client)

        from . import fabric_connector as fabric_connector_module
        from . import trusted_list as trusted_list_module

        self.fabric_connector = fabric_connector_module.CliGlobalSystemCsfFabricConnector(client)
        self.trusted_list = trusted_list_module.CliGlobalSystemCsfTrustedList(client)

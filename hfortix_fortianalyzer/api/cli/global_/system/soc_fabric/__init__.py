"""FortiAnalyzer soc_fabric system API endpoints."""

from __future__ import annotations

from ..soc_fabric_base import CliGlobalSystemSocFabric as CliGlobalSystemSocFabricBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import trusted_list

__all__ = ["CliGlobalSystemSocFabric"]


class CliGlobalSystemSocFabric(CliGlobalSystemSocFabricBase):
    """FortiAnalyzer soc_fabric system API endpoints."""

    trusted_list: "trusted_list.CliGlobalSystemSocFabricTrustedList"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemSocFabric with endpoint methods and child modules."""
        super().__init__(client)

        from . import trusted_list as trusted_list_module

        self.trusted_list = trusted_list_module.CliGlobalSystemSocFabricTrustedList(client)

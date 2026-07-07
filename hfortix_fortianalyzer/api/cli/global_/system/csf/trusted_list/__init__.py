"""FortiAnalyzer trusted_list csf API endpoints."""

from __future__ import annotations

from ..trusted_list_base import CliGlobalSystemCsfTrustedList as CliGlobalSystemCsfTrustedListBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom

__all__ = ["CliGlobalSystemCsfTrustedList"]


class CliGlobalSystemCsfTrustedList(CliGlobalSystemCsfTrustedListBase):
    """FortiAnalyzer trusted_list csf API endpoints."""

    adom: "adom.CliGlobalSystemCsfTrustedListAdom"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemCsfTrustedList with endpoint methods and child modules."""
        super().__init__(client)

        from . import adom as adom_module

        self.adom = adom_module.CliGlobalSystemCsfTrustedListAdom(client)

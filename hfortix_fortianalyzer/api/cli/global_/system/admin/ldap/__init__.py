"""FortiAnalyzer ldap admin API endpoints."""

from __future__ import annotations

from ..ldap_base import CliGlobalSystemAdminLdap as CliGlobalSystemAdminLdapBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom

__all__ = ["CliGlobalSystemAdminLdap"]


class CliGlobalSystemAdminLdap(CliGlobalSystemAdminLdapBase):
    """FortiAnalyzer ldap admin API endpoints."""

    adom: "adom.CliGlobalSystemAdminLdapAdom"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemAdminLdap with endpoint methods and child modules."""
        super().__init__(client)

        from . import adom as adom_module

        self.adom = adom_module.CliGlobalSystemAdminLdapAdom(client)

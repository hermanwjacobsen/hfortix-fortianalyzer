"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .adom import CliGlobalSystemAdminLdapAdom

__all__ = ["CliGlobalSystemAdminLdap"]


from ..ldap_base import CliGlobalSystemAdminLdap as CliGlobalSystemAdminLdapBase

class CliGlobalSystemAdminLdap(CliGlobalSystemAdminLdapBase):
    """CliGlobalSystemAdminLdap endpoints."""

    adom: CliGlobalSystemAdminLdapAdom

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

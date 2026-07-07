"""FortiAnalyzer saml system API endpoints."""

from __future__ import annotations

from ..saml_base import CliGlobalSystemSaml as CliGlobalSystemSamlBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import fabric_idp
    from . import service_providers

__all__ = ["CliGlobalSystemSaml"]


class CliGlobalSystemSaml(CliGlobalSystemSamlBase):
    """FortiAnalyzer saml system API endpoints."""

    fabric_idp: "fabric_idp.CliGlobalSystemSamlFabricIdp"
    service_providers: "service_providers.CliGlobalSystemSamlServiceProviders"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemSaml with endpoint methods and child modules."""
        super().__init__(client)

        from . import fabric_idp as fabric_idp_module
        from . import service_providers as service_providers_module

        self.fabric_idp = fabric_idp_module.CliGlobalSystemSamlFabricIdp(client)
        self.service_providers = service_providers_module.CliGlobalSystemSamlServiceProviders(client)

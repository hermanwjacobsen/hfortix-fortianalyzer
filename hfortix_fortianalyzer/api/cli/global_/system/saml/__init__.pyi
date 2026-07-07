"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .fabric_idp import CliGlobalSystemSamlFabricIdp
    from .service_providers import CliGlobalSystemSamlServiceProviders

__all__ = ["CliGlobalSystemSaml"]


from ..saml_base import CliGlobalSystemSaml as CliGlobalSystemSamlBase

class CliGlobalSystemSaml(CliGlobalSystemSamlBase):
    """CliGlobalSystemSaml endpoints."""

    fabric_idp: CliGlobalSystemSamlFabricIdp
    service_providers: CliGlobalSystemSamlServiceProviders

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

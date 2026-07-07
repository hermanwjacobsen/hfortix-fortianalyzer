"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .export import SoarAdomSubnetExport
    from .import_ import SoarAdomSubnetImport

__all__ = ["Subnet"]


class Subnet:
    """Subnet endpoints."""

    export: SoarAdomSubnetExport
    import_: SoarAdomSubnetImport

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

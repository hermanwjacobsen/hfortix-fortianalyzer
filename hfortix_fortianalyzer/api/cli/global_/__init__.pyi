"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from ._meta_fields import Metafields
    from .exec import Exec
    from .fmupdate import Fmupdate
    from .system import System

__all__ = ["Global"]


class Global:
    """Global endpoints."""

    _meta_fields: Metafields
    exec: Exec
    fmupdate: Fmupdate
    system: System

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

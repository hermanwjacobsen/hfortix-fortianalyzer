"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .add import Add
    from .del_ import Del
    from .import_ import Import

__all__ = ["Cmd"]


class Cmd:
    """Cmd endpoints."""

    add: Add
    del_: Del
    import_: Import

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

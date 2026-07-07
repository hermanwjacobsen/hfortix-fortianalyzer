"""FortiAnalyzer cmd API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import add
    from . import del_
    from . import import_

__all__ = ["Cmd"]


class Cmd:
    """FortiAnalyzer cmd API endpoints."""

    add: "add.Add"
    del_: "del_.Del"
    import_: "import_.Import"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Cmd namespace with JSON-RPC client."""
        from . import add as add_module
        from . import del_ as del__module
        from . import import_ as import__module

        self.add = add_module.Add(client)
        self.del_ = del__module.Del(client)
        self.import_ = import__module.Import(client)

"""FortiAnalyzer API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import dvmdb

__all__ = ["API"]


class API:
    """FortiAnalyzer API endpoints."""

    dvmdb: "dvmdb.Dvmdb"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize API namespace with JSON-RPC client."""
        from . import dvmdb as dvmdb_module

        self.dvmdb = dvmdb_module.Dvmdb(client)

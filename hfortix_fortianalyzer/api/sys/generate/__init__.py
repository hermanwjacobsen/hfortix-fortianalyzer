"""FortiAnalyzer generate API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import wsdl

__all__ = ["Generate"]


class Generate:
    """FortiAnalyzer generate API endpoints."""

    wsdl: "wsdl.SysGenerateWsdl"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Generate namespace with JSON-RPC client."""
        from . import wsdl as wsdl_module

        self.wsdl = wsdl_module.SysGenerateWsdl(client)

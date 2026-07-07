"""FortiAnalyzer global_ API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import _meta_fields
    from . import exec
    from . import fmupdate
    from . import system

__all__ = ["Global"]


class Global:
    """FortiAnalyzer global_ API endpoints."""

    _meta_fields: "_meta_fields.Metafields"
    exec: "exec.Exec"
    fmupdate: "fmupdate.Fmupdate"
    system: "system.System"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Global namespace with JSON-RPC client."""
        from . import _meta_fields as _meta_fields_module
        from . import exec as exec_module
        from . import fmupdate as fmupdate_module
        from . import system as system_module

        self._meta_fields = _meta_fields_module.Metafields(client)
        self.exec = exec_module.Exec(client)
        self.fmupdate = fmupdate_module.Fmupdate(client)
        self.system = system_module.System(client)

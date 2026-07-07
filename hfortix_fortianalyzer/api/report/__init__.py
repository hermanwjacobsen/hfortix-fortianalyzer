"""FortiAnalyzer report API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import adom
    from . import config
    from . import template

__all__ = ["Report"]


class Report:
    """FortiAnalyzer report API endpoints."""

    adom: "adom.Adom"
    config: "config.Config"
    template: "template.Template"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Report namespace with JSON-RPC client."""
        from . import adom as adom_module
        from . import config as config_module
        from . import template as template_module

        self.adom = adom_module.Adom(client)
        self.config = config_module.Config(client)
        self.template = template_module.Template(client)

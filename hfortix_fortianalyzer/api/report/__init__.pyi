"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .adom import Adom
    from .config import Config
    from .template import Template

__all__ = ["Report"]


class Report:
    """Report endpoints."""

    adom: Adom
    config: Config
    template: Template

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
